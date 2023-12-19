#!/bin/csh -f

# $Header: written by Yan Li 

set filename = $1
set projectdir = /home/liyan/projects/short_te_3t7t
cd ${projectdir} 

if (! -e ${filename}.txt) then
	echo "${projectdir}/${filename}.txt does not exist"
	exit 1
endif

set bnum = b0000
set tnum = t0000
#set snum = s00
set n = 1

set datadir = (data/spore3/brain_clinical data/bioe5/QUEST data/bioe1/QUEST data/bioe2/NEW_LGG data/bioe2/NEW_HGG data/bioe2/REC_LGGdata/bioe2/REC_HGG data/lhst4/7T_btumor_patients data/bioe1/7T_btumor_patients data/lhst3/rad001 data/bioe1/REC_LGG data/lhst3/NEW_RAD001 data/bioe1/hsp_phase_2 data/bioe2/LoGlio)


foreach line (`cat ${filename}.txt`)

     set bnumpre = $bnum
     set tnumpre = $tnum
 #    set snumpre = $snum
	 set pass = 0

     if (($line =~ b????) || ($line =~ b???)) then
        set bnum = $line
     else if (($line =~ t????) || ($line =~ t?????)) then
        set tnum = $line
   #  else if (($line =~ s?) || ($line =~ s??)) then
   #  	set snum = $line
     endif

	 foreach dpath ($datadir)
	 	if (-e /${dpath}/${bnum}/${tnum}) then
	 		
	 		cd /${dpath}/${bnum}/${tnum}
	 		set nspec = `ls -d ./spectra* | wc -l`
	 		set dspec = `ls -d ./spectra*`
	 	#	echo $n $bnum $tnum $dpath ${nspec}spectra
	 		set specstring = 
	 		set snum =
	 		set echotime =
	 		set specdirname = 
	 		set m = 1
	 		while ($m <= $nspec)
	 			set specdirname = `echo $dspec[$m] | cut -d"/" -f2`
	 			set ddffile = `ls ./${specdirname}/*cor_sum.ddf`
	 			set ddffile = `echo $ddffile[1] | cut -d"/" -f3`
	 			if (${%ddffile} > 0) then
		 			set snum = `grep -w "series number" ./${specdirname}/$ddffile | cut -d":" -f2`
		 			set snum = `echo $snum[1]`
	 				set echotime = `grep -w "echo time" ./${specdirname}/$ddffile | cut -d":" -f2`
	 				set echotime = `echo $echotime[1] | cut -d"." -f1`
	 				set specstring = `echo "$specstring, $specdirname($snum/$echotime)"`
	 		#	echo "$n,$bnum,$tnum,$nspec,$k,$specdirname,$snum, $echotime"
	 			else
	 				set specstring = `echo "$specstring, $specdirname"`
	 			endif
	 			@ m++
	 		end
	 		echo "$n,$bnum,$tnum,$nspec,$specstring"
	 		@ n++
	 	endif
	 end
end