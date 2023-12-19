#!/bin/tcsh 
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/vtk_registration/trunk/vtktransformation.x $
#   $Rev: 8024 $
#   $Author: jasonc $
#   $Date: 2008-08-07 17:29:19 -0700 (Thu, 07 Aug 2008) $
#

if (${#argv} == 0) then
  /netopt/bin/local/brain/vtkCISG/bin/vtktransformation  
  exit;
endif

set source_idf = $1
set output_idf = $2

# Check for existence of files

if (!(-e ${source_idf})) then
  printf "\nvtktransformation.x: Unable to find source file ${source_idf}\n\n"
  exit
endif

# Walk through the input arguments and see if the user requested 
# a resampling of the image (using the -target) flag.  Also check for 
# validity of input arguments.

set iarg      = 1
set reslice   = 0

while ($iarg <= $#argv)
  if ("$argv[$iarg]" == "-target") then
    set reslice = 1
    @ iarg = $iarg + 1
    set target_idf = $argv[$iarg]
    if (!(-e ${target_idf})) then
      printf "\nvtktransformation.x: unable to find target ${target_idf}\n\n"
      exit
    endif
  else
    @ iarg = $iarg + 1
  endif
end

# Run the transformation

/netopt/bin/local/brain/vtkCISG/bin/vtktransformation $*


if ($reslice == 0) then

  cp ${source_idf} ${output_idf}
  /netopt/share/bin/local/brain/fix_rootname.x $output_idf:r

else

  cp ${target_idf} ${output_idf}
  /netopt/share/bin/local/brain/fix_rootname.x $output_idf:r

  # Check to make sure the filetype didn't accidentally get changed
 
  set source_filetype = `read_idf_field.x ${source_idf} filetype`
  set output_filetype = `read_idf_field.x ${output_idf} filetype`

  if (${source_filetype[1]} != ${output_filetype[1]}) then
    modify_idf_filetype.x ${output_idf} ${source_filetype}
  endif

  set source_orientation = `read_idf_field.x ${source_idf} orientation`
  set target_orientation = `read_idf_field.x ${target_idf} orientation`

  if (${source_orientation[1]} != ${target_orientation[1]}) then
    printf "\n-----------------------------------------------------\n"
    printf "WARNING: orientation of target does not match source\n"
    printf "         resulting IDF will not be correct!\n"
    printf "-----------------------------------------------------\n\n"
  endif

endif

