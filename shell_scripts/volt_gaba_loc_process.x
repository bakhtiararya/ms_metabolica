#!/bin/csh -f

# calculate % of subcortical ROIs using HOSub25 atlas
# convert all the voxel locations in MNI152 space and generate averaged ROIs
# 2017/03/16

# $Header: written by Yan Li 


set datapath = /data/lhst2/7T_volunteer_scans_MRS

#set blist = (20150501_gaba 20150505_1_gaba 20150505_2_gaba 20150506_gaba 20150507_gaba 20150729_gaba)
set blist = (20150505_2_gaba)
set subdir = (acc aud caud)
set addroi = 0 

foreach bnum ($blist)
	cd ${datapath}/$bnum
	echo $bnum
	set ename = `ls -d E* | cut -d"/" -f1`	
	
	if (-e images) then
		if (! -e images_1) then			
			mv images images_1
		else
			mv images images_2
		endif	
	endif

	#if (-e t1_analysis) then
	#	/bin/rm -r t1_analysis
	#endif

	foreach rois ($subdir)
		foreach stime (1 2)	
			cd ${datapath}/$bnum
			if (! -e t1_analysis_$stime) then  
				mkdir t1_analysis_$stime
			endif
			cd ${datapath}/$bnum/t1_analysis_$stime
	
			if (! -e ${ename}_t1v_exam${stime}_reorient_br.nii.gz) then
				cp ../images_${stime}/${ename}_t1v.int2 ${ename}_t1v_exam${stime}.int2
				cp ../images_${stime}/${ename}_t1v.idf ${ename}_t1v_exam${stime}.idf
				fix_rootname.x ${ename}_t1v_exam${stime}
				nifti_file_convert --input ${ename}_t1v_exam${stime}.int2 --output_root ${ename}_t1v_exam${stime}
				fslreorient2std ${ename}_t1v_exam${stime}.nii.gz ${ename}_t1v_exam${stime}_reorient
				bet ${ename}_t1v_exam${stime}_reorient.nii.gz  ${ename}_t1v_exam${stime}_reorient_br -f 0.3 -g 0.09 
			endif

			if (! -e ${ename}_t1v_exam${stime}_to_MNI_transform.mat) then
				flirt -in ${ename}_t1v_exam${stime}_reorient.nii.gz -ref /netopt/fsl_versions/fsl_5.0.1/data/standard/MNI152_T1_1mm.nii.gz -omat ${ename}_t1v_exam${stime}_to_MNI_transform.mat -out ${ename}_t1v_exam${stime}_reorient_to_MNI
			endif

			if (! -e HOsub25_to_${ename}_t1v_exam${stime}.nii.gz) then
				flirt -in /netopt/fsl_versions/fsl_5.0.1/data/standard/MNI152_T1_1mm.nii.gz -ref ${ename}_t1v_exam${stime}_reorient.nii.gz -omat MNI_to_${ename}_t1v_exam${stime}_transform.mat -out MNI_to_${ename}_t1v_exam${stime}_reorient
				flirt -in /netopt/fsl_versions/fsl_5.0.1/data/atlases/HarvardOxford/HarvardOxford-sub-maxprob-thr25-1mm.nii.gz -ref ${ename}_t1v_exam${stime}_reorient.nii.gz -out HOsub25_to_${ename}_t1v_exam${stime}  -init MNI_to_${ename}_t1v_exam${stime}_transform.mat -applyxfm -interp nearestneighbour
				nifti_file_convert --input HOsub25_to_${ename}_t1v_exam${stime}.nii.gz --output_root HOsub25_to_${ename}_t1v_exam${stime}
			endif

			if (! -e ${ename}_${rois}_${stime}_pressr_reorient.nii.gz)  then
				cp ../spectra_${rois}_${stime}/${ename}_${rois}_${stime}_dif_cor_sum_comb_phased.cmplx .
				cp ../spectra_${rois}_${stime}/${ename}_${rois}_${stime}_dif_cor_sum_comb_phased.ddf .
				if (-e ${ename}_aud_${stime}_dif_cor_sum_comb_phased.ddf) then
					/home/liyan/script/cshellscript/edit_aud_si_thick.x ${ename}_aud_${stime}_dif_cor_sum_comb_phased.ddf
				endif			
				/home/liyan/script/serial_spectra/press_2d_profile.x ${ename}_${rois}_${stime}_dif_cor_sum_comb_phased ${ename}_${rois}_${stime} 
				resample_image ${ename}_${rois}_${stime}_press.int2 ${ename}_t1v_exam${stime}.int2
				nifti_file_convert --input ${ename}_${rois}_${stime}_pressr.int2 --output_root ${ename}_${rois}_${stime}_pressr
				fslreorient2std ${ename}_${rois}_${stime}_pressr.nii.gz ${ename}_${rois}_${stime}_pressr_reorient
			endif

			if (! -e ${ename}_t1v_exam${stime}_reorient_br_pve_1.nii.gz) then
				fast -H 0.3  ${ename}_t1v_exam${stime}_reorient_br.nii.gz
			endif
			nifti_file_convert --input ${ename}_t1v_exam${stime}_reorient_br_pve_1.nii.gz --output_root ${ename}_t1v_exam${stime}_reorient_br_pve_1
			convert_ddfidf.x ${ename}_${rois}_${stime}_dif_cor_sum_comb_phased ${ename}_${rois}_${stime}_dif_cor_sum_comb_phased
			percent_image.x ${ename}_t1v_exam${stime}_reorient_br_pve_1.int2 ${ename}_${rois}_${stime}_dif_cor_sum_comb_phased ${ename}_${rois}_exam${stime}_percent
			if (-e ${ename}_caud_${stime}_dif_cor_sum_comb_phased.idf) then
				percent_image.x HOsub25_RightCaudate_to_${ename}_t1v_exam${stime}.int2 ${ename}_caud_${stime}_dif_cor_sum_comb_phased ${ename}_caud_exam${stime}_HOsub25_percent	
			endif

			if (! -e ${ename}_${rois}_${stime}_pressr_reorient_to_MNI.nii.gz) then
				flirt -in ${ename}_${rois}_${stime}_pressr_reorient.nii.gz -ref /netopt/fsl_versions/fsl_5.0.1/data/standard/MNI152_T1_1mm.nii.gz -out ${ename}_${rois}_${stime}_pressr_reorient_to_MNI  -init ${ename}_t1v_exam${stime}_to_MNI_transform.mat -applyxfm -interp nearestneighbour
			endif
				
			if (! -e ${ename}_${rois}_${stime}_pressr_reorient_to_MNI.nii.gz) then
				echo "ERROR"
			else
				cp ${ename}_${rois}_${stime}_pressr_reorient_to_MNI.nii.gz /working/brain1/brain_work/yan/pt_7t/volt_gaba_loc
			endif
			cd /working/brain1/brain_work/yan/pt_7t/volt_gaba_loc	
		nifti_file_convert --input  ${ename}_${rois}_${stime}_pressr_reorient_to_MNI.nii.gz --output_root ${ename}_${rois}_${stime}_pressr_reorient_to_MNI

		end
		cd /working/brain1/brain_work/yan/pt_7t/volt_gaba_loc	
		if (! -e ${ename}_${rois}_pressr_reorient_to_MNI.nii.gz) then
			fslmaths ${ename}_${rois}_1_pressr_reorient_to_MNI.nii.gz -add ${ename}_${rois}_2_pressr_reorient_to_MNI.nii.gz ${ename}_${rois}_pressr_reorient_to_MNI
			nifti_file_convert --input ${ename}_${rois}_pressr_reorient_to_MNI.nii.gz --output_root ${ename}_${rois}_pressr_reorient_to_MNI		
		endif

	end
end

if ($addroi == 1) then
   cd /working/brain1/brain_work/yan/pt_7t/volt_gaba_loc
   foreach rois ($subdir)
	echo ${rois}
	set roilist = `ls *_${rois}_pressr_reorient_to_MNI.nii.gz`
	set n = `ls *_${rois}_pressr_reorient_to_MNI.nii.gz | wc -l`		
	if ($n > 0) then
		set z = 2
		set file1 = `echo $roilist | awk '{print $1}'`
		set file1_out = `echo $file1 | cut -d"." -f1`
		nifti_file_convert --input ${file1} --output_root ${file1_out}
		while ($z <= $n)
			set file2 = `echo $roilist | cut -d" " -f${z}`
			set file2_out = `echo $file2 | cut -d"." -f1`
			nifti_file_convert --input ${file2} --output_root ${file2_out}
			fslmaths ${file1} -add ${file2} temp
			set z = `arithmetic $z + 1`
			set z = `echo $z | cut -d'.' -f1`
			set file1 = temp.nii.gz 
		end
		mv temp.nii.gz volt_${rois}.nii.gz
		fslmaths volt_${rois}.nii.gz -div 1000  volt_${rois}_max1
		nifti_file_convert --input  volt_${rois}.nii.gz --output_root volt_${rois}
		nifti_file_convert --input  volt_${rois}_max1.nii.gz --output_root volt_${rois}_max1
	endif	
    end
endif


