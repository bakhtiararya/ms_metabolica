#!/bin/csh 
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/vtk_registration/trunk/align_nonrigid_grid.x $
#   $Rev: 8024 $
#   $Author: jasonc $
#   $Date: 2008-08-07 17:29:19 -0700 (Thu, 07 Aug 2008) $
#

set target = $1:r
set source = $2:r

qsub -pe brain_pe 1                          \
     -l  arch=glinux                         \
     -N  warp_${target}_to_${source}         \
     -o  vtknreg_${target}_to_${source}.log  \
     -e  /dev/null                           \
     -v  PATH                                \
     -cwd                                    \
     -M  ${USER}@mrsc.ucsf.edu               \
     /netopt/share/bin/local/brain/vtknreg.x $* -v 3
