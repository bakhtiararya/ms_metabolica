#!/bin/csh -f

# $Header: written by Yan Li 

set filename = atlas_list_03092015_temp04152015
set projectdir = /home/liyan/projects/atlas_spectra

if (-e /${filename}_output.csv) then
   /bin/rm ${projectdir}/${filename}_output.csv
   /bin/rm ${projectdir}/${filename}_acq_parameter_output.csv 
endif

cd ${projectdir}

set bnum = b0000
set tnum = t0000
set n = 0

echo "N,bnum,tnum,path, weight, nspecdir, nspec, rawdir, psd, rawname, readbox, readsats, octsats, lace, inrec, WStime, TE, specdir, dcos1, dcos2, dcos3, shimfile, boxalpha, xrescsi, yrescsi, zrescsi" >  ${projectdir}/${filename}_output.csv 
echo "N,bnum,tnum,path, nspecdir, nspec, tg, r1,r2,arf1, arf2, arf3, octsats, readsat, iaoct1, iaoct2, iaoct3, iaoct4, iaoct5, iaoct6, aoct1, aoct2, aoct3, aoct4, aoct5, aoct6, iasat1, iasat2, iasat3, iasat4, iasat5, iasat6, iasat7, iasat8, iasat9, asat1, asat2, asat3, asat4, asat5, asat6,asat7, asat8, asat9, foct1, foct2, foct3, foct4, foct5, foct6, fsat1, fsat2, fsat3, fsat4, fsat5, fsat6, fsat7, fsat8, fsat9, fcos1, fcos2, fcos3, fcos4, fcos5, fcos6"  >  ${projectdir}/${filename}_acq_parameter_output.csv 
	 

foreach line (`cat ${filename}.txt`)
   #   echo $line

     set bnumpre = $bnum
     set tnumpre = $tnum

     if (($line =~ b????) || ($line =~ b???)) then
        set bnum = $line
     else if ($line =~ t????) then
        set tnum = $line
     endif

     if (($bnum =~ $bnumpre) && ($tnum =~ $tnumpre)) then
		echo "duplicate $bnum $tnum"
     else 
	 	foreach temppath (spore3/brain_clinical bioe1/hsp_phase_2 lhst3/rad001 bioe5/QUEST brain_work/yan/mrs_3t) 
	    	if (-e /data/${temppath}/$bnum/$tnum) then
	    		cd /data/${temppath}/$bnum/$tnum	    		
	       		set n = `arithmetic $n + 1`
           		set n = `echo $n | cut -d"." -f1`
	       		
	       		set exam = `ls -d ./E* | cut -d"/" -f2` 
	       		set a = `grep raw Logfile | grep completed | cut -d"_" -f2 | cut -d"/" -f2`
	       		set nraw = `grep raw Logfile | grep -c completed`
	       		set nspecdir = `ls -dl spec* | wc -l`
	       		set nrawdir = `ls -dl $exam/*raw | wc -l`
	       			       		
	       		set x = 1
	       		while ($x <= $nraw)
	       			set rawdir = `echo $a | cut -d" " -f$x`
					set pname = `find $exam/${rawdir}_raw/ -type f ! -name "*.*"`
					set pname = `echo $pname | cut -d" " -f1 | cut -d"/" -f3`
	       			set psd = `rdump -A $exam/${rawdir}_raw/${pname} | grep -i yan | cut -d"=" -f2 | cut -d"#" -f1`
	       			set tg = `rdump -A $exam/${rawdir}_raw/${pname} | grep -i mps_tg | cut -d"=" -f2 | cut -d"#" -f1`
	       			set wt = `rdump -A $exam/${rawdir}_raw/${pname} | grep -i patweight | cut -d"=" -f2 | cut -d"#" -f1`
				set r1 = `rdump -A $exam/${rawdir}_raw/${pname} | grep -i mps_r1 | cut -d"=" -f2 | cut -d"#" -f1`
				set r2 = `rdump -A $exam/${rawdir}_raw/${pname} | grep -i mps_r2 | cut -d"=" -f2 | cut -d"#" -f1`
	       			
	       			set dbox = `grep read_box $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
	       			set doct = `grep oct_sats $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
	       			set dsat = `grep read_sats $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
	       			set lace = `grep lacemode $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
	       			set inrec = `grep inrecmode $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
	       			set wstime = `grep -w t_0102 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
	       			set wstime = `arithmetic $wstime / 1000`
	       			set wstime = `echo $wstime | cut -d"." -f1`
	       			set opte = `grep -w opte $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
	       			set opte = `arithmetic $opte / 1000`
	       			set opte = `echo $opte | cut -d"." -f1`
	       			
	       			set exshim = `ls $exam/${rawdir}_raw/*shim*`
	       			if (${%exshim} > 0) then
	       				set shimf = `tail -1 $exshim` 
	       				set shimf = `echo $shimf | awk '{print $1}'`
	       			else
	       				set shimf = noshimf
	       			endif
	       				
	       			set exshim = `ls $exam/${rawdir}_raw/*press*`
	       			if (${%exshim} > 0) then
	       				set boxalpha = `tail -1 $exshim` 
	       			else
	       				set boxalpha = unfound
	       			endif
	       				    
	       			set	xrescsi = `grep xrescsi $exam/${rawdir}_raw/*.dat | cut -d"=" -f2` 
	       			set	yrescsi = `grep yrescsi $exam/${rawdir}_raw/*.dat | cut -d"=" -f2` 
	       			set	zrescsi = `grep zrescsi $exam/${rawdir}_raw/*.dat | cut -d"=" -f2` 	
   			
	       			set b = `grep ${rawdir}_raw Logfile`
		       		set b =	`echo $b | grep "dir"`
		       		if (${%b} > 0) then		       			
		       			set specdir = `grep ${rawdir}_raw Logfile | grep -o "dir .*"`
		       			set specdir = `echo $specdir | cut -d" " -f2`
		       		else
		       			set specdir = spectra
		       		endif
		       		
		       		set c = `ls $specdir/*fbcomb_*cp_cor_sum.ddf`
		       		if (${%c} > 0) then
		       			set c = `echo $c | awk '{print $1}'`
		       			set dcos1 = `grep -w "acq. dcos1" $c`
		       			set dcos1 = `echo $dcos1 | cut -d":" -f2 | cut -d" " -f2-4`
		       			
		       			set dcos2 = `grep -w "acq. dcos2" $c`
		       			set dcos2 = `echo $dcos2 | cut -d":" -f2 | cut -d" " -f2-4`
		       			
		       			set dcos3 = `grep -w "acq. dcos3" $c`
		       			set dcos3 = `echo $dcos3 | cut -d":" -f2 | cut -d" " -f2-4`
		       			
		       		else
		       			set dcos1 = nan
		       			set dcos2 = nan
		       			set dcos3 = nan
		       		endif
		       		
		       		if ($nraw == $nspecdir) then
		       			set nspec = $nraw
		       		else
		       			set nspec = check
		       		endif
		       		
		       		set arf1 = `grep -w a_gzrf1 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       		set arf2 = `grep -w a_gxrf2 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       		set arf3 = `grep -w a_gyrf3 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       				       		
		       		if ($doct == 1) then
		       			 
			       		set aoct1 = `grep -w a_eosat1 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set aoct2 = `grep -w a_eosat2 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set aoct3 = `grep -w a_eosat3 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		    	   		set aoct4 = `grep -w a_eosat4 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set aoct5 = `grep -w a_eosat5 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set aoct6 = `grep -w a_eosat6 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct1 = `grep -w flip_eosat1 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct2 = `grep -w flip_eosat2 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct3 = `grep -w flip_eosat3 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct4 = `grep -w flip_eosat4 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct5 = `grep -w flip_eosat5 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct6 = `grep -w flip_eosat6 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iaoct1 = `grep -w ia_eosat1 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iaoct2 = `grep -w ia_eosat2 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iaoct3 = `grep -w ia_eosat3 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		    	   		set iaoct4 = `grep -w ia_eosat4 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iaoct5 = `grep -w ia_eosat5 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iaoct6 = `grep -w ia_eosat6 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			
		       			
		       			set asat1 = `grep -w a_eosat7 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set asat2 = `grep -w a_eosat8 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
				       	set asat3 = `grep -w a_eosat9 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		    		   	set asat4 = `grep -w a_eosat10 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set asat5 = `grep -w a_eosat11 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set asat6 = `grep -w a_eosat12 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set asat7 = `grep -w a_eosat13 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set asat8 = `grep -w a_eosat14 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set asat9 = `grep -w a_eosat15 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`	
		       			set fsat1 = `grep -w flip_eosat7 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat2 = `grep -w flip_eosat8 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat3 = `grep -w flip_eosat9 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat4 = `grep -w flip_eosat10 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat5 = `grep -w flip_eosat11 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat6 = `grep -w flip_eosat12 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set fsat7 = `grep -w flip_eosat13 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat8 = `grep -w flip_eosat14 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat9 = `grep -w flip_eosat15 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iasat1 = `grep -w ia_eosat7 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iasat2 = `grep -w ia_eosat8 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
				       	set iasat3 = `grep -w ia_eosat9 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		    		   	set iasat4 = `grep -w ia_eosat10 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iasat5 = `grep -w ia_eosat11 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iasat6 = `grep -w ia_eosat12 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iasat7 = `grep -w ia_eosat13 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iasat8 = `grep -w ia_eosat14 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iasat9 = `grep -w ia_eosat15 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`	
			       		
			       	else			       		
			       		set asat1 = `grep -w a_eosat1 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set asat2 = `grep -w a_eosat2 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set asat3 = `grep -w a_eosat3 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		    	   		set asat4 = `grep -w a_eosat4 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set asat5 = `grep -w a_eosat5 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set asat6 = `grep -w a_eosat6 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set asat7 = `grep -w a_eosat7 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set asat8 = `grep -w a_eosat8 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set asat9 = `grep -w a_eosat9 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set fsat1 = `grep -w flip_eosat1 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat2 = `grep -w flip_eosat2 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat3 = `grep -w flip_eosat3 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat4 = `grep -w flip_eosat4 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat5 = `grep -w flip_eosat5 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat6 = `grep -w flip_eosat6 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat7 = `grep -w flip_eosat7 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat8 = `grep -w flip_eosat8 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set fsat9 = `grep -w flip_eosat9 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iasat1 = `grep -w ia_eosat1 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iasat2 = `grep -w ia_eosat2 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iasat3 = `grep -w ia_eosat3 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		    	   		set iasat4 = `grep -w ia_eosat4 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iasat5 = `grep -w ia_eosat5 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iasat6 = `grep -w ia_eosat6 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set iasat7 = `grep -w ia_eosat7 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iasat8 = `grep -w ia_eosat8 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set iasat9 = `grep -w ia_eosat9 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			
		       			
		       			
			       		set aoct1 = `grep -w a_eosat10 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set aoct2 = `grep -w a_eosat11 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set aoct3 = `grep -w a_eosat12 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		    	   		set aoct4 = `grep -w a_eosat13 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set aoct5 = `grep -w a_eosat14 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set aoct6 = `grep -w a_eosat15 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
			       		set foct1 = `grep -w flip_eosat10 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct2 = `grep -w flip_eosat11 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct3 = `grep -w flip_eosat12 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct4 = `grep -w flip_eosat13 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct5 = `grep -w flip_eosat14 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			set foct6 = `grep -w flip_eosat15 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`
		       			
			       	endif
		       					       		
			       	set fcos1 = `grep -w freq_cosmod_eosat1 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`	
			       	set fcos2 = `grep -w freq_cosmod_eosat2 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`	
			       	set fcos3 = `grep -w freq_cosmod_eosat3 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`	
			       	set fcos4 = `grep -w freq_cosmod_eosat4 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`	
			       	set fcos5 = `grep -w freq_cosmod_eosat5 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`	
			       	set fcos6 = `grep -w freq_cosmod_eosat6 $exam/${rawdir}_raw/*.dat | cut -d"=" -f2`	
			       						       			
		       		echo "$n, $bnum, $tnum, $temppath, $wt, $nrawdir, $x, ${rawdir}_raw, $psd, $pname, $dbox, $dsat, $doct, $lace, $inrec, $wstime, $opte, $specdir, $dcos1, $dcos2, $dcos3, $shimf, $boxalpha, $xrescsi, $yrescsi, $zrescsi " >> ${projectdir}/${filename}_output.csv
					echo "$n, $bnum, $tnum, $temppath, $nrawdir, $x, $tg,$r1, $r2,$arf1, $arf2, $arf3, $doct, $dsat, $iaoct1, $iaoct2, $iaoct3, $iaoct4, $iaoct5, $iaoct6, $aoct1, $aoct2, $aoct3, $aoct4, $aoct5, $aoct6, $iasat1, $iasat2, $iasat3, $iasat4, $iasat5, $iasat6, $iasat7, $iasat8, $iasat9, $asat1, $asat2, $asat3, $asat4, $asat5, $asat6, $asat7, $asat8, $asat9, $foct1, $foct2, $foct3, $foct4, $foct5, $foct6, $fsat1, $fsat2, $fsat3, $fsat4, $fsat5, $fsat6, $fsat7, $fsat8, $fsat9, $fcos1, $fcos2, $fcos3, $fcos4, $fcos5, $fcos6" >>  ${projectdir}/${filename}_acq_parameter_output.csv 
						      		 
							       		  
		       		set x = `arithmetic $x + 1`
           			set x = `echo $x | cut -d"." -f1`
	       		end
	       		
            endif
        end
    endif
end
               
