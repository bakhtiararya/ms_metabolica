#!/bin/csh -f

# $Header: written by Yan Li 

foreach filename (PerfrecovFail2 PerfphFail2 Perfnonlin_rfFail2)
     if (-e /home/liyan/${filename}.txt) then
           /bin/rm /home/liyan/${filename}.txt
     endif
end

cd /home/liyan/

set snum = a
set tnum = b

set number = 0

foreach line (`cat PerfReprocList.txt`)

#  echo $line
  
  if ($line =~ s????) then
     set snum = $line
  else if ($line =~ t????) then
     set tnum = $line
  endif

  if (($snum =~ s????) && ($tnum =~ t????)) then

      if ( (-e /data/spore/$snum/$tnum) || (-e /data/spore/3T/$snum/$tnum) ) then

         set number = `arithmetic $number + 1`

         if (-e /data/spore/$snum/$tnum) then
            set data_dir = /data/spore/$snum/$tnum
         else 
            set data_dir = /data/spore/3T/$snum/$tnum
         endif

         set roi_dir = /data/brain_work/yan/spore/spore_rois/$snum

         set cbv_name = ${roi_dir}/${tnum}_nonlin_cbv_t1ca.real
         set perf_status = error
         if (-e $cbv_name) then
            foreach temp_dir (perf_aligned perf_align_rigid perf)
                set temp_name = ${data_dir}/${temp_dir}/nonlin_fit/${tnum}_nonlin_cbv_t1ca.real
                if (-e ${temp_name}.gz) then
                    gunzip ${temp_name}.gz
                endif
                if (-e ${temp_name}) then
                    cmp -s ${cbv_name} ${temp_name}
                    if ($status == 0) then
                         set perf_status = ${temp_dir}
                    endif
                 endif
             end
          endif

          echo $snum $tnum $perf_status

	  if ($perf_status =~ perf_align_rigid) then
               if (! -e ${roi_dir}/${tnum}_ph_t1ca.real) then
			set temp_name = ph
			if (-e ${data_dir}/${perf_status}/non_parametric/${tnum}_rpeak.real) then
			    cd ${data_dir}/${perf_status}/non_parametric
			    /home/liyan/script/cshellscript/resample_perf_image.x ${tnum} rpeak t1ca
                            if (-e ${tnum}_rpeak_t1ca.real) then
				cp ${tnum}_rpeak_t1ca.* ${roi_dir}
				cd ${roi_dir}
				name_change.x ${tnum}_rpeak_t1ca ${tnum}_ph_t1ca
				cp ${data_dir}/${perf_status}/non_parametric/${tnum}_rpeak_t1ca.* ${roi_dir}
				set temp_status = 3
				echo $snum $tnum $perf_status >> /home/liyan/Perf${temp_name}Fail2.txt
			     endif
                         endif
                endif
          endif
               
          if ($perf_status =~ perf) then
             foreach temp_name (recov ph nonlin_rf)
		if ($temp_name =~ nonlin_rf) then
		     set tempsub = nonlin_fit
                else
		     set tempsub = non_parametric
		endif      
                set file_name = ${tnum}_${temp_name}_t1ca.real
                if ((-e ${roi_dir}/${file_name}) || (-e ${roi_dir}/${file_name}.gz)) then
                        cmp -s ${roi_dir}/${file_name} ${data_dir}/perf/${tempsub}/${file_name}
                        if ($status == 0) then
                               set temp_status = 0
			else
			       set temp_status = 1
                               cp ${data_dir}/perf/${tempsub}/${tnum}_${temp_name}_t1ca.* ${roi_dir}/
                        endif
                 else 
			set temp_dir = ${data_dir}/${perf_status}/${tempsub}/${tnum}_${temp_name} 
			if ((-e ${temp_dir}_t1ca.real) || (-e ${temp_dir}_t1ca.real.gz)) then
                               set temp_status = 0
                        else if ((-e ${temp_dir}.real) || (-e ${temp_dir}.real.gz)) then
			       cd ${data_dir}/${perf_status}/${tempsub}
                               /home/liyan/script/cshellscript/resample_perf_image.x ${tnum} ${temp_name} t1ca
        			if (-e ${temp_dir}_t1ca.real) then
                                    cp ${temp_dir}_t1ca.* ${roi_dir}
                                    set temp_status = 0
                                else
                                    set temp_status = -1
				endif
			else
                              set temp_status = -2
                        endif
                  endif
                  if (($temp_status == -2) && ($temp_name =~ ph)) then
			cd ${data_dir}
			/netopt/share/bin/local/brain/make_perf $tnum -b
		        if (-e ${data_dir}//${perf_status}/${tempsub}/${tnum}_${temp_name}.real) then
				cd ${data_dir}/${perf_status}/${tempsub}
                               /home/liyan/script/cshellscript/resample_perf_image.x ${tnum} ${temp_name} t1ca
                                if (-e ${temp_dir}_t1ca.real) then
                                    cp ${temp_dir}_t1ca.* ${roi_dir}
                                    set temp_status = 0
 				endif
			endif
		  endif
                  echo $snum $tnum $perf_status $temp_status >> /home/liyan/Perf${temp_name}Fail2.txt
              end
          endif

          if (($snum =~ s1123) && ($tnum =~ t2740)) then
	      set perf_status = None
          endif
	  
      endif
  endif  
end


echo Total exam number is $number
