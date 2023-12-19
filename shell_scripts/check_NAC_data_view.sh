#!/bin/csh -f

# $Header: written by Yan Li 

# process high resolution sLASER EPSI/flyback

set datapath = /data/lhst2/7T_NAC_MS_GSH
cd $datapath
set t2list = `ls su*/*/images/*cube_fl.idf`
set nt2list =  `ls su*/*/images/*cube_fl.idf | wc -l`

set n = 1
set viewflag = 1
set processflag = 0

foreach i ($t2list)
	set tempdata = $t2list[1]
	set bnum = `echo $tempdata | cut -d"/" -f1`
	set tnum = `echo $tempdata | cut -d"/" -f2`
	cd $datapath/$bnum/$tnum
	set exam = `ls -d E*`
	set exam = `echo $exam | cut -d"/" -f1`
	echo $n $bnum $tnum $exam
	if (! -e $datapath/$bnum/$tnum/images/${exam}_cube_fl.idf) then
		echo "   missing ${exam}_cube_fl.idf"
	endif
	if (! -e $datapath/$bnum/$tnum/images/${exam}_cube_fl_ax.idf) then
		cd $datapath/$bnum/$tnum/images
		resample_image_axial ${exam}_cube_fl.int2 ${exam}_cube_fl_ax
	endif
	if (! -e $datapath/$bnum/$tnum/images/${exam}_t1v.int2) then
		echo " no ${exam}_t1v.int2"
	endif
	if (! -e $datapath/$bnum/$tnum/images/${exam}_cube_fl_axa.int2) then
		cd $datapath/$bnum/$tnum/images
		echo " aligning T2 images to T1"
		align_tool ${exam}_cube_fl_ax ${exam}_t1v ${exam}_cube_fl_axa
	endif
	if ($viewflag == 1) then
		svk_multi_view $datapath/$bnum/$tnum/images/${exam}_cube_fl_axa.int2 $datapath/$bnum/$tnum/images/${exam}_t1v.int2
	endif
	if (-e $datapath/$bnum/$tnum/spectra_csi) then
		set ncmplx = `ls $datapath/$bnum/$tnum/spectra_csi/*.cmplx | wc -l`
		if ($ncmplx > 0) then
			echo "   spectra_csi $ncmplx cmplx files"
		else
			echo "   no processing?"
			if ($processflag == 1) then
				process_mrsi_7t.x ${exam}_csi --i ${exam}
			endif
		endif
	else
		cd $datapath/$bnum/$tnum/
		mkdir spectra_csi
		cd spectra_csi
		if (! -e $datapath/$bnum/$tnum/rawfiles/${exam}_csi) then
			echo " where is raw csi file"
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
	

	echo " "
	@ n++
	shift t2list
end
echo $nt2list