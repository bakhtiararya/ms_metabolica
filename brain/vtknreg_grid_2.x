#!/bin/csh 
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/vtk_registration/trunk/vtknreg_grid_2.x $
#   $Rev: 22695 $
#   $Author: jasonc@RADIOLOGY.UCSF.EDU $
#   $Date: 2011-12-12 12:13:20 -0800 (Mon, 12 Dec 2011) $
#


onintr interrupt_handler

echo
echo Submitting job to grid on `date` 
echo "  (this may take a minute or two ...)"

set execution = "qsub -q brain.q@@rrc_brain_desktop -N vtknreg -l hostname=${1} -cwd -sync y /netopt/share/bin/local/brain/vtknreg.x"

set arg = 2
while ($arg <= ${#argv}) 
  set execution = "${execution} $argv[$arg]"
  @ arg = ${arg} + 1
end

${execution}

interrupt_handler:
"rm" -f vtknreg.pe*
"rm" -f vtknreg.po*
"rm" -f PI*

