#!/bin/csh -f

# $Header: written by Yan Li 

# process high resolution sLASER EPSI/flyback


# this specifies where the NAC study raw data files are
set datapath = /data/waubant1/7T_NAC_MS_GSH
# svk_multi_view t1v and fla
set viewflag = 0 
# process MRSI data
set processflag = 0
# align Atlas ROIs
set roiflag = 0
# svk_multi_view atlas ROIs
set checkroi = 0
# resample ROI % to spectra resolution
set specroi = 0
# Lcmodel quantification
set quantification = 0
set filename = NAC_7T_MRS_List
if (-e ${datapath}/${filename}.csv) then
	/bin/rm ${datapath}/${filename}.csv
endif
echo "n,bnum,tnum,exam,mrn" > ${datapath}/${filename}.csv

# check the dataset 
echo " "
cd $datapath
set sublist = `ls -d subj*/*` # list out the name of the folder for every (subject, timepoint) pair 
set nsub = `ls -d subj*/ | wc -l` # counts the number of subject 
set nscan = `ls -d subj*/*_* --ignore='*.*' | wc -l` # counts the number of scans
echo " Total $nsub patients $nscan Scans" # tells the user the number of patients and scans
set nimage = `ls -d subj*/*/images | wc -l` # supposed to give total number of image folder spread over all patients
set nt1v = `ls -d subj*/*/images/*_t1v.idf | wc -l` # total number of t1 reference images that can be found
echo " Total $nimage Dimage and $nt1v T1v" 
echo " "


set n = 1
foreach i ($sublist)
	set tempdata = $sublist[1] # reference subj01/2016_11_04
	set bnum = `echo $tempdata | cut -d"/" -f1` 
	set tnum = `echo $tempdata | cut -d"/" -f2`
	if (-e ${datapath}/${bnum}/${tnum}/images) then	
		
		cd $datapath/$bnum/$tnum
		set exam = `ls -d E*` # set exam to be the name of the folder which contains the DICOMs
		set exam = `echo $exam | cut -d"/" -f1` # extract the directory name only
		#	echo $n $bnum $tnum $exam
		
		if (! -e $datapath/$bnum/$tnum/images/${exam}_t1v.idf) then
			echo "   $n $bnum $tnum $exam - missing ${exam}_t1v.idf"
		else # we can only execute the code below if we have anatomical reference to do segmentation

	# generate HO atlas ROI analysis
			if ($roiflag == 1) then
				if (! -e $datapath/$bnum/$tnum/HOAtlas_analysis) then
					mkdir $datapath/$bnum/$tnum/HOAtlas_analysis
				endif
				if (! -e $datapath/$bnum/$tnum/HOAtlas_analysis/${exam}_t1v.int2) then
					cp $datapath/$bnum/$tnum/images/${exam}_t1v.* $datapath/$bnum/$tnum/HOAtlas_analysis/
				endif
				cd $datapath/$bnum/$tnum/HOAtlas_analysis/
				Align_HOAtlas.x ${exam}_t1v
			endif
		endif

		if (! -e $datapath/$bnum/$tnum/images/${exam}_cube_fl.idf) then
			echo "   $n $bnum $tnum $exam - missing ${exam}_cube_fl.idf"
		endif
		if (! -e $datapath/$bnum/$tnum/images/${exam}_cube_fl_ax.idf) then
			cd $datapath/$bnum/$tnum/images
			resample_image_axial ${exam}_cube_fl.int2 ${exam}_cube_fl_ax
		endif
		if (! -e $datapath/$bnum/$tnum/images/${exam}_cube_fl_axa.int2) then
			cd $datapath/$bnum/$tnum/images
			echo " aligning T2 images to T1"
		#	align_tool ${exam}_cube_fl_ax ${exam}_t1v ${exam}_cube_fl_axa
		endif
		
	# checking images		
		if ($viewflag == 1) then
			svk_multi_view $datapath/$bnum/$tnum/images/${exam}_cube_fl_axa.int2 $datapath/$bnum/$tnum/images/${exam}_t1v.int2
		endif
		
	# checking MRSI
		if (-e $datapath/$bnum/$tnum/spectra_csi) then # verifying that the spectra_csi folder exists
			set ncmplx = `ls $datapath/$bnum/$tnum/spectra_csi/*.cmplx | wc -l` # counting the number of files with ending .cmplx in timepoint folder
			if ($ncmplx > 0) then # if there are complex files
				#echo "   spectra_csi $ncmplx cmplx files"
				if (! -e $datapath/$bnum/$tnum/spectra_csi/${exam}_csi_comb_cor_sum.ddf) then
					echo "   $n $bnum $tnum $exam $ncmplx - can't find ${exam}_csi_comb_cor_sum.ddf"
				else # ensure that the *comb_cor_sum.dff exists
					if ($quantification == 1) then 
						cd $datapath/$bnum/$tnum/spectra_csi
						if (! -e LcGrid) then # if this folder isn't here, then the LCM Quantification has not been done
							GridLcModelQuant.x ${exam}_csi_comb_cor_sum
						endif
					endif
				endif
			else
				echo "   $n $bnum $tnum $exam $ncmplx - no processing?" # if there are no .cmplx, post-processing on data most likely hasn't been done
				if ($processflag == 1) then
					cd $datapath/$bnum/$tnum/spectra_csi
					# does some post-processing work to ensure that the spectra files are ready to be quantified using LCModel (i.e. regression)
					process_mrsi_7t.x ${exam}_csi --ifile / ${exam}
				endif
			endif
			if (-e $datapath/$bnum/$tnum/spectra_csi/LcGrid) then
				echo "   $n $bnum $tnum $exam - LCModel Quantification Processed"
			endif
		else
			cd $datapath/$bnum/$tnum/
			mkdir spectra_csi
			cd spectra_csi
			if (! -e $datapath/$bnum/$tnum/rawfiles/${exam}_csi) then
				echo "   $n $bnum $tnum $exam - where is raw csi file"
				set tempr = `ls $datapath/$bnum/$tnum/rawfiles/*`
				echo "  $tempr"
			else
				ln -s ../rawfiles/${exam}_csi
				ln -s ../rawfiles/${exam}_csi.dat
				if (-e ../rawfiles/${exam}_csi_sat_bands.dat) then
					ln -s ../rawfiles/${exam}_csi_sat_bands.dat
				endif
			endif
		endif	
		
		
		if (! -e $datapath/$bnum/$tnum/spectra_csi/${exam}_t1v_resampled.int2) then
			cd $datapath/$bnum/$tnum/spectra_csi/
			cp ../images/${exam}_t1v.* .
			resample_image_spectra ${exam}_t1v ${exam}_csi_comb_cor_sum
		endif
		
		if (-e $datapath/$bnum/$tnum/spectra_csi/${exam}_csi) then
			set mrnnumber = `rdump -p $datapath/$bnum/$tnum/spectra_csi/${exam}_csi | grep "Patient ID"`
			set mrnnumber = `echo $mrnnumber | cut -d":" -f2`
			set mrnnumber = `echo $mrnnumber | cut -d" " -f1`
		else
			set mrnnumber = 
		endif

	# resample ROIs to spec resolution
		if ($specroi == 1) then
			cd /data/lhst2/7T_NAC_MS_GSH/$bnum/$tnum/HOAtlas_analysis/HarvardOxford_analysis
			cp ../../spectra_csi/${exam}_csi_comb_cor_sum.ddf .
			convert_ddfidf.x ${exam}_csi_comb_cor_sum ${exam}_csi_comb_cor_sum
			if (! -e ROI_Spec/HOcort25_to_${exam}_t1v_val2_spec_percent.idf) then
			    if (! -e ROI_Spec) then
				mkdir ROI_Spec
			    endif
			     foreach r (2 3 4 29 30)
				percent_image.x HOcort25_to_${exam}_t1v_val$r.int2 ${exam}_csi_comb_cor_sum.idf  HOcort25_to_${exam}_t1v_val${r}_spec_percent
				percent_image.x HOcort25_to_${exam}_t1v_val${r}_rh.int2 ${exam}_csi_comb_cor_sum.idf  HOcort25_to_${exam}_t1v_val${r}_rh_spec_percent
				percent_image.x HOcort25_to_${exam}_t1v_val${r}_lh.int2 ${exam}_csi_comb_cor_sum.idf  HOcort25_to_${exam}_t1v_val${r}_lh_spec_percent
			    end
			     foreach r (10 11 12 13)
				percent_image.x HOsub25_to_${exam}_t1v_val${r}_lh.int2 ${exam}_csi_comb_cor_sum.idf HOsub25_to_${exam}_t1v_val${r}_lh_spec_percent
				percent_image.x HOsub25_to_${exam}_t1v_val${r}.int2 ${exam}_csi_comb_cor_sum.idf HOsub25_to_${exam}_t1v_val${r}_spec_percent
			     end
			     foreach r (49 50 51 52) 
				percent_image.x HOsub25_to_${exam}_t1v_val${r}_rh.int2 ${exam}_csi_comb_cor_sum.idf HOsub25_to_${exam}_t1v_val${r}_rh_spec_percent
			     end
			     mv -f *_spec_percent.* ROI_Spec
			endif
		endif	
		
	# checking rois
		if ($checkroi == 1) then
			cd /data/lhst2/7T_NAC_MS_GSH/$bnum/$tnum/HOAtlas_analysis/HarvardOxford_analysis
			set string = 
			if (-e /data/lhst2/7T_NAC_MS_GSH/$bnum/$tnum/HOAtlas_analysis/HarvardOxford_analysis/ROI_Spec) then
				foreach r (2 3 4 29 30)
					set string = `echo "$string ../${exam}_t1v.idf -o ROI_Spec/HOcort25_to_${exam}_t1v_val${r}_spec_percent.idf"`
				end
				foreach r (10 11)
					set string = `echo "$string ../${exam}_t1v.idf -o ROI_Spec/HOsub25_to_${exam}_t1v_val${r}_lh_spec_percent.idf"`
				end
				foreach r (12 13)
					set string = `echo "$string ../${exam}_t1v.idf -o ROI_Spec/HOsub25_to_${exam}_t1v_val${r}_spec_percent.idf"`
				end
			else		
				foreach r (2 3 4 29 30)
					set string = `echo "$string ../${exam}_t1v.idf -o HOcort25_to_${exam}_t1v_val$r.idf"`
				end
				foreach r (10 11)
					set string = `echo "$string ../${exam}_t1v.idf -o HOsub25_to_${exam}_t1v_val${r}_lh.idf"`
				end
				foreach r (12 13)
					set string = `echo "$string ../${exam}_t1v.idf -o HOsub25_to_${exam}_t1v_val${r}.idf"`
				end
			#	foreach r (49 50 51 52) 
			#		set string = `echo "$string ../${exam}_t1v.idf -o HOsub25_to_${exam}_t1v_val${r}_rh.idf"`
			#	end
			endif
			svk_multi_view $string --skipValidation
		endif
		

		
		echo "$n,$bnum,$tnum,$exam,$mrnnumber" >> ${datapath}/${filename}.csv
	#	echo " "
		@ n++
		
	else
#		echo "$tempdata $bnum $tnum missing images"
	endif
	
	shift sublist
end




