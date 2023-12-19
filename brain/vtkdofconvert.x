#!/bin/tcsh -f

setenv LD_LIBRARY_PATH /netopt/bin/local/brain/vtkCISG/lib:/data/camelot/mclee/VTK-4.0_sol2/bin:/opt/local/lib

/netopt/bin/local/brain/vtkCISG/vtkdofconvert $*
