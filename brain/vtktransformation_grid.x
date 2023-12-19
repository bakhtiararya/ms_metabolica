#!/bin/csh 
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/vtk_registration/trunk/vtktransformation_grid.x $
#   $Rev: 22695 $
#   $Author: jasonc@RADIOLOGY.UCSF.EDU $
#   $Date: 2011-12-12 12:13:20 -0800 (Mon, 12 Dec 2011) $
#

if ($#argv == 0) then
  printf "\n--------------------------------------------------------------\n"
  printf "  vtktransformation_grid.x: executes interactively on a Linux node\n"
  printf "--------------------------------------------------------------\n"
  vtktransformation.x $*
  exit
endif

qsub -q brain.q@@rrc_brain_desktop -N vtktransformation -cwd -sync y /netopt/share/bin/local/brain/vtktransformation.x $*


