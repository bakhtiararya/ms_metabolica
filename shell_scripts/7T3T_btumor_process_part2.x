#! /bin/csh -f
# $Header: written by Yan Li 

if (-e /home/liyan/process_error2.txt) then
   /bin/rm /home/liyan/process_error2.txt
endif

set bnum2 = (b3006 b3312 b1957 b3214 b2495 b383 b355 b3199 b3640 b446 b1878)
set tnum2 = (t8231 t9094 t9100 t9109 t9141 t9150 t9187 t9188 t9206 t9204 t9230)
set datapath = (/data/spore3/brain_clinical /data/bioe1/hsp_phase_2 /data/lhst3/rad001)

set n = 0
foreach i ($bnum2)
   foreach j ($tnum2)
      foreach k ($datapath)
	
        if (-e $k/$i/$j) then
           echo $i/$j
           set n =  `arithmetic $n + 1`
           set n = `echo $n | cut -d"." -f1`

	   #if (-e $k/$i/$j/spectra/${j}_fbcomb_sum_cp_cor_sum.ddf) then
	   #    cd $k/$i/$j/spectra
	   #    /home/liyan/script/svs7tup/vss_7t.x ${j}_fbcomb_sum_cp_cor_sum
           #endif
	   #if (-e $k/$i/$j/spectra/${j}_fbcomb_cp_cor_sum.ddf) then
	   #    cd $k/$i/$j/spectra
	   #    /home/liyan/script/svs7tup/vss_7t.x ${j}_fbcomb_cp_cor_sum
           #endif
           #set a = `ls $k/$i/$j/spectra/*vss.idf`
           #echo $a

       if (-e $k/$i/$j/spectra/${j}_fbcomb_sum_cp_cor_sum.ddf) then
	  set rawname = ${j}_fbcomb_sum_cp_cor_sum
       else
          set rawname = ${j}_fbcomb_cp_cor_sum
       endif
        cd $k/$i/$j/spectra
	if (! -e ${rawname}_inv.raw) then
              echo "{rawname}.raw didn't exist" >> /home/liyan/process_error2.txt
        endif 

         foreach sl (3 4 5 6 7 8 9 10 11 12 13 14)

                 set fcontrol = ${rawname}_vss_sl${sl}_lc.control
		 

                 if (-e $fcontrol) then
		    cp $fcontrol ../spectra_short/${j}_short_fbcomb_1_cor_sum_cor_sum_vss_sl${sl}_lc.control
          #          7TMRSIQuantifyLcModel ${rawname}_inv $sl 144

                    set fcontrol = Slice_${sl}_Results/${rawname}_inv.control

      	            set rowst = `grep -i IROWST $fcontrol | cut -d"=" -f2`
                    set rowend = `grep -i IROWEN $fcontrol | cut -d"=" -f2`
                    set colst = `grep -i ICOLST $fcontrol | cut -d"=" -f2`
                    set colend = `grep -i ICOLEN $fcontrol | cut -d"=" -f2`
                    set voxsk = `grep -i NVOXSK $fcontrol | cut -d"=" -f2`
                    set nrow = `arithmetic $rowend - $rowst`
                    set nrow = `arithmetic $nrow + 1` 
                    set ncol = `arithmetic $colend - $colst`
                    set ncol = `arithmetic $ncol + 1`

                    set calnvox = `arithmetic $nrow x $ncol`
                    set calnvox = `arithmetic $calnvox - $voxsk`
                    set calnvox = `echo $calnvox | cut -d"." -f1`
 
                    set nps = `ls Slice_${sl}_Results/*.ps`

                    if (`echo ${#nps}` > 0) then
	                set nvox = `ls Slice_${sl}_Results/*.ps | wc -l`
                        if ($calnvox != $nvox) then
		           set nmiss = `arithmetic $calnvox - $nvox`
		           set nmiss = `echo $nmiss | cut -d"." -f1`	
                           echo "     Missing $nmiss ($nvox/$calnvox) voxel(s) in $i/$j/Slice$sl" >> /home/liyan/process_error2.txt
                        else 
                           echo "     $nvox/$calnvox voxels in $i/$j/Slice$sl" >> /home/liyan/process_error2.txt
                        endif
                   else

                      echo "      Missing  ${calnvox} voxels in $i/$j/Slice$sl" >> /home/liyan/process_error2.txt
                   endif

               else
                   echo "       Missing control files from matlab in $i/$j/Slice$sl" >> /home/liyan/process_error2.txt
               endif
          end


#short TE
      cd $k/$i/$j/spectra_short
      set rawname = ${j}_short_fbcomb_1_cor_sum_cor_sum
	if (! -e ${rawname}_inv.raw) then
              echo "{rawname}_inv.raw didn't exist" >> /home/liyan/process_error2.txt
        endif 

         foreach sl (3 4 5 6 7 8 9 10 11 12 13 14)

                 set fcontrol = ${rawname}_vss_sl${sl}_lc.control
		 

                 if (-e $fcontrol) then

     #               7TMRSIQuantifyLcModel ${rawname}_inv $sl 35

                    set fcontrol = Slice_${sl}_Results/${rawname}_inv.control

      	            set rowst = `grep -i IROWST $fcontrol | cut -d"=" -f2`
                    set rowend = `grep -i IROWEN $fcontrol | cut -d"=" -f2`
                    set colst = `grep -i ICOLST $fcontrol | cut -d"=" -f2`
                    set colend = `grep -i ICOLEN $fcontrol | cut -d"=" -f2`
                    set voxsk = `grep -i NVOXSK $fcontrol | cut -d"=" -f2`
                    set nrow = `arithmetic $rowend - $rowst`
                    set nrow = `arithmetic $nrow + 1` 
                    set ncol = `arithmetic $colend - $colst`
                    set ncol = `arithmetic $ncol + 1`

                    set calnvox = `arithmetic $nrow x $ncol`
                    set calnvox = `arithmetic $calnvox - $voxsk`
                    set calnvox = `echo $calnvox | cut -d"." -f1`
 
                    set nps = `ls Slice_${sl}_Results/*.ps`

                    if (`echo ${#nps}` > 0) then
	                set nvox = `ls Slice_${sl}_Results/*.ps | wc -l`
                        if ($calnvox != $nvox) then
		           set nmiss = `arithmetic $calnvox - $nvox`
		           set nmiss = `echo $nmiss | cut -d"." -f1`	
                           echo "     Missing $nmiss ($nvox/$calnvox) voxel(s) in $i/${j}_short/Slice$sl" >> /home/liyan/process_error2.txt
                        else 
                           echo "     $nvox/$calnvox voxels in $i/${j}_short/Slice$sl" >> /home/liyan/process_error2.txt
                        endif
                   else

                      echo "      Missing  ${calnvox} voxels in $i/${j}_short/Slice$sl" >> /home/liyan/process_error2.txt
                   endif

               else
                   echo "       Missing control files from matlab in $i/${j}_short/Slice$sl" >> /home/liyan/process_error2.txt
               endif
          end







        endif
      end
    end
end
