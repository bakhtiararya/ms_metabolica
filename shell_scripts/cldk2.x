#!/bin/csh -f

# $Header: written by Yan Li 

switch ($#argv)
  case 2
     set root = $1
     set cl_type = $2
  breaksw
  case 1
     set root = $1
     set cl_type = 0
  breaksw
  default:
    echo Usage: cldk.x rootname cl_type
    echo "      cl_type = 0 (default) or 1 (whole)"
    exit 1
endsw


set chan = 32

set tempc = `arithmetic $chan + $chan`
set tempc = `echo $tempc | cut -d"." -f1`


set num = 1
while ($num <= $tempc)
    /bin/rm $1_${num}.cmplx $1_${num}.ddf $1_${num}.cmplx.gz
    endif
    set num = `arithmetic $num + 1`
    set num = `echo $num | cut -d"." -f1`
end

set num = 1
while ($num <= $tempc)
     /bin/rm $1*_${num}_*phased.cmplx $1*_${num}_*phased.ddf $1*_${num}_*phased.cmplx.gz
     /bin/rm $1*_${num}_*fptphase.cmplx $1*_${num}_*fptphase.ddf $1*_${num}_*fptphase.cmplx.gz
     /bin/rm $1*_${num}_*selbox.cmplx $1*_${num}_*selbox.ddf $1*_${num}_*selbox.cmplx.gz
     /bin/rm $1*_${num}_*selvol.cmplx $1*_${num}_*selvol.ddf $1*_${num}_*selvol.cmplx.gz
     /bin/rm $1*_${num}_*correct.cmplx $1*_${num}_*correct.ddf $1*_${num}_*correct.cmplx.gz
     /bin/rm $1*_${num}_*cor_back.cmplx $1*_${num}_*cor_back.ddf $1*_${num}_*cor_back.cmplx.gz
     /bin/rm $1*_${num}_*cor.cmplx $1*_${num}_*cor.ddf $1*_${num}_*cor.cmplx.gz
     /bin/rm -r $1_*${num}_cor_met
     set num = `arithmetic $num + 1`
     set num = `echo $num | cut -d"." -f1`
end

/bin/rm *.idf *.real *.peak

if (${cl_type} == 1) then
     set num = 1
     /bin/rm *est*.idf *.real *.peak *.int2
     while ($num <= $tempc)
        /bin/rm $1*_${num}_*cor_sum.cmplx $1*_${num}_*cor_sum.ddf $1*_${num}_*cor_sum.cmplx.gz
        /bin/rm $1*_${num}_*est.peak
        set num = `arithmetic $num + 1`
        set num = `echo $num | cut -d"." -f1`
     end
endif
