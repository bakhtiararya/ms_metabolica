#!/bin/csh -f

echo " " 
echo "LcModel quantification ..." 
set z = 0 
set root = $2

foreach x (c)
  foreach type (cor_sum phased)
   if ($x == c) then
        echo "  - combined data-set"
        set filename = $1_${root}_cor_sum_comb_${type}
   else
      # echo "  - Enter channel number with highest 2 signals (1-8): "
      # set y = $<
        set y = $x
        set filename = $1_${root}_${y}_${type}
        echo "  - channel $y"
   endif
   if (-e ${filename}.cmplx) then
       invFTCmplx -p 2048 ${filename}
       cp ${filename}.ddf ${filename}_inv.ddf
       svcmplx2Raw.x ${filename}_inv
       7TLcModel ${filename}_inv n 90
       set z = `arithmetic $z + 1`
       set z = `echo $z | cut -d"." -f1`
       echo " "
    else
       echo "${filename}.cmplx does not exist"
    endif
 end
end
