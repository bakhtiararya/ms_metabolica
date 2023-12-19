#!/bin/csh -f
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/apply_dof_to_dynamic/trunk/apply_dof_to_dynamic_new.x $
#   $Rev: 3556 $
#   $Author: jasonc $
#   $Date: 2008-05-06 14:08:10 -0700 (Tue, 06 May 2008) $
#


# Usage :apply_dofs_to_dynamic_new

#set original_dynamic = $1
#set first_root       = $2
#set dof_file         = $3
#set new_dynamic      = $4

set rootname         = $1
set any_dof          = $2
set new_dynamic      = $3

set MODIFY_IDF         = modify_idf_v5
set READ_IDF_FIELD     = read_idf_field.x
set MAKE_ANALYZE       = make_analyze
set APPLY_VTK          = vtktransformation.x
set FIX_ROOTNAME       = fix_rootname.x
set EXTRACT_TIMEPOINT  = extract_timepoint.x
set REVERSE_IMAGE      = get_range.x


set force_order        = force_order

if (${#argv} < 3) then
  echo
  echo "Usage: apply_dof_to_dynamic_new.x rootname dof_file  output"
  echo
  echo "       'rootname' can be whatever output rootname you want "
  echo
  echo "       'dof_file'  is any deformation file generated "
  echo "                  by vtknreg or vtkareg"
  echo 
  echo "       The output will have a rootname_first.int2 and  "
  echo "       rootname_dynamic.int2 file, corresponding to the unwarped"
  echo "       EPI sequence and the first image of that sequence."
  echo
  echo "       Michael C. Lee, Ph.D."
  echo "       University of California, San Francisco"
  echo 
  echo "       Last modified: 20 April 04"
  exit
endif

# Get some basic information about the number of slices we need

set original_dynamic = ${rootname}_dynamic
set first_root = ${rootname}_first

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

#  ${APPLY_VTK} ${original_dynamic}_${timepoint}.idf          \
#               ${rootname}_temp1_${timepoint}.idf               \
#               -dofin ${rootname}_rigid.dof                            \
         
  ${APPLY_VTK} ${original_dynamic}_${timepoint}.idf          \
               ${new_dynamic}_${timepoint}.idf               \
               -dofin ${any_dof}                            \

#  ${APPLY_VTK}  ${rootname}_temp_${timepoint}.idf          \
#               ${new_dynamic}_${timepoint}.idf               \
#               -dofin ${rigid_dof}                            \
         

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


