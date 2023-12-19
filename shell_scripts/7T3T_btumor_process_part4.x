#! /bin/csh -f
# $Header: written by Yan Li 

if (-e /home/liyan/process_error.txt) then
   /bin/rm /home/liyan/process_error.txt
endif

#set bnum = (b1355 b3244 b1720 b3303 b3255 b0078 b3311 b3313 b3324 b2977 b2661 b968 b3388 b3398)
#b3203 b2716 b2969 b1878 b446)

set bnum = (b446)
set tnum = (t7683 t7705 t7851 t7762 t7778 t7845 t7990 t7999 t8001 t8058 t8071 t8100 t8161 t8209 t8260 t8264 t8342 t9230 t9204)
set tnumseven = (t7679 t7704 t7854 t7757 t7777 t7846 t7991 t8000 t8002 t8059 t8072 t8097 t8160 t8205 t8256 t8265 t8345 t9231 t9203)

set copypath = /data/brain_work/yan/pt_7t/3DMRSI
set datapath = /data/spore3/brain_clinical

set n = 0
foreach i ($bnum)
   foreach j ($tnum)
       if (-e ${datapath}/$i/$j) then

           if (! -e ${copypath}/$i/3t/${j}_t2all.idf) then
                   cp ${datapath}/$i/$j/rois/${j}_t2all.* ${copypath}/$i/3t
           endif
          if (! -e ${copypath}/$i/3t/${j}_t1va.idf) then
		if (-e ${datapath}/$i/$j/images/${j}_t1va.idf) then
                   cp ${datapath}/$i/$j/images/${j}_t1va.* ${copypath}/$i/3t
		else
		   cp ${datapath}/$i/$j/images/${j}_t1ca.* ${copypath}/$i/3t
		   cd ${copypath}/$i/3t
		   cp ${j}_t1ca.idf ${j}_t1va.idf
		    cp ${j}_t1ca.int2 ${j}_t1va.int2
		    fix_rootname.x ${j}_t1va
		endif
            endif
         if (! -e ${copypath}/$i/3t/${j}_fla.idf) then
                   cp ${datapath}/$i/$j/images/${j}_fla.* ${copypath}/$i/3t
           endif
	  if (! -e ${copypath}/$i/3t/${j}_t2allr.idf) then
		  cd ${copypath}/$i/3t/
		   resample_image ${j}_t2all.byt ${j}_fla.idf
           endif
	  if (! -e ${copypath}/$i/3t/${j}_t2all_percent) then
		cd ${copypath}/$i/3t
		 convert_ddfidf.x ${j}_fbcomb_sum_cp_cor_sum ${j}_fbcomb_sum_cp_cor_sum
		 percent_image.x ${j}_t2all.byt ${j}_fbcomb_sum_cp_cor_sum.idf ${j}_t2all_percent
	   endif
	 if (! -e ${copypath}/$i/3t/${j}_press_r.idf) then
		cd ${copypath}/$i/3t
		/home/liyan/script/cshellscript/resample_press.x ${j}_fbcomb_sum_cp_cor_sum 1 1 1 ${j} ${j}_t2allr
         endif 
gunzip ${copypath}/$i/3t/${j}*t1v*.gz

		cd ${copypath}/$i/3t
		mask_math ${j}_t2allr -and ${j}_press_r ${j}_t2allr_press
		get_mask_values ${j}_t2allr ${j}_t1va
		get_mask_values ${j}_t2allr_press ${j}_t1va


           foreach k ($tnumseven)
              if (-e ${copypath}/$i/$k) then
 		  break
	      endif
           end
	   if (! -e ${copypath}/$i/$k/${k}_t1v_resampled.idf) then
		if (! -e ${copypath}/$i/$k/${k}_t1v.idf) then
		#    cp /data/lhst4/7T_btumor_patients/$i/$k/images/${k}_t1v.* ${copypath}/$i/$k
		echo "$i/$k missing t1v"
                endif
		cd  ${copypath}/$i/$k
#gunzip ${k}_comb_cor_sum.cmplx.gz
#gunzip ${k}_t1v*.gz
	#	 resample_image_spectra ${k}_t1v ${k}_comb_cor_sum
           endif
         /bin/rm  ${copypath}/$i/$k/${j}_t2all.*
	   if (! -e  ${copypath}/$i/$k/${j}_t2allr.idf) then
		cd ${copypath}/$i/$k
		ln -s ../3t/${j}_t2allr.idf
		ln -s ../3t/${j}_t2allr.int2
           endif
	   if (! -e ${copypath}/$i/$k/${j}_t1va.idf) then
		cd ${copypath}/$i/$k
		ln -s ../3t/${j}_t1va.idf
		ln -s ../3t/${j}_t1va.int2
	   endif

	   if (! -e ${copypath}/$i/$k/${j}_t2allr_7t.idf) then
		cd ${copypath}/$i/$k
                flirt_obl.x ${j}_t1va ${k}_t1v_resampled ${j}_t1va_7t transform.mat
		apply_flirt.x ${j}_t2allr ${k}_t1v_resampled ${j}_t2allr_7t transform.mat
           endif
	   if (! -e ${copypath}/$i/$k/${k}_comb_cor_sum.idf) then
		cd ${copypath}/$i/$k/
		 convert_ddfidf.x ${k}_comb_cor_sum ${k}_comb_cor_sum
	   endif
	   if (! -e ${copypath}/$i/$k/${j}_${k}_t2all_percent.idf) then
		cd ${copypath}/$i/$k/
           	percent_image.x ${j}_t2allr_7t.int2 ${k}_comb_cor_sum.idf ${j}_${k}_t2all_percent
	   endif
	if (! -e ${copypath}/$i/$k/${k}_press_r.idf) then
		cd ${copypath}/$i/$k
		/home/liyan/script/cshellscript/resample_press.x ${k}_comb_cor_sum 1 1 1 ${k} ${j}_t2allr_7t
         endif 
		cd ${copypath}/$i/$k
		mask_math ${j}_t2allr_7t -and ${k}_press_r ${k}_t2allr_press
		get_mask_values ${j}_t2allr_7t ${k}_t1v_resampled
		get_mask_values ${k}_t2allr_press ${k}_t1v_resampled


       endif
  end
end
