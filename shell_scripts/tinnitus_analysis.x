#!/bin/csh -f

# $Header: written by Yan Li 

# processing data on 2017/01

set dir_project = /home/liyan/projects/tinnitus
#set filesheet = 
set pathroot = /data/tinnitus/7T

set a = `date +"%y%m%d"`
set outputname = tinnitus_20$a
set check_data = 1
set get_value = 0
set dateext = $a

if ((-e ${dir_project}/${outputname}_check_image.csv) && ($check_data == 1)) then
	/bin/rm ${dir_project}/${outputname}_check_image.csv
endif
if ((-e ${dir_project}/${outputname}_check_spectra.csv) && ($check_data == 1)) then
	/bin/rm ${dir_project}/${outputname}_check_spectra.csv
endif
if ($check_data == 1) then
	foreach quanttype (GABA GABA_WaterRef Edit_OFF Edit_OFF_WaterRef)
		if (-e ${dir_project}/LcGrid_${quanttype}_quant_20$a.csv) then
			/bin/rm ${dir_project}/LcGrid_${quanttype}_quant_20$a.csv
		endif
	end
endif

if ($check_data == 1) then
	cd $pathroot
	set a = `ls -d ./20*`
	set b = `ls -d ./20* | wc -l`
	set n = 1
	while ($n <= $b) 
		# achieve date of scan (bnum), exam number (exam)
		set bnum = `echo $a[$n] | cut -d"/" -f2`
		set exam = `ls -d $pathroot/$bnum/E???? | cut -d"/" -f6`
		set specdir = `ls -d $pathroot/$bnum/spectra* | cut -d"/" -f6`
		set nspecdir = `ls -d $pathroot/$bnum/spectra* | wc -l`
		# achieve MRN number
		if (! -e $pathroot/$bnum/rawfiles) then
			echo "$n,$bnum,$exam,no rawfiles directory"
		endif
		set pfile = `ls -S $pathroot/$bnum/rawfiles/ --ignore='*.*'`
		set pfile1 = `echo $pfile[1]`
		set mrnnumber = `rdump -p $pathroot/$bnum/rawfiles/${pfile1} | grep "Patient ID"`
		set mrnnumber = `echo $mrnnumber | cut -d":" -f2`
		set mrnnumber = `echo $mrnnumber | cut -d" " -f1`
		set string1 = `echo "$n,$bnum,$mrnnumber,$exam,${nspecdir}SpecDir"`
		# check T1-weighted images
		if (! -e $pathroot/$bnum/images/${exam}_t1v.idf) then
			echo "${string1}, No T1"
		endif
		# check tissue segementation
		if (-e /data/tinnitus/7T_processed/${bnum}) then
			if (-e /data/tinnitus/7T_processed/${bnum}/t1_7T) then
				set ngm = `ls /data/tinnitus/7T_processed/${bnum}/t1_7T/c1* | wc -l`
				set nwm = `ls /data/tinnitus/7T_processed/${bnum}/t1_7T/c2* | wc -l`
				set ncsf = `ls /data/tinnitus/7T_processed/${bnum}/t1_7T/c3* | wc -l`
				if ($ngm == 1) then
					set gm = `ls /data/tinnitus/7T_processed/${bnum}/t1_7T/c1*`
					set gm = `echo $gm | cut -d"/" -f7`
					set string1 = `echo "${string1}, $gm"`
				else
					set string1 = `echo "${string1}, no gm"`
				endif
				if ($nwm == 1) then
					set wm = `ls /data/tinnitus/7T_processed/${bnum}/t1_7T/c2*`
					set wm = `echo $wm | cut -d"/" -f7`
					set string1 = `echo "${string1}, $wm"`
				else
					set string1 = `echo "${string1}, no wm"`
				endif
				if ($ncsf == 1) then
					set csf = `ls /data/tinnitus/7T_processed/${bnum}/t1_7T/c3*`
					set csf = `echo $csf | cut -d"/" -f7`
					set string1 = `echo "${string1}, $csf"`
				else
					set string1 = `echo "${string1}, no csf"`
				endif
			else
				set string1 = `echo "$string1, no t1 7t dir,,,"`
			endif
		else
			set string1 = `echo "$string1, no segmention,,,"`		
		endif	
		echo "$string1" >> ${dir_project}/${outputname}_check_image.csv		
		# check each spectral directory		
		set m = 1
		while ($m <= $nspecdir) 
			# check whether thep processing were completed   
			set string2 = `echo "$n,$bnum,$exam,${nspecdir}"`				
			set subdir = `echo $specdir[$m]`
			foreach quanttype (GABA GABA_WaterRef Edit_OFF Edit_OFF_WaterRef)
				if (-e $pathroot/$bnum/$subdir/LcGrid_${quanttype}) then
					set string2 = `echo "$string2, $m, $subdir, LC ${quanttype} processed"`
					set nps = `ls $pathroot/$bnum/$subdir/LcGrid_${quanttype}/*.ps | wc -l`
					set ncsv = `ls $pathroot/$bnum/$subdir/LcGrid_${quanttype}/*.csv | wc -l`
					if (($nps == 1) & ($ncsv == 1)) then
						cp $pathroot/$bnum/$subdir/LcGrid_${quanttype}/*.ps  ${dir_project}/PS_${quanttype}
						if (($n == 1) & ($m == 1)) then
							set header = `head -1 $pathroot/$bnum/$subdir/LcGrid_${quanttype}/*.csv`
							echo "subject, exam,location, $header" > ${dir_project}/LcGrid_${quanttype}_quant_20${dateext}.csv	
						endif
						set tempvalue = `awk 'FNR > 1' $pathroot/$bnum/$subdir/LcGrid_${quanttype}/*.csv`
						echo "$bnum,${exam},$subdir,$tempvalue" >> ${dir_project}/LcGrid_${quanttype}_quant_20${dateext}.csv	
					else
						echo "$bnum $subdir LcGrid_${quanttype} $nps $ncsv"
					endif
				else
					set string2 = `echo "$string2, $m, $subdir, LC ${quanttype} not processed"`
				endif
			end
			
			# check voxel for each acquisition
			set nddf = `ls $pathroot/$bnum/$subdir/*.ddf | wc -l`
			if ($nddf > 0 ) then
				cd $pathroot/$bnum/$subdir/LcGrid_GABA
				set specroot = `ls *dif_gaba.ddf`
				set specroot = `echo $specroot | cut -d"." -f1`
				set sloc = `echo $subdir | cut -d"_" -f2-5`
				set outputroot = ${exam}_${sloc}
			#	/home/liyan/script/serial_spectra/press_2d_profile.x ${specroot} ${outputroot} 

				set boxsize = `grep "selection size" ${specroot}.ddf`
				set boxx = `echo $boxsize | awk '{print $3}' | cut -d"." -f1`
				set boxy = `echo $boxsize | awk '{print $4}' | cut -d"." -f1`
				set boxz = `echo $boxsize | awk '{print $5}' | cut -d"." -f1`
				set string2 = `echo $string2, $boxx, $boxy, $boxz`
				
				# generate PRESS images
			#	ln -s $pathroot/$bnum/images/${exam}_t1v.int2
			#	ln -s $pathroot/$bnum/images/${exam}_t1v.idf
			#	/home/liyan/script/cshellscript/resample_image_v5_mine.x ${outputroot}_press int2 ${exam}_t1v ${outputroot}_pressr	
			#	nifti_file_convert --input ${outputroot}_pressr.int2 --output_root ${outputroot}_pressr
			#	fslreorient2std ${outputroot}_pressr.nii.gz ${outputroot}_pressr_reorient
			#	nifti_file_convert --input ${exam}_t1v.int2 --output_root ${exam}_t1v
			#	fslreorient2std ${exam}_t1v.nii.gz ${exam}_t1v_reorient
			#	cp ${outputroot}_pressr_reorient.nii.gz /data/tinnitus/7T/MRS_Box_Location		
			#	mv ${exam}_t1v_reorient.nii.gz	/data/tinnitus/7T/MRS_Box_Location/T1_Images	
			#	/bin/rm ${exam}_t1v.nii.gz	
			else
				set string2 = `echo $string2, no ddf`
				set nfiles = `ls  $pathroot/$bnum/$subdir | wc -l`
				if ($nfiles == 2) then
					set pname = `ls -S --ignore="_water" $pathroot/$bnum/$subdir`
					cd $pathroot/$bnum/$subdir
					echo " $subdir process_gaba.x $pname"
				#	process_gaba.x $pname --i ${exam} 
				else
					echo "$pathroot/$bnum/$subdir $nfiles"
				endif 
			endif
			# clear up previous box/sats images
			#set nvssf = `ls $pathroot/$bnum/$subdir/*_vss.* | wc -l`
			#set nboxf = `ls $pathroot/$bnum/$subdir/*_box.* | wc -l`
			#if ($nvssf > 0) then
			#	echo "$bnum, $subdir, $nvssf VSS, $nboxf Box"
			#	/bin/rm $pathroot/$bnum/$subdir/*_vss.* 
			#	/bin/rm $pathroot/$bnum/$subdir/*_box.*
			#endif
			# Generate Box masks
			#		/home/liyan/script/serial_spectra/press_2d_profile.x ${ename}_${rois}_${nscan}_dif_cor_sum_comb_phased ${ename}_${rois}_${nscan} 
			#		resample_image ${ename}_${rois}_${nscan}_press.int2 ${ename}_t1v_exam${nscan}.int2
			#		nifti_file_convert --input ${ename}_${rois}_${nscan}_pressr.int2 --output_root ${ename}_${rois}_${nscan}_pressr

			
			echo "$string2" >> ${dir_project}/${outputname}_check_spectra.csv	
			@ m++
		end		
		@ n++
	end
endif




#	Get the image of PRESS Box
#				/home/liyan/script/serial_spectra/press_2d_profile.x ${ename}_${rois}_${stime}_dif_cor_sum_comb_phased ${ename}_${rois}_${stime} 
#				resample_image ${ename}_${rois}_${stime}_press.int2 ${ename}_t1v_exam${stime}.int2
#				nifti_file_convert --input ${ename}_${rois}_${stime}_pressr.int2 --output_root ${ename}_${rois}_${stime}_pressr
#				fslreorient2std ${ename}_${rois}_${stime}_pressr.nii.gz ${ename}_${rois}_${stime}_pressr_reorient
