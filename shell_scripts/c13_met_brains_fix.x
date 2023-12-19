#!/bin/csh -f

set tnum = $1
set tmat = $3
set ref = $2

set flist = `ls ${tnum}*.real`
set n = 1

foreach i ($flist)
   set tempf = $flist[1]
   set fname = `echo $tempf | cut -d"." -f1`
   echo $n $fname
   align_tool ${fname} $ref ${fname}_to_c13 -t $tmat
   @ n++
   shift flist
end
