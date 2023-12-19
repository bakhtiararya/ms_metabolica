#!/bin/csh 
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/vtk_registration/trunk/vtknreg_grid.x $
#   $Rev: 22695 $
#   $Author: jasonc@RADIOLOGY.UCSF.EDU $
#   $Date: 2011-12-12 12:13:20 -0800 (Mon, 12 Dec 2011) $
#


if ($#argv == 0) then
  printf "\n--------------------------------------------------------------\n"
  printf "  vtknreg_grid.x: executes interactively on a Linux node\n"
  printf "--------------------------------------------------------------\n"
  vtknreg.x $*
  exit
endif

printf "\nSubmitting job to grid on `date`\n"
printf "    (this may take a minute or two ...)\n\n"

qsub -q brain.q@@rrc_brain_desktop -N vtknreg -cwd -sync y /netopt/share/bin/local/brain/vtknreg.x $*
    

