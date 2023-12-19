#!/bin/csh -f

# $Header: written by Yan Li 

set projectpath = /home/liyan/projects/c13_h1_epsi
set processdate = `date +"%y%m%d"`
set outputroot = c13h1_epi_datastatus_20${processdate}

if (-e ${projectpath}/${outputroot}.csv) then
	/bin/rm ${projectpath}/${outputroot}.csv
endif
echo "No, bnum, H-tnum, C-tnum, Vcel, Vt2all, C13 res" > ${projectpath}/${outputroot}.csv

set blist = (b4327 b2284 b4332 b4035 b4339 b4222)
set htlist = (t11598 t11600 t11618 t11731 t11814 t11815)
set ctlist = (t11597 t11599 t11620 t11730 t11812 t11813)
# b4035: t11812, t11814 most recent 32 channel data
# b4222: t11813, t11815 most recent 32 channel data
#b4035/t11669, t11668 50Hz shift
#b4161/t11765, t11764 position error
set blist = (b4222)
set htlist = (t11980)
set ctlist = (t11975)

set blist = (b4161)
set htlist = (t11996)
set ctlist = (t11995)



set pathroot = /data/bioe3/C13_BrainPatient
set n = 1
foreach bnum ($blist)
	set outputstring = $n
	foreach tnum ($htlist)
		if (-e ${pathroot}/${bnum}/${tnum}) then
			set htnum = $tnum
			break
		endif	
	end
	foreach tnum ($ctlist)
		if (-e ${pathroot}/${bnum}/${tnum}) then
			set ctnum = $tnum
			break
		endif
	end
	echo $n $bnum $htnum $ctnum
	set outputstring = `echo $outputstring, $bnum, $htnum, $ctnum`
	if (! -e ${pathroot}/${bnum}/${htnum}_to_${ctnum}) then
		mkdir ${pathroot}/${bnum}/${htnum}_to_${ctnum}
	endif

	# check H-1 MRSI
	if (! -e ${pathroot}/${bnum}/${htnum}/spectra_lac) then
		echo "   no spectra_lac"
	else 
		if (! -e ${pathroot}/${bnum}/${htnum}_to_${ctnum}/brain_analysis_${htnum}_lac_fbhsvdfcomb) then
			echo " copying brain_analysis_${htnum}_lac_fbhsvdfcomb "
			cp -r ${pathroot}/${bnum}/${htnum}/brain_analysis_${htnum}_lac_fbhsvdfcomb ${pathroot}/${bnum}/${htnum}_to_${ctnum}
		endif
		if (! -e  ${pathroot}/${bnum}/${htnum}_to_${ctnum}/${htnum}_lac_fbhsvdcomb_sum_empcs_cor.ddf) then
			cp ${pathroot}/${bnum}/${htnum}/spectra_lac/${htnum}_lac_fbhsvdfcomb_sum_empcs_cor.* ${pathroot}/${bnum}/${htnum}_to_${ctnum}
			cp ${pathroot}/${bnum}/${htnum}/spectra_lac/${htnum}_lac_fbhsvdfcomb_dif_empcs_cor.* ${pathroot}/${bnum}/${htnum}_to_${ctnum}
		endif
	endif

	# check ROIs
	if (! -e ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois) then
		mkdir ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois
	endif
	if (! -e ${pathroot}/${bnum}/${htnum}/rois) then
		mkdir ${pathroot}/${bnum}/${htnum}/rois
	endif	
	if (! -e ${pathroot}/${bnum}/${htnum}/rois/${htnum}_wm.byt) then
		echo "  no WM ROI"
		echo "  segmenting WM"
		cd ${pathroot}/${bnum}/${htnum}/
		segment_wm.x ${htnum} t1va
		cp ${pathroot}/${bnum}/${htnum}/rois/${htnum}_wm.* ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois
		cp ${pathroot}/${bnum}/${htnum}/images/${htnum}_gm.* ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois
		cp ${pathroot}/${bnum}/${htnum}/images/${htnum}_csf.* ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois
	endif
	if (! -e ${pathroot}/${bnum}/${htnum}/rois/${htnum}_t2all.byt) then
		echo "   no t2ll ROI"
	endif
	if (! -e ${pathroot}/${bnum}/${htnum}/rois/${htnum}_cel.byt) then
		echo "   no cel ROI"
	endif
	if (! -e ${pathroot}/${bnum}/${htnum}/rois/${htnum}_brainmask.byt) then
		if (-e ${pathroot}/${bnum}/${htnum}/images/${htnum}_brainmask.byt) then
			cp ${pathroot}/${bnum}/${htnum}/images/${htnum}_brainmask.* ${pathroot}/${bnum}/${htnum}/rois/
		else
			echo "  Can not find brainmask"
		endif
	endif
	cp ${pathroot}/${bnum}/${htnum}/rois/* ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois
	if (! -e ${pathroot}/${bnum}/${htnum}_to_${ctnum}/${htnum}_gm.byt) then
		cp ${pathroot}/${bnum}/${htnum}/images/${htnum}_t1va_gm.byt ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois/${htnum}_gm.byt
		cp ${pathroot}/${bnum}/${htnum}/images/${htnum}_t1va_gm.idf ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois/${htnum}_gm.idf
		cp ${pathroot}/${bnum}/${htnum}/images/${htnum}_t1va_csf.byt ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois/${htnum}_csf.byt
		cp ${pathroot}/${bnum}/${htnum}/images/${htnum}_t1va_csf.idf ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois/${htnum}_csf.idf
		cd ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois/
		fix_rootname.x ${htnum}_csf
		fix_rootname.x ${htnum}_gm
	endif

	# check C-13 EPI data
	if (! -e ${pathroot}/${bnum}/${htnum}_to_${ctnum}/epi) then
		mkdir ${pathroot}/${bnum}/${htnum}_to_${ctnum}/epi
	endif
	if (! -e ${pathroot}/${bnum}/${ctnum}/epi/dynamics_lactate) then
		echo "   no dynamics lactate"
		set a = `ls ${pathroot}/${bnum}/${ctnum}/epi/`
	#	echo "  epi: $a"
	else
		cp -r ${pathroot}/${bnum}/${ctnum}/epi/dynamics_* ${pathroot}/${bnum}/${htnum}_to_${ctnum}/epi
	endif
	if (! -e ${pathroot}/${bnum}/${ctnum}/epi/_results/AUC_ratio_lp) then
		echo "  no AUC ratio lp"
		set a = `ls ${pathroot}/${bnum}/${ctnum}/epi/_results`
	#	echo "  epi/_results: $a"
	else
		cp -r ${pathroot}/${bnum}/${ctnum}/epi/_results/AUC_ratio* ${pathroot}/${bnum}/${htnum}_to_${ctnum}/epi
	endif
	cp ${pathroot}/${bnum}/${ctnum}/epi/*.mat ${pathroot}/${bnum}/${htnum}_to_${ctnum}/epi
	cp ${pathroot}/${bnum}/${ctnum}/epi/${ctnum}.7 ${pathroot}/${bnum}/${htnum}_to_${ctnum}/epi
	cd ${pathroot}/${bnum}/${htnum}_to_${ctnum}/epi
	if (! -e ${ctnum}_epi_ratio_lp.idf) then
		if (-e AUC_ratio_lp) then
			svk_file_convert -i AUC_ratio_lp/Image_001.dcm -t 3 -o ${ctnum}_epi_ratio_lp
		else
			echo " where AUC_ratio_lp"
		endif
	endif
	if (! -e ${ctnum}_epi_ratio_bp.idf) then
		if (-e AUC_ratio_bp) then
			svk_file_convert -i AUC_ratio_bp/Image_001.dcm -t 3 -o ${ctnum}_epi_ratio_bp
		else
			echo "   where is AUC_ratio_bp"
		endif
	endif
	
	# set up alignment
	cd ${pathroot}/${bnum}/${htnum}_to_${ctnum}
	if (! -e brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi) then
		mkdir brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi
	endif
	if (! -e brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}) then
		mkdir brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}
	endif
	cd ${pathroot}/${bnum}/${htnum}_to_${ctnum}
	if (! -e ${htnum}_fla.int2) then
		cp ../${htnum}/images/${htnum}_fla.* .
	endif
	if (! -e ${htnum}_fla_resampled.int2) then
		resample_image_spectra ${htnum}_fla ${htnum}_lac_fbhsvdfcomb_sum_empcs_cor
	endif
	if (! -e ${ctnum}_fse.idf) then
#		if (-e ${ctnum}_epi_ratio_lp.idf) then
#			modify_idf_center.sh ${ctnum}_fse ${ctnum}_epi_ratio_lp ${ctnum}_fse_to_epi ${ctnum}_fse_resampled
#		endif
		if (! -e ../${ctnum}/images/${ctnum}_fse.idf) then
			echo " no ${ctnum} fse"
			exit 1
		else
			cp ../${ctnum}/images/${ctnum}_fse.* .
		endif
	endif
	if (! -e ${htnum}_fla_resampled_to_${ctnum}_fse_transform.tfm) then
		align_tool.dev -k BRAINS ${htnum}_fla_resampled ${ctnum}_fse ${htnum}_fla_resampled_to_${ctnum}_fse
		#align_tool.dev -k BRAINS ${htnum}_fla_resampled ${ctnum}_fse ${htnum}_fla_resampled_to_${ctnum}_fse -f "--transformType Rigid --initializeTransformMode useCenterOfHeadAlign --maskProcessingMode ROIAUTO  --ROIAutoDilateSize 3  --interpolationMode Linear"		
	else 
#		svk_multi_view ${htnum}_fla_resampled_to_${ctnum}_fse.idf  ${ctnum}_fse.idf
	endif
	if (-e epi/${ctnum}_epi_ratio_lp.idf) then 
		if (! -e sample_c13_met.idf) then
			cp	epi/${ctnum}_epi_ratio_lp.idf sample_c13_epi.idf
			modify_idf_4_13C.x sample_c13_epi sample_c13_met
			cp brain_analysis_${htnum}_lac_fbhsvdfcomb/${htnum}_lac_fbhsvdfcomb_empcsahl_res_cho_naa.real sample_c13_met.real
			fix_rootname.x sample_c13_met
			modify_idf_filetype.x sample_c13_met.idf 7
			modify_idf_filetype.x sample_c13_epi.idf 7
		endif
	endif 
	
	# rois
	cd ${pathroot}/${bnum}/${htnum}_to_${ctnum}/rois
	if (! -e ${htnum}_nawm.idf) then
		if (-e ${htnum}_cel.idf) then
			mask_math ${htnum}_wm -not ${htnum}_t2all -not  ${htnum}_cel ${htnum}_nawm
		else
			mask_math ${htnum}_wm -not ${htnum}_t2all ${htnum}_nawm
		endif
	endif
	
	foreach rtype (cel t2all nawm wm brainmask gm csf)
		if (-e ${htnum}_${rtype}.byt) then
			echo "   align $rtype"
			if (! -e ${htnum}_fla.int2) then 
				cp ../${htnum}_fla.* .
			endif
			if (! -e ${ctnum}_fse.int2) then
				cp ../${ctnum}_fse.* .
			endif
			if (! -e ${htnum}_fla_to_${ctnum}_fse_transform.tfm) then
				align_tool.dev -k BRAINS ${htnum}_fla ${ctnum}_fse ${htnum}_fla_to_${ctnum}_fse
			endif
			if (! -e ${htnum}_${rtype}_to_${ctnum}_fse.idf) then
				align_tool.dev -k BRAINS ${htnum}_${rtype} ${ctnum}_fse ${htnum}_${rtype}_to_${ctnum}_fse -t ${htnum}_fla_to_${ctnum}_fse_transform.tfm 
			else
		#		svk_multi_view ${htnum}_fla_to_${ctnum}_fse.idf ${ctnum}_fse.idf ${htnum}_${rtype}_to_${ctnum}_fse.idf 
			endif
			if ((! -e ${ctnum}_epi_ratio_lp.idf) & (-e ../epi/${ctnum}_epi_ratio_lp.idf)) then
				cp ../epi/${ctnum}_epi_ratio_lp.idf .
			endif
			if (! -e ${htnum}_${rtype}_to_${ctnum}_fse_epi_percent.idf) then
				if (-e ${ctnum}_epi_ratio_lp.idf ) then
					percent_image.x ${htnum}_${rtype}_to_${ctnum}_fse.int2 ${ctnum}_epi_ratio_lp.idf ${htnum}_${rtype}_to_${ctnum}_fse_epi_percent
				else
					echo "  No C13 EPI information for ROI alignment" 
				endif
			endif		
		endif
	end
	if (-e ${htnum}_cel.byt) then
		if (! -e ${htnum}_fla_${htnum}_cel_params.txt) then
			get_mask_values ${htnum}_cel ${htnum}_fla
		endif
		set tempv = `grep "mask volume" ${htnum}_fla_${htnum}_cel_params.txt`
		set vol = `echo $tempv | cut -d" " -f3`
		set outputstring = `echo $outputstring,$vol`
	else
		set outputstring = `echo $outputstring,`
	endif
	if (! -e ${htnum}_fla_${htnum}_t2all_params.txt) then
		get_mask_values ${htnum}_t2all ${htnum}_fla
	endif
	set tempv = `grep "mask volume" ${htnum}_fla_${htnum}_t2all_params.txt`
	set vol = `echo $tempv | cut -d" " -f3`
	set pixelsize = `grep "pixelsize(mm)" ../epi/${ctnum}_epi_ratio_lp.idf | cut -d":" -f5`
	set outputstring = `echo $outputstring,$vol,$pixelsize`
	echo $outputstring >> ${projectpath}/${outputroot}.csv

	#align brain met to C13 
	if (! -e ${pathroot}/${bnum}/${htnum}_to_${ctnum}/brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi) then
		/bin/rm ${pathroot}/${bnum}/${htnum}_to_${ctnum}/brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi
	endif
	cd ${pathroot}/${bnum}/${htnum}_to_${ctnum}/brain_analysis_${htnum}_lac_fbhsvdfcomb
	if (! -e ${htnum}_fla_resampled_to_${ctnum}_fse_transform.tfm) then
		cp ../${htnum}_fla_resampled_to_${ctnum}_fse_transform.tfm .
	endif
	if ((-e sample_c13_met.idf) | (-e ../sample_c13_met.idf)) then
		cp ../sample_c13_met.* .
		cp ../sample_c13_epi.idf .
		echo "  aligning metabolite files"
		set flist = `ls ${htnum}*.real`
		set rf = 1
		foreach i ($flist)
			set tempf = $flist[1]
			set fname = `echo $tempf | cut -d"." -f1` 						
			if ((! -e ${fname}_to_${ctnum}.real) & (! -e ../brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}/${fname}_to_${ctnum}.real))  then
				echo $rf $fname
				align_tool.dev -k BRAINS ${fname} sample_c13_met ${fname}_to_${ctnum} -t ${htnum}_fla_resampled_to_${ctnum}_fse_transform.tfm	
				mv  -f ${fname}_to_${ctnum}.* ../brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}			
			endif
			if ((! -e ${fname}_to_${ctnum}_epi.real) & (! -e ../brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi/${fname}_to_${ctnum}_epi.real)) then
				if (! -e ${fname}_to_${ctnum}.real) then
					cd ../brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}
					cp ../sample_c13_epi.idf .
					resample_image_v5_mine.x ${fname}_to_${ctnum} real sample_c13_epi ${fname}_to_${ctnum}_epi
					mv -f ${fname}_to_${ctnum}_epi.* ../brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi				
					cd ../brain_analysis_${htnum}_lac_fbhsvdfcomb
				else
					resample_image_v5_mine.x ${fname}_to_${ctnum} real sample_c13_epi ${fname}_to_${ctnum}_epi
					mv -f ${fname}_to_${ctnum}_epi.* ../brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi			
				endif
			endif
			@ rf++
			shift flist
		end
	#	mv *_to_${ctnum}.* ../brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}	
	#	mv *_to_${ctnum}_epi.* ../brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi				
	endif
	cd ${pathroot}/${bnum}/${htnum}_to_${ctnum}
	set cnifile = ${htnum}_lac_fbhsvdfcomb_empcsahl_res_cho_naa
#	svk_multi_view rois/${htnum}_fla_to_${ctnum}_fse.idf rois/${ctnum}_fse.idf rois/${htnum}_t2all_to_${ctnum}_fse.idf 
#	svk_multi_view  brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}/${cnifile}_to_${ctnum}.real 
#	if (-e epi/${ctnum}_epi_ratio_lp.idf) then
#		svk_multi_view epi/${ctnum}_epi_ratio_lp.idf brain_analysis_${htnum}_lac_fbhsvdfcomb_to_${ctnum}_epi/${cnifile}_to_${ctnum}_epi.real rois/${htnum}_t2all_to_${ctnum}_fse_epi_percent.idf
#	endif
	@ n++
end
