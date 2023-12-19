#! /bin/csh -f
# $Header: written by Yan Li 

set bnum2 = (b1957 b3214 b2495 b383 b355 b3199 b3640 b446 b1878)
#b3312
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

	     cd $k/$i/$j/spectra_short/
	     mkdir rois_analysis
	     cp $k/$i/$j/rois/${j}_t2all.* rois_analysis
	     cp $k/$i/$j/images/${j}_fla.* rois_analysis
	     cd rois_analysis
	     gunzip *.gz
	     resample_image ${j}_t2all.byt ${j}_fla.idf
	     cp ../${j}_short_fbcomb_1_cor_sum_cor_sum.ddf .
	     convert_ddfidf.x ${j}_short_fbcomb_1_cor_sum_cor_sum ${j}_short_fbcomb_1_cor_sum_cor_sum
	     percent_image.x ${j}_t2allr.int2 ${j}_short_fbcomb_1_cor_sum_cor_sum.idf ${j}_t2all_percent
	     /home/liyan/script/cshellscript/resample_press.x ${j}_short_fbcomb_1_cor_sum_cor_sum 1 1 1 ${j}_short ${j}_t2allr

		mask_math ${j}_t2allr -and ${j}_short_press_r ${j}_t2allr_press
		get_mask_values ${j}_t2allr ${j}_fla
		get_mask_values ${j}_t2allr_press ${j}_fla



        endif
      end
    end
end
