#!/bin/csh -f

# $Header: written by Yan Li 
#rm /home/liyan/PerfProcStat.txt

set snum = (s1233 s1265 s0969 s1418)
set tnum = (t0006 t0007 t0008 t0009 t2884 t2443 t3344)

foreach i ($snum)
  foreach j ($tnum)

     if ((-e /data/spore/3T/$i/$j) || (-e /data/spore/$i/$j)) then

        echo $i $j
        if (-e /data/spore/$i/$j) then
          set data_dir = /data/spore/$i/$j
        else 
          set data_dir = /data/spore/3T/$i/$j
        endif
           
        cd ${data_dir}

        if (! -e perf_aligned) then
           if (-e perf_orig) then
              mv perf_orig perf_orig_orig
           endif
           if (! -e perf) then
              make_perf $j
           endif
           align_perf.x $j warp
        endif
            
        set perf_dir = ${data_dir}/perf_aligned
        set cbv_dir = ${data_dir}/perf_aligned/nonlin_fit
        set cbv_name = ${data_dir}/perf_aligned/nonlin_fit/${j}_nonlin_cbv.real
        set perf_stat = None
        
        if (-e ${perf_dir}) then
            set perf_stat = Perf_aligned        
        endif
        if (-e ${cbv_dir}) then
            set perf_stat = Nonlin_fit
        endif
        if (-e ${cbv_name}) then
            set perf_stat = Cbv
        endif

#        echo $i $j ${perf_stat}
        echo $i $j $perf_stat >> /home/liyan/PerfProcStat.txt

     endif

   end

 endif
end


