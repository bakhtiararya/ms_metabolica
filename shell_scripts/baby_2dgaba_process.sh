#!/bin/csh -f

# $Header: written by Yan Li 

# process 2D GABA dataset

set datapath = /data/lhst2/neonate_gaba
set outputpath = /home/liyan/baby_2dgaba

cd $datapath
set sublist = `ls -d ./*`

set n = 1
foreach i ($sublist)
	set tempdata = $sublist[1]
	set bnum = `echo $tempdata | cut -d"/" -f2`	
	set pfile = ${bnum}bg_slice
	if (-e ${datapath}/${bnum}/${pfile}) then	
		cd ${datapath}/${bnum}
		set mrn = `rdump -p $pfile | grep -i "patient id" | cut -d":" -f2`
		set mrn = `echo $mrn | cut -d" " -f1`
		set scandate = `rdump -p $pfile | grep -i "exam date" | cut -d":" -f2`
		set scandate = `echo $scandate | cut -d" " -f1`
		if (-e spectra_lac) then
			if (-e spectra_lac/LcGrid) then
				echo "$n $bnum $pfile $mrn $scandate processed"
				#echo " white - cycle 1; red - cycle 2"				
				#svk_multi_view.dev -s spectra_lac/single_coil/${bnum}_lac_hsvdf_comb1_correct.cmplx -s spectra_lac/single_coil/${bnum}_lacf_comb2_correct.cmplx -b 424 -e 646
				# pre728 re-process for even
				# red - NAA
				if (! -e ${datapath}/${bnum}/spectra_lac/single_coil/nonedit_cycle/${bnum}_singlehsvdfcomb_emp_cor_sum.ddf) then
					cd  ${datapath}/${bnum}/spectra_lac/single_coil
					if (! -e nonedit_cycle) then
						mkdir nonedit_cycle
					endif	
					if (! -e nonedit_cycle/${bnum}_singlehsvdfcomb.ddf) then
						cp ${bnum}_lac_hsvdf_comb1_correct.ddf nonedit_cycle/${bnum}_singlehsvdfcomb.ddf
						cp ${bnum}_lac_hsvdf_comb1_correct.cmplx nonedit_cycle/${bnum}_singlehsvdfcomb.cmplx
					endif
					correct_spec_single_hsvd.x ${bnum}_singlehsvdfcomb 1.2 5 none brain_all3 0.4 nonedit_cycle
					brain_quant_single.x ${bnum}_singlehsvdfcomb brain_all3 empcs nonedit_cycle ba521_cal a 0.4
				endif
				if (! -e ${datapath}/${bnum}/spectra_lac/single_coil/nonedit_cycle/LcGrid) then
					cd ${datapath}/${bnum}/spectra_lac/single_coil/nonedit_cycle
					GridLcModelQuant.x ${bnum}_singlehsvdfcomb_emp_cor_sum
				endif
			else
				cd spectra_lac
				GridLcModelQuant.x ${bnum}_lachsvdfcomb_dif_emp_cor_sum
				echo "$n $bnum $pfile $mrn $scandate no quantification"
			endif
			if (! -e ${datapath}/${bnum}/images/${bnum}_t1v_resampled.idf) then
				cd ${datapath}/${bnum}/spectra_lac
				cp ../images/${bnum}_t1v.* .
				resample_image_spectra ${bnum}_t1v ${bnum}_lachsvdfcomb_dif_emp_cor_sum
				mv ${bnum}_t1v_resampled.* ../images
			endif
		else
			set coil = `rdump -A $pfile | grep -i "coil name" | cut -d"=" -f2 | cut -d"#" -f1`
			set c8ch = `echo $coil | grep 8`
			if (`echo ${%c8ch}` != 0) then
				proc_lac_svk.x $pfile $bnum 8 odd brain_all3 fb hsvd cal				
			else
				echo "$n $bnum $pfile $mrn what's the coil information"
			
			endif
		endif
				
	else
		echo $n $bnum
	endif
	
	
	@ n++
	shift sublist
end

# rdump -p ba520bg_slice | grep -i "patient id" | cut -d":" -f2 | cut -d" " -f2

