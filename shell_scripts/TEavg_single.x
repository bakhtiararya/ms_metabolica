#! /bin/sh -f

filename=$1
export filename

Obj='Vol'
export Obj

Int=2.5
export Int

#cd $1
#idl /home/liyan/script/idl/runTE_avg.pro
#cd ..

mkdir ${1}_3ptavg
cd ${1}_3ptavg
cp ../$1/$1 .
idl /home/liyan/script/idl/runTE_avg_3pt.pro
cd ..

