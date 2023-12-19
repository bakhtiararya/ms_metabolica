#!/bin/csh -f

# GABA 7T in 5 volunteers for 2015 ISMRM poster

# $Header: written by Yan Li 

if (-e /home/liyan/gaba_processing_notes.txt) then
	/bin/rm /home/liyan/gaba_processing_notes.txt
endif

if (-e /home/liyan/gaba_processing_results.txt) then
	/bin/rm /home/liyan/gaba_processing_results.txt
endif


set datapath = /data/lhst2/7T_volunteer_scans

set blist = (20150501_gaba 20150505_1_gaba 20150505_2_gaba 20150506_gaba 20150507_gaba)
set subdir = (acc aud caud)

foreach bnum ($blist)
	cd ${datapath}/$bnum
	echo "$bnum" >> /home/liyan/gaba_processing_notes.txt
	set ename = `ls -d E* | cut -d"/" -f1`	
	foreach nscan (1 2)
		cd ${datapath}/$bnum
		ls -d images*	
		echo `ls -d images*` >> /home/liyan/gaba_processing_notes.txt
		set nextscan = `arithmetic 3 - $nscan`
		set nextscan = `echo $nextscan | cut -d"." -f1`
		if (-e images_${nscan}) then			
			echo "mv images images_${nextscan}" >> /home/liyan/gaba_processing_notes.txt
			echo "mv images_${nscan} images" >> /home/liyan/gaba_processing_notes.txt
			mv images images_${nextscan}
			mv images_${nscan} images
		endif
		foreach rois ($subdir)
			set rawname = ${ename}_${rois}_${nscan}
			cd ${datapath}/${bnum}/spectra_${rois}_${nscan}
			if (-e script_all_shift.x) then
			#	/bin/rm script_all_shift.x
			endif
			if (! -e ${ename}_fft_phased_comb_gaba.dcm) then
				svk_gaba_edit_offline_recon -p ${rawname}
			endif
			if (! -e ${ename}_fft_phased_comb_gaba.dcm) then
				echo "spectra_${rois}_${nscan}/${ename}_fft_phased_comb_gaba.dcm doesn't exist"  >> /home/liyan/gaba_processing_notes.txt
			endif
			#svk_file_convert.dev -i ..dcm -t 2 -o ${ename}_fft_phased_comb_gaba
			set recenter = `grep -w "reordered center" ${ename}_fft_phased_comb_gaba.ddf`
			set recenter = `echo ${recenter} | cut -d":" -f2`
			set orcenter = `grep -w "selection center" ${ename}_fft_phased_comb_gaba.ddf`
			set orcenter = `echo ${orcenter} | cut -d":" -f2`
			echo "spectra_${rois}_${nscan}: original center -- $orcenter">> /home/liyan/gaba_processing_notes.txt
			echo "spectra_${rois}_${nscan}: reorganized center -- $recenter" >> /home/liyan/gaba_processing_notes.txt
			echo "/home/liyan/script/svs7tup/set_7t_cshift_0Hz.x ${rawname}_1 ${rawname}_1 $recenter" > script_all_shift.x
			tail -n +2 script_all.x >> script_all_shift.x
			#chmod 755 script_all_shift.x
			#script_all_shift.x
			set finalcenter = `grep -w "reordered center" ${rawname}_dif_cor_sum_comb_phased.ddf`
			set recenter = `echo ${finalcenter} | cut -d":" -f2`
			#echo "spectra_${rois}_${nscan}: final center -- $finalcenter" >> /home/liyan/gaba_processing_notes.txt
			
			mkdir temp
			cd temp
			#ln -s ../${ename}_fft_phased_comb_gaba.cmplx
			#ln -s ../${ename}_fft_phased_comb_gaba.ddf
			#ln -s ../${ename}
			#cp ../*.control .
			#MRSIQuantifyLcModel ${ename}_fft_phased_comb_gaba_inv
			#MRSIQuantifyLcModel ${rawname}_dif_cor_sum_comb_phased_inv
			echo "$bnum/spectra_${rois}_${nscan}" >> /home/liyan/gaba_processing_results.txt
			grep % LcFit*/Slice*/*_table* >> /home/liyan/gaba_processing_results.txt
			echo " " >> /home/liyan/gaba_processing_results.txt
			cp LcFit*/Slice*/*.ps /home/liyan/gaba_volt_ps/${rawname}_fft_phased_comb_gaba_inv.ps

		end
	end
	echo " " >> /home/liyan/gaba_processing_notes.txt
end

