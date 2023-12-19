#!/bin/csh 
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/vtk_registration/trunk/apply_dof_no_dynamic.x $
#   $Rev: 8024 $
#   $Author: jasonc $
#   $Date: 2008-08-07 17:29:19 -0700 (Thu, 07 Aug 2008) $
#

# Usage :apply_dof_no_dynamic_new

#set original_dynamic = $1
#set first_root       = $2
#set dof_file         = $3
#set new_dynamic      = $4

set rootname         = $1
set signadir         = $2
set doffile          = $3
set new_dynamic      = $4

set MODIFY_IDF         = /netopt/bin/local/modify_idf_v5
set READ_IDF_FIELD     = /netopt/share/bin/local/brain/read_idf_field.x
set MAKE_ANALYZE       = /netopt/bin/local/brain/make_analyze
set APPLY_VTK          = /netopt/share/bin/local/brain/vtktransformation.x
set FIX_ROOTNAME       = /netopt/share/bin/local/brain/fix_rootname.x
set EXTRACT_TIMEPOINT  = /netopt/share/bin/local/brain/extract_timepoint.x
set REVERSE_IMAGE      = /netopt/share/bin/local/brain/get_range.x

set force_order        = force_order

if (${#argv} < 3) then
  echo
  echo "Usage: apply_dofs_no_dynamic.x rootname signadir "
  echo "       doffile output"
  echo
  echo "       'rootname' can be whatever output rootname you want "
  echo
  echo "       'doffile'  is the nonrigid deformation file generated "
  echo "                  by vtknreg"
  echo 
  echo "       The output will have a rootname_first.int2 and  "
  echo "       rootname_dynamic.int2 file, corresponding to the unwarped"
  echo "       EPI sequence and the first image of that sequence."
  echo 
  echo "       Last modified: Feb 05"
  exit
endif

# first need to re-import dynamic

set original_dynamic = ${rootname}_dynamic
set first_root = ${rootname}_first

set total_images   = `/netopt/share/bin/local/brain/count   ${signadir}`

import  -f 1 -l ${total_images} ${signadir} ${original_dynamic}
force_dynamic_si.x ${original_dynamic} ${first_root} ${original_dynamic}

# Get some basic information about the number of slices we need

set dynamic_size   = `read_idf_field.x ${original_dynamic}.idf npix`
set first_size     = `read_idf_field.x ${first_root}.idf       npix`
set num_timepoints = `echo $dynamic_size[3] $first_size[3] / p | dc`
echo ${num_timepoints}
set num_slices     = $first_size[3]

set timepoint      = 1

while (${timepoint} <= ${num_timepoints})

#  @ first_image = ${num_slices} * ( ${timepoint} - 1 ) + 1
#  @ last_image  = ${first_image} + ${num_slices} - 1

  echo
  echo ----- Transforming timepoint $timepoint -----
  echo

  # Usage: extract_timepoint.x <dynamic_root> <first_root> <time> <output_root>

  ${EXTRACT_TIMEPOINT} ${original_dynamic}                   \
                       ${first_root}                         \
                       ${timepoint}                          \
                       ${original_dynamic}_${timepoint}

  ${APPLY_VTK} ${original_dynamic}_${timepoint}.idf          \
               ${new_dynamic}_${timepoint}.idf               \
               -dofin ${doffile}                            \
         

  if (${timepoint} == 1) then               # Need to create the output file

    cp -f ${new_dynamic}_${timepoint}.int2 ${rootname}_first.int2
    cp -f ${new_dynamic}_${timepoint}.idf  ${rootname}_first.idf  
    ${FIX_ROOTNAME} ${rootname}_first  

    mv  ${new_dynamic}_${timepoint}.int2 \
        ${new_dynamic}.int2

  else                                      # Otherwise we can just append it
    cat ${new_dynamic}_${timepoint}.int2 \
        >> ${new_dynamic}.int2
    rm -f ${new_dynamic}_${timepoint}.int2 
  endif

  # Cleanup the debris

  rm -f ${new_dynamic}_${timepoint}.idf        \
        ${original_dynamic}_${timepoint}.idf   \
        ${original_dynamic}_${timepoint}.int2  \
	${rootname}_temp_${timepoint}.idf      \
        ${rootname}_temp_${timepoint}.int2

  @ timepoint = $timepoint + 1

end

# We've built the INT2, but we still need an IDF.  Fortunately this 
# should be exactly the same as the original IDF (except the rootname)

cp -f ${original_dynamic}.idf ${new_dynamic}.idf
${FIX_ROOTNAME} ${new_dynamic}

mv  ${new_dynamic}.idf  ${original_dynamic}.idf
mv  ${new_dynamic}.int2  ${original_dynamic}.int2
${FIX_ROOTNAME} ${original_dynamic}

