#!/bin/csh -f

# $Header: written by Yan Li 


set dir_project = /home/liyan/projects/tinnitus
#set filesheet = 
set pathroot = /data/tinnitus/7T

set a = `date +"%y%m%d"`
set outputname = tinnitus_20$a
set check_dir = 1
set organize_dir = 0
set processing = 0
set quant = 0

if ((-e ${dir_project}/${outputname}_check.csv) && ($check_dir == 1)) then
	/bin/rm ${dir_project}/${outputname}_check.csv
endif
if ((-e ${dir_project}/${outputname}_organize.csv) && ($organize_dir == 1)) then
	/bin/rm ${dir_project}/${outputname}_organize.csv
endif
if ((-e ${dir_project}/${outputname}_process.txt) && ($processing == 1)) then
	/bin/rm ${dir_project}/${outputname}_process.txt
endif 
if ((-e ${dir_project}/${outputname}_quant.txt) && ($quant == 1)) then
	/bin/rm ${dir_project}/${outputname}_quant.txt
endif 

if ($check_dir == 1) then
	cd $pathroot
	set a = `ls -d ./20*`
	set b = `ls -d ./20* | wc -l`
	set n = 1
	while ($n <= $b) 
		set bnum = `echo $a[$n] | cut -d"/" -f2`
		set exam = `ls -d $pathroot/$bnum/E???? | cut -d"/" -f6`
		set specdir = `ls -d $pathroot/$bnum/spectra* | cut -d"/" -f6`
		set nspecdir = `ls -d $pathroot/$bnum/spectra* | wc -l`
		set string = `echo "$n,$bnum,$exam,$nspecdir"`
		if (! -e $pathroot/$bnum/rawfiles) then
			mkdir $pathroot/$bnum/rawfiles
		else
			set nfiles = `ls -l  $pathroot/$bnum/rawfiles | egrep -c '^-'`
			echo "$bnum rawfiles $nfiles files"
		endif
		set nwaterdir = `ls -d $pathroot/$bnum/unsup_* | wc -l`
		if ($nwaterdir == 1) then
			set waterdir = `ls -d $pathroot/$bnum/unsup_*`
			set waterdir = `echo $waterdir:t`
			if ($nfiles == 0) then
				echo "copy $waterdir files to rawfiles"
				cp $pathroot/$bnum/$waterdir/* $pathroot/$bnum/rawfiles
			endif
		else
			echo "$bnum unsup_h2o doesnot exist"
		endif
		set m = 1
		while ($m <= $nspecdir) 
			set subdir = `echo $specdir[$m]`
			set specdif = `ls $pathroot/$bnum/$subdir/*dif_cor_sum_comb_phased.ddf`
			set specdif = `echo $specdif:t | cut -d"." -f1`
			# dif file name = ${root}_dif_cor_sum_comb_phased
			set root = `echo $specdif | sed 's/.\{24\}$//'`
			if (-e $pathroot/$bnum/$subdir/$root) then
				set symroot = `ls -ltr $pathroot/$bnum/$subdir/$root | grep ">"`
				if (`echo ${%symroot}` != 0) then
					set rootexist = "link"
					if (-e $pathroot/$bnum/rawfiles/$root) then
						set rootexist = "link_rawfiles"
					endif
				else
					set rootexist = "file"					
					if (! -e $pathroot/$bnum/rawfiles/$root) then
						echo "$bnum $root need to copy to rawfiles"
						cp $pathroot/$bnum/$subdir/$root $pathroot/$bnum/rawfiles
						cp $pathroot/$bnum/$subdir/*.dat $pathroot/$bnum/rawfiles						
					endif
				endif
			else
				set rootexist = "no"
			endif
			set string = `echo "$string, $subdir, $root, $rootexist"`
			@ m++
		end
		echo "$string" >> ${dir_project}/${outputname}_check.csv
		if ($nspecdir > 4) then
			set nbad =  `ls -d $pathroot/$bnum/spectra*BAD | wc -l`		
	#		echo $bnum $nspecdir $nbad
		endif
		if (! -e $pathroot/$bnum/images/${exam}_t1v.idf) then
			echo $bnum NO T1 images
		endif
		@ n++
	end
endif

if ($organize_dir == 1) then
	cd $pathroot
	set a = `ls -d ./*`
	set b = `ls -d ./* | wc -l`
	set n = 1
	while ($n <= $b) 
		set bnum = `echo $a[$n] | cut -d"/" -f2`
	#	if (! -e $pathroot/$bnum/original_spectra_process) then
	#		mkdir $pathroot/$bnum/original_spectra_process
	#		mv $pathroot/$bnum/spectra* $pathroot/$bnum/original_spectra_process
	#		cp -r $pathroot/$bnum/rawfiles $pathroot/$bnum/original_spectra_process
	#	endif
		set exam = `ls -d $pathroot/$bnum/E???? | cut -d"/" -f6`
		cd $pathroot/$bnum/rawfiles
		set npfiles = `ls -S --ignore='*.*' | wc -l`
		set pfiles = `ls -S --ignore='*.*'`
		set p = 1
		set q = 1
	#	echo $bnum $npfiles
		set string = `echo "$n,$bnum,$exam,$npfiles"`
		while ($p <= $npfiles)
			set pname = `echo $pfiles[$p]`
			set psdname = `rdump -A $pname | grep -i "image.psdname" | cut -d"=" -f2 | cut -d"#" -f1`
			if ($psdname == prose7T_yan) then
				set psize = `stat -c %s $pname`
				set pdescription = `rdump -p $pname | grep "Series description" | cut -d":" -f2 | cut -d" " -f4-10`
				set pdescription = `echo $pdescription | sed -e 's/ /_/g'`
				set snum = `rdump -p $pname | grep -i "series #" | cut -d"#" -f3`
				echo "$n $bnum $npfiles $pname $snum $pdescription ($psize)"
				if ($psize > 35229056) then
					set pacq = met
					set newname = ${exam}_${pdescription}					
					set string = `echo "$string,$pname,$snum,$pdescription,$newname"`
					if (! -e ../spectra_${pdescription}) then 
						mkdir ../spectra_${pdescription}
						cp $pname ../spectra_${pdescription}/${newname}
					else
						set snum1 = `rdump -p ../spectra_${pdescription}/$newname | grep -i "series #" | cut -d"#" -f3`
						if (! -e ../spectra_${pdescription}_2) then
							if ($snum1 < $snum) then
								mkdir ../spectra_${pdescription}_2
								cp $pname ../spectra_${pdescription}_2/${newname}_2
								echo "spectra_${pdescription} series $snum1 vs. spectra_${pdescription}_2 series $snum"
							else
								if ($snum1 > $snum) then
									mv ../spectra_${pdescription} ../spectra_${pdescription}_2
									mv ../spectra_${pdescription}_2/$newname ../spectra_${pdescription}_2/${newname}_2
									mkdir ../spectra_${pdescription}
									cp $pname ../spectra_${pdescription}/${newname}
									set snum1 = `rdump -p ../spectra_${pdescription}/$newname | grep -i "series #" | cut -d"#" -f3`
									set snum2 = `rdump -p ../spectra_${pdescription}_2/${newname}_2 | grep -i "series #" | cut -d"#" -f3`
									echo "spectra_${pdescription} series $snum1 vs. spectra_${pdescription}_2 series $snum2"
								endif
							endif 
						else
							echo "Error $bnum $pname $pdescription > 2 files"
						endif
					endif
				else
					set pacq = water
					set newname = ${exam}_${pdescription}_water
					set snumb =
					if (-e ../spectra_${pdescription}) then
						set sumb = `rdump -p ../spectra_${pdescription}/${exam}_${pdescription} | grep -i "series #" | cut -d"#" -f3`
						if ($sumb == $snum) then
							cp $pname ../spectra_${pdescription}/${newname}
						else
							if (! -e ../spectra_${pdescription}_2) then
								echo "$bnum $pname $snum ($snumb $snumb) spectra_${pdescription}_2 does not exist"
							else
								set sumb = `rdump -p ../spectra_${pdescription}_2/${exam}_${pdescription}_2 | grep -i "series #" | cut -d"#" -f3`
								if ($sumb == $snum) then
									cp $pname ../spectra_${pdescription}_2/${exam}_${pdescription}_2_water
								else
									echo "Error $bnum $pname water $pdescription > 2 files"
								endif
							endif
						endif
					else
						echo "$bnum $pname ($snum $snumb) spectra_${pdescription} does not exist"
					endif
										
				endif
			#	set string = `echo "$string,$pname,$psize,$pacq,$pdescription"`
				@ q++
			endif
			@ p++
		end
		set string = `echo "$string, $p, $q"`
		echo "$string" >> ${dir_project}/${outputname}_organize.csv
		@ n++
	end
endif


if ($processing == 1) then
	cd $pathroot
	set a = `ls -d ./*`
	set b = `ls -d ./* | wc -l`
	set n = 1
	while ($n <= $b) 
		set bnum = `echo $a[$n] | cut -d"/" -f2`
		set exam = `ls -d $pathroot/$bnum/E???? | cut -d"/" -f6`
		set specdir = `ls -d $pathroot/$bnum/spectra* | cut -d"/" -f6`
		set nspecdir = `ls -d $pathroot/$bnum/spectra* | wc -l`
		set m = 1
		while ($m <= $nspecdir) 
			set subdir = `echo $specdir[$m]`
			set nfiles = `ls -l  $pathroot/$bnum/$subdir | egrep -c '^-'`
			if ($nfiles != 2) then
				echo "$n $bnum $subdir $nfiles files"
			endif
			cd $pathroot/$bnum/$subdir
			set root = `ls -S`
			set root = `echo $root[1]`
			if (! -e $root) then
				echo "Error $bnum $subdir $root"
			endif
			if (! -e ${root}_water) then
				echo "Error $bnum $subdir no ${root}_water"
			endif
			process_gaba.x ${root} --i ${exam}  --l 0
			@ m++
		end	
		@ n++
	end
endif

if ($quant == 1) then
	cd $pathroot
	set a = `ls -d ./*`
	set b = `ls -d ./* | wc -l`
	set n = 1
	while ($n <= $b) 
		set bnum = `echo $a[$n] | cut -d"/" -f2`
		set exam = `ls -d $pathroot/$bnum/E???? | cut -d"/" -f6`
		set specdir = `ls -d $pathroot/$bnum/spectra* | cut -d"/" -f6`
		set nspecdir = `ls -d $pathroot/$bnum/spectra* | wc -l`
		set m = 1
		while ($m <= $nspecdir) 
			set subdir = `echo $specdir[$m]`
			cd $pathroot/$bnum/$subdir
			set root = `echo $subdir | cut -d"/" -f1 | cut -d"_" -f2-10`
			set root = ${exam}_${root}
			if (! -e ${root}) then
				echo "${bnum}/${subdir} $root does not exist" 			
			endif
			if ((! -e  ${root}_cor_sum_naa.ddf) | (! -e ${root}_cor_sum_dif_gaba_water.ddf)) then
				echo "$bnum $root haven't processed yet"
				process_gaba.x ${root} --i ${exam}  --l 0
			endif
		# get voxel segmentation information
		#	cp ${ename}_${rois}_exam${nscan}_t1vseg_wconc.txt ${rawname}_cor_sum_naa_seg_wconc.txt
		#	cp ${ename}_${rois}_exam${nscan}_t1vseg_wconc.txt ${rawname}_cor_sum_dif_gaba_seg_wconc.txt
		#	process_gaba.x ${root} --i ${exam} --p 0
			@ m++
		end	
		@ n++
	end			
endif


