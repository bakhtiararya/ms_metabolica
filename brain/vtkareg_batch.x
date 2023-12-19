#!/bin/csh 
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/vtk_registration/trunk/vtkareg_batch.x $
#   $Rev: 22695 $
#   $Author: jasonc@RADIOLOGY.UCSF.EDU $
#   $Date: 2011-12-12 12:13:20 -0800 (Mon, 12 Dec 2011) $
#


if ($#argv == 0) then
  printf "\n--------------------------------------------------------------\n"
  printf "  vtkareg_batch.x: submits as a batch job on a Linux node\n"
  printf "--------------------------------------------------------------\n"
  vtkareg.x $*
  exit
endif

# Find the output DOF file and use this to construct a log

set found_dof = 0
set iarg = 1
while ($iarg <= $#argv)
  if ("$argv[$iarg]" == "-dofout") then
    set found_dof = 1
    @ iarg = $iarg + 1
    set dof_name = $argv[$iarg]
  else
    @ iarg = $iarg + 1
  endif
end

if ($found_dof == 0) then
  printf "\nvtkareg_batch.x: you must specify a -dofout option\n\n"
  exit 
endif

set logfile = $dof_name:r
set logfile = ${logfile}_vtkareg.log

if (-e ${logfile}) then
  rm ${logfile}
endif

printf "\nOutput will be written to: $logfile\n\n"

qsub -q brain.q@@rrc_brain_desktop -N vtkareg -cwd \
     -e /dev/null                                   \
     -o ${logfile}                                  \
     /netopt/share/bin/local/brain/vtkareg.x $* -v 3

printf "\n"

