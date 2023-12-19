#!/bin/csh -f

# $Header: written by Yan Li 

set datapath = /data/lhst2/Li_Epilepsy
set outputpath = /home/liyan/projects/tle_3t

cd $datapath
set flist = `ls -d ./20*`
set n = 1

set csiproc = 0
set csiquant = 0
set svsproc = 0
set roiproc = 1
set atlasproc = 0

foreach i ($flist)
	cd $datapath
	set tempb = $flist[1]
	set bnum = `echo $tempb | cut -d"/" -f2`
	echo "$n $bnum ..."
	cd ${datapath}/${bnum}
	set exam = `ls -d E*`
	set nexam = `ls -d E* | wc -l`		
	if ($nexam != 1) then
		echo "$bnum $nexam E-folder (>1)"
		echo "Exit
		exit 1
	endif
	set exam = `echo $exam | cut -d"/" -f1`
#	echo "   Exam: $exam"
	
	if (${csiproc} == 1) then
	
		echo " Processing short TE MRSI ..."
		
		
		if (! -e ${datapath}/${bnum}/rawcsifiles) then
			echo "csi raw files do not exist"
			echo "Exit"
			exit 2
		endif 
				
		cd ${datapath}/${bnum}/rawcsifiles
		set rawname = `ls --ignore='*.*'`
	    set nraw = `ls --ignore='*.*' | wc -l` 
	    if ($nraw != 1) then
			echo "$bnum $nraw MRSI (>1)"
			echo "Exit"
			exit 3
		endif
		set rawname = `echo $rawname | cut -d"@" -f1`
		echo "   Raw file: $rawname"		
		set coilname = `rdump -A $rawname | grep "image.cname"`
		set coilname = `echo $coilname | cut -d"=" -f2 | cut -d"#" -f1`
		switch ($coilname)
			case Nova32Ch
				set chan = 32
				breaksw
			case NOVA08
				set chan = 8
				breaksw
			case 8HRBRAIN
				set chan = 8
				breaksw
			default:
				echo $coilname
				echo "Can not recognize coil"
				echo "Exit"
				exit 4
		endsw
		echo "   #Channel = $chan ($coilname)"

		if (-e ${datapath}/${bnum}/images/${exam}_ac_8.idf) then
	    	# using cal
	    	 set calibr = 1 
	    	 echo "   Cal Images: Exist"
	    else
	    	 # using rw
	    	 set calibr = 0 
	    	 echo "   Cal Images: None"
	    endif
	    	
	    cd ${datapath}/${bnum}
		if ($calibr == 1) then
			proc_short_svk.x rawcsifiles/${rawname} ${exam} ${chan} single brain_short11 fb3t self cal
		else
			proc_short_svk.x rawcsifiles/${rawname} ${exam} ${chan} single brain_short11 fb3t self rw
		endif	
		echo " "
		
	endif
	
	if (${csiquant} == 1) then
		set lcspecroot = fbfcomb_emp_cor_sum
		cd ${datapath}/${bnum}/spectra_short
		set specroot = `ls *_short_${lcspecroot}.ddf`
		set nspecroot = `ls *_short_${lcspecroot}.ddf | wc -l`
		if (${nspecroot} != 1) then
			echo " $bnum - $nspecroot spectra file ($specroot)"
		endif
		set specroot = `echo $specroot | cut -d"." -f1`
		if (-e ${specroot}.cmplx) then
			if (! -e LcGrid) then
				GridLcModelQuant.x ${specroot}  --lcsetup --lcquant --lcconvert --lcclean
				/bin/rm ${datapath}/${bnum}/spectra_short/LcGrid/lcmodel_batch.*
			endif
		endif
		
	endif
	cd ${datapath}/${bnum}/spectra_short/LcGrid
	/bin/rm *.table
	if (! -e temp_csv_files) then
		mkdir temp_csv_files
	endif
	mv -f *.csv temp_csv_files
	/bin/rm *batch*
	if (! -e temp_lcm_print) then
		mkdir temp_lcm_print
	endif
	mv -f *.PRINT temp_lcm_print
	
	if (${roiproc} == 1) then
	
		if (! -e ${datapath}/${bnum}/t1analysis) then
    		mkdir ${datapath}/${bnum}/t1analysis
    	endif
    	cd ${datapath}/${bnum}/t1analysis
    	if (! -e ${exam}_t1v.int2) then
    		ln -s ../images/${exam}_t1v.int2
    		ln -s ../images/${exam}_t1v.idf
    	endif
    #	Align_HOAtlas.x ${exam}_t1v			
    #	svk_multi_view ${exam}_t1v_reorient.int2 HOsub25_to_${exam}_t1v.int2 HOcort25_to_${exam}_t1v.int2
    	if (! -e ${exam}_t1v_wm.byt) then
	    	segment_t1v_grid.x ${exam}_t1v		
    		erode_image.x ${exam}_t1v_wm.byt ${exam}_t1v_wme.byt 2
    		mask_connect ${exam}_t1v_wme ${exam}_t1v_wm 15 4
		endif
	endif
	
	# run matlab 
		# separate_hoatlas_roi(${tnum}_t1v, 'both', 'imag')
	
	if (${roiproc} == 2) then
	
		cd ${datapath}/${bnum}/t1analysis
		set lcspecroot = fbfcomb_emp_cor_sum
		if (! -e ${exam}_short_${lcspecroot}.idf) then
			cp ../spectra_short/${exam}_short_${lcspecroot}.ddf .
			convert_ddfidf.x ${exam}_short_${lcspecroot} ${exam}_short_${lcspecroot}
			cp ${exam}_short_${lcspecroot}.idf HarvardOxford_analysis
		endif
		if (! -e ${exam}_short_${lcspecroot}_wm_percent.idf) then
	#		percent_image.x ${exam}_t1v_wm.byt ${exam}_short_${lcspecroot}.idf ${exam}_short_${lcspecroot}_wm_percent
		endif
		
		if (! -e ${datapath}/${bnum}/t1analysis/HarvardOxford_analysis) then
			echo "${bnum}/t1analysis/HarvardOxford_analysis does not exist"
			echo "Exit"
			exit 1
		endif
		cd ${datapath}/${bnum}/t1analysis/HarvardOxford_analysis	
		if (! -e ${exam}_short_${lcspecroot}.idf) then
			cp ../${exam}_short_${lcspecroot}.idf .
		endif
		foreach horoi (HOcort25  HOsub25)
			set r = 1
			while ($r <= 58)
				if (-e ${horoi}_to_${exam}_t1v_val${r}_rh.idf) then
					if (! -e ${horoi}_to_${exam}_t1v_val${r}_rh_spec_percent.idf) then
						percent_image.x ${horoi}_to_${exam}_t1v_val${r}_rh.int2 ${exam}_short_${lcspecroot}.idf  ${horoi}_to_${exam}_t1v_val${r}_rh_spec_percent
					endif
				endif	
				if (-e ${horoi}_to_${exam}_t1v_val${r}_lh.idf) then
				 	if (! -e ${horoi}_to_${exam}_t1v_val${r}_lh_spec_percent.idf) then
						percent_image.x ${horoi}_to_${exam}_t1v_val${r}_lh.int2 ${exam}_short_${lcspecroot}.idf  ${horoi}_to_${exam}_t1v_val${r}_lh_spec_percent
					endif
				endif	
				@ r++
			end	
		end
	endif
	
	if ($atlasproc == 1) then
		cd ${datapath}/${bnum}
		if (! -e atlas_analysis) then
			mkdir atlas_analysis
		endif
		cd atlas_analysis
		if (! -e ${exam}_t1v.int2) then
    		ln -s ../images/${exam}_t1v.int2
    		ln -s ../images/${exam}_t1v.idf
    	endif
    	set lcspecroot = fbfcomb_emp_cor_sum
    	set specname = ${exam}_short_${lcspecroot}
    	if (! -e ${specname}.ddf) then
    		cp ../spectra_short/${specname}.* . 
    	endif
    	if (! -e ${exam}_t1v_resampled.int2) then
			resample_image_spectra ${exam}_t1v ${specname}
		endif
		if (! -e MNI152_T1_1mm.int2) then
			cp /netopt/fsl_versions/fsl_5.0.1/data/standard/MNI152_T1_1mm.nii.gz .
			nifti_file_convert --input MNI152_T1_1mm.nii.gz --output_root MNI152_T1_1mm
		endif
    	align_tool.x -k BRAINS ${exam}_t1v_resampled MNI152_T1_1mm ${exam}_t1v_resampled_to_MNI
    	
    	cd 
    				

    	if (! -e ${exam}_to_MNI152_transform.mat) then
    		flirt -in ${root}_reorient.nii.gz -ref
			flirt -ref /netopt/fsl_versions/fsl_5.0.1/data/standard/MNI152_T1_1mm.nii.gz -in ${root}_reorient.nii.gz -omat ${exam}_to_MNI_transform.mat -out ${exam}_reorient_to_MNI
		endif
    	
	endif
	
	@ n++
	shift flist
end