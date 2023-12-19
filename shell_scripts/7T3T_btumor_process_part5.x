#! /bin/csh -f
# $Header: written by Yan Li 

if (-e /home/liyan/process_error.txt) then
   /bin/rm /home/liyan/process_error.txt
endif

set bnum = (b446 b1878) #(b3203 b2716 b2969 b1355 b3244 b1720 b3303 b3255 b0078 b3311 b3313 b3324 b2977 b2661 b968 b3388 b3398)
set tnum = (t9230 t9204) #(t7683 t7705 t7851 t7762 t7778 t7845 t7990 t7999 t8001 t8058 t8071 t8100 t8161 t8209 t8260 t8264 t8342)
set tnumseven = (t9231 t9203) #(t7679 t7704 t7854 t7757 t7777 t7846 t7991 t8000 t8002 t8059 t8072 t8097 t8160 t8205 t8256 t8265 t8345)

set copypath = /data/brain_work/yan/pt_7t/3DMRSI
set datapath = /data/spore3/brain_clinical

set n = 0
foreach i ($bnum)
   foreach j ($tnum)
       if (-e ${datapath}/$i/$j) then
	cd ${copypath}/$i/3t
	convert_ddfidf.x ${j}_fbcomb_sum_cp_cor_sum ${j}_fbcomb_sum_cp_cor_sum
	percent_image.x ${j}_t2all.byt ${j}_fbcomb_sum_cp_cor_sum.idf ${j}_t2all_percent
      endif
   end
end
