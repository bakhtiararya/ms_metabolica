#!/bin/csh -f

# $Header: written by Yan Li 

set blist = (20150409 20150427 20150918 20151020 20151021)
set elist = (E2797 E2864 E3197 E3229 E3232)
set rlist = hippo

set blist = (20150330_epilepsy 20150406_epilepsy 20150408_epilepsy 20150521_epilepsy 20150609_epilepsy 20150625_epilepsy)
set elist = (E2771 E2785 E2789 E2924 E2965 E3005)

foreach bnum ($blist)
	if (-e /data/lhst2/7T_epilepsy/$bnum) then
		set datapath = /data/lhst2/7T_epilepsy/$bnum
	else
		if (-e /data/lhst2/7T_volunteer_scans/$bnum) then
			set datapath = /data/lhst2/7T_volunteer_scans/$bnum
		else
			echo "$bnum does not exist"
		endif
	endif
	foreach exam ($elist)
		if (-e $datapath/$exam) then
			set proot = $exam
			cd $datapath
			if (-e spectra_hippo_2d) then
				cd $datapath/spectra_hippo_2d
				if ((-e LcGrid_GABA) && (-e LcGrid_Editoff)) then
					echo $datapath
					set ndiffile = `ls *dif_cor_sum_comb_phased.ddf | wc -l`
					if ($ndiffile == 1) then
						set diffile = `ls *dif_cor_sum_comb_phased.ddf`
					else 
						echo "No dif file"
						exit
					endif
					if (! -e ${proot}_t1v_resampled.idf) then
						if (! -e ${proot}_t1v.idf) then
							if (-e ../images/${proot}_t1v.idf) then
								ln -s ../images/${proot}_t1v.idf
								ln -s ../images/${proot}_t1v.int2
							endif
						endif
						set refspec = `echo $diffile | cut -d"." -f1`
						resample_image_spectra ${proot}_t1v ${refspec}
					endif
					set noneditspec = `ls LcGrid_Editoff/*cor_sum_comb_cor_sum_LCM_cor.ddf`
					set difspecname = `ls LcGrid_GABA/*phased_LCM_cor.ddf`
					set gabamap = `ls LcGrid_GABA/LCM_Met/*phased_LCM_GABANAA.idf`
					set naamap = `ls LcGrid_Editoff/LCM_Met/*cor_sum_comb_cor_sum_LCM_NAA+NAAGCr+PCr.idf `
					echo "svk_multi_view.dev ${proot}_t1v_resampled.idf ${proot}_t1v_resampled.idf -s $difspecname  -b 2200 -e 3000 -l -5e7 -u 3e7 -o $gabamap -o $naamap"
				endif
			endif
		endif
	end
end