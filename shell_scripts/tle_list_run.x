#!/bin/csh -f

# $Header: written by Yan Li 


#set blist = (20150409 20150427 20150918 20151020 20151021)
#set elist = (E2797 E2864 E3197 E3229 E3232)
#set rlist = (acc ROF LOF)

#set blist = (20150330_epilepsy 20150406_epilepsy 20150408_epilepsy 20150521_epilepsy 20150609_epilepsy 20150625_epilepsy)
#set elist = (E2771 E2785 E2789 E2924 E2965 E3005)

set blist = (20150409 20150427 20150918 20151020 20151021 20150330_epilepsy 20150406_epilepsy 20150408_epilepsy 20150521_epilepsy 20150609_epilepsy 20150625_epilepsy)
set elist = (E2797 E2864 E3197 E3229 E3232 E2771 E2785 E2789 E2924 E2965 E3005)
set rlist = (acc ROF LOF)


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
		endif
	end
	foreach roi ($rlist)
		cd $datapath
		if (-e spectra_$roi) then
			set rootname = ${proot}_${roi}
			cd $datapath/spectra_$roi
			#echo " $bnum $proot $roi ..."
			if (! -e $rootname) then
				echo "$bnum $exam spectra_${roi} No $rootname"
			else
				gaba_epilepsy_process.x $rootname
			endif
			#if (! -e ${proot}_t1v_resampled.idf) then
			#	if (! -e ${proot}_t1v.idf) then
			#		if (-e ../images/${proot}_t1v.idf) then
			#			ln -s ../images/${proot}_t1v.idf
			#			ln -s ../images/${proot}_t1v.int2
			#			resample_image_spectra ${proot}_t1v ${rootname}_cyc2_cor_sum_comb_cor_sum
			#		endif
			#	endif
			#endif
			#if (-e ${proot}_t1v_resampled.idf) then  
    		#	echo "  viewing cycle 1..."
			#	svk_multi_view.dev ${proot}_t1v_resampled.idf -s ${rootname}_cyc1_cor_sum_comb_cor_sum.cmplx  -b 1100 -e 1500 -l -5e8 -u 3e8	
			#else
			#	echo "   No image files"
			#	sleep 5
			#	exit	
			#endif
			#echo "   Please enter the cycle of Editing OFF"
			#set ncyc = $<
			#if ($ncyc == 1) then
			#	process_mrsi_7t.x $rootname --i $exam --g 1		
			#endif
		else
			echo "$bnum $exam No $roi"
		endif
	end
end
		