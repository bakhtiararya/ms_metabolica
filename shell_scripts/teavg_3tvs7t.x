#! /bin/csh -f

if ( $#argv < 3 ) then
      echo Usage: teavg_3tvs7t.x froot field peak imageroot
      exit 1
endif 

signa_csi_v6.dev $1
echo $2

switch ($2)
   case 7t
      /home/liyan/script/cshellscript/n32avg.x $1 7t

      cp $1_1.ddf $1_avg_1.ddf
       
      set a = `grep -i "dimension 2" $1_avg_1.ddf`
      set b = `echo $a | cut -d":" -f4`
      set c = `echo $b | awk '{print $1}'`
      echo $c
      if ($c == 48) then
          /home/liyan/script/cshellscript/edit_ddf_d2.x $1_avg_1.ddf
      else
         /home/liyan/script/cshellscript/edit_ddf_avg.x $1_avg_1.ddf
      endif 

      cp $1_avg_1.ddf $1_avg_2.ddf
      cp $1_avg_1.ddf $1_avg_3.ddf
      cp $1_avg_1.ddf $1_avg_4.ddf
      cp $1_avg_1.ddf $1_avg_5.ddf
      cp $1_avg_1.ddf $1_avg_6.ddf
      cp $1_avg_1.ddf $1_avg_7.ddf
      cp $1_avg_1.ddf $1_avg_8.ddf

      /home/liyan/script/TEavg7t/set_teavg7t.x $1_avg_1 $1_avg

      process_spec_v6.dev -p $1_avg.par $1_avg_1.cmplx
      process_spec_v6.dev -p $1_avg.par $1_avg_2.cmplx
      process_spec_v6.dev -p $1_avg.par $1_avg_3.cmplx
      process_spec_v6.dev -p $1_avg.par $1_avg_4.cmplx
      process_spec_v6.dev -p $1_avg.par $1_avg_5.cmplx
      process_spec_v6.dev -p $1_avg.par $1_avg_6.cmplx
      process_spec_v6.dev -p $1_avg.par $1_avg_7.cmplx
      process_spec_v6.dev -p $1_avg.par $1_avg_8.cmplx

      cp /home/liyan/script/TEavg7t/$3.peak .
      /home/liyan/script/TEavg7t/csi_teavg.x $1_avg_1 $3
      /home/liyan/script/TEavg7t/csi_teavg.x $1_avg_2 $3
      /home/liyan/script/TEavg7t/csi_teavg.x $1_avg_3 $3
      /home/liyan/script/TEavg7t/csi_teavg.x $1_avg_4 $3
      /home/liyan/script/TEavg7t/csi_teavg.x $1_avg_5 $3
      /home/liyan/script/TEavg7t/csi_teavg.x $1_avg_6 $3
      /home/liyan/script/TEavg7t/csi_teavg.x $1_avg_7 $3
      /home/liyan/script/TEavg7t/csi_teavg.x $1_avg_8 $3

      cp /home/liyan/script/TEavg7t/$3_avg.peak .
      /home/liyan/script/TEavg7t/combine.x  $1_avg $4

      /home/liyan/script/TEavg7t/csi_teavg_avg.x $1_avg_comb_phased $3_avg

      cmplx2jmrui.x 2djwm_avg_comb_phased_cor_sum
      /home/hratiney/jMrui_V2.2/WaterSuppCmljar -k 25 -b -100 150 2djwm_avg_comb_phased_cor_sum_invfull1.mrui
      cp 2djwm_avg_comb_phased_cor_sum_inv.ddf 2djwm_avg_comb_phased_cor_sum_invfull1_SVDSup.ddf
      /home/liyan/script/test/SunOS_sparc/writeCmplx 2djwm_avg_comb_phased_cor_sum_invfull1_SVDSup

      svcmplx2Raw.x 2djwm_avg_comb_phased_cor_sum_invfull1_SVDSup
      7T2DJLcModel 2djwm_avg_comb_phased_cor_sum_invfull1_SVDSup n 7

   breaksw
   case 3t
       /home/liyan/script/cshellscript/n32avg.x $1 3t

       cp $1_1.ddf $1_avg.ddf
       /home/liyan/script/cshellscript/edit_ddf_avg.x $1_avg.ddf

       /home/liyan/script/TEavg7t/set_teavg3t.x $1_avg $1_avg

       process_spec_v6.dev -p $1_avg.par $1_avg.cmplx
       cp /home/liyan/script/TEavg7t/$3.peak .
       /home/liyan/script/TEavg7t/csi_sv_3t.x $1_avg_phased $3

       cmplx2jmrui.x $1_avg_phased_cor_sum 
       /home/hratiney/jMrui_V2.2/WaterSuppCmljar -k 20 -b -35 100 $1_avg_phased_cor_sum_invfull1.mrui
       cp $1_avg_phased_cor_sum_inv.ddf $1_avg_phased_cor_sum_invfull1_SVDSup.ddf
       /home/liyan/script/test/SunOS_sparc/writeCmplx $1_avg_phased_cor_sum_invfull1_SVDSup
       
       svcmplx2Raw.x  $1_avg_phased_cor_sum_invfull1_SVDSup
       7T2DJLcModel $1_avg_phased_cor_sum_invfull1_SVDSup n 3

   breaksw
endsw


