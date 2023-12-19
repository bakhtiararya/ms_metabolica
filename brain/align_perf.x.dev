#!/bin/csh -f
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/perfusion/trunk/scripts/align_perf.x $
#   $Rev: 40043 $
#   $Author: janinel@RADIOLOGY.UCSF.EDU $
#   $Date: 2017-08-02 12:53:58 -0700 (Wed, 02 Aug 2017) $
#



if (${#argv} < 3) then
  echo
  echo "align_perf_dev.x <root_name> <antomical_root> <alignment_type> [thresh]"
  echo
  echo "    aligns the perfusion data to the specified antomic series using BRAINSFIT software"
  echo "	run from within the perfusion alignment directory ie. perf_aligned "
  echo
  echo "             where:  <root_name>        is the t - number  "
  echo 
  echo "                     <anatomical_root>  is t1va, fsea, fla, or t1ca"
  echo                      
  echo "               and   <alignment_type>   is either 'rigid' or 'warp' "
  echo
  echo
  echo "             Optional input:  "
  echo "                     [thresh]           is the threshold to use in extract_brain.x "
  echo "                                        (default is .3 for fsea and .5 for t1va) "
  echo "                                        smaller #'s yield bigger brains "
  echo "                     [noalign]          data already aligned using specified type (rigid or warp), do "
  echo "                                        not repeat alignment."
  echo
  echo "              For example: "
  echo
  echo "                  align_perf_dev.x t1234 t1va warp "
  echo
  echo "               will do the following:  "
  echo "				1) extract the scalp from the t1va  "
  echo "				2) align the _first perfusion image in the perf folder to the _t1vabr " 
  echo "                3) apply the alignment to the entire dynamic dataset"
  echo "                4) rerun make_perf to create maps of normalized, nonparametric and nonlinearly fitted data"
  echo
  echo "     should use the t1va scan whenever possible. fsea works next best, followed by t1ca"
  echo
  echo "     Note, that the warp option uses the qb3 grid and data should be in an accessible location (e.g. /data/*) "
  echo
  echo "     Written by:    Janine M. Lupo, Ph.D."
  exit
endif

echo ""
echo ""

log_processing -l ./ -s "$0 $*"


set align = 1; 
echo $argv | grep '\-\-noalign'; 
if (  $status == 0 ) then
    set argv = `echo $argv | sed 's/--noalign//' ` ; 
    set align = 0; 
endif
echo "argv: $argv"

set root = $1;
set target_root = $2;
set type = $3;


if (${#argv} < 4) then

  if (${target_root} == fsea) then
      set thresh = .3
  else if (${target_root} == t1va) then 
      set thresh = .5
  else
      set thresh = .4
  endif

else
  set thresh = $4

endif

set target = ${root}_${target_root};

set cur_dir = `pwd`;


set extract = /netopt/share/bin/local/brain/extract_brain.x
set align_tool = /netopt/share/bin/local/brain/align_tool.dev
set apply_dynamic = /home/janinel/bin/apply_transform_to_dynamic.x
set perf = /netopt/share/bin/local/brain/make_perf.dev

#-----------------------
#create new directory for aligned images and copy over necessary files
#-----------------------

#mkdir perf_aligned

echo ""
echo "cp ../images/${target}.i* ."
cp ../images/${target}.i* .


gunzip -fq *.gz


#------------------------
#extract brain from t1va
#------------------------
echo ""
echo "======================================================="; 
echo "Extract brain"; 
echo "Using a threshold of ${thresh} for brain extraction"
echo "${extract} ${target} ${target}br ${thresh}"
${extract} ${target} ${target}br ${thresh}
${extract} ${root}_first ${root}_firstbr .1
echo "======================================================="; 
echo "";

#------------------------
#perform either rigid or nonrigid alignment
#------------------------

echo ""
echo "======================================================="; 
echo "run alignment: $align"
pwd


if  (${type} == rigid) then

    if ( $align == 1 ) then 
  
        ${align_tool} -k BRAINS -f "--transformType Rigid,ScaleVersor3D,ScaleSkewVersor3D" ${root}_firstbr ${target}br ${root}_firsta

        
    endif 
 
else if (${type} == warp) then


    if ( $align == 1 ) then 

		align_tool.dev -k BRAINS -f "--transformType Rigid,ScaleVersor3D,ScaleSkewVersor3D,BSpline --maxBSplineDisplacement 5 --splineGridSize 10,20,10" ${root}_firstbr ${target}br ${root}_firsta

    endif 
 	 
else

  	 echo "Invalid type of alignment specified, must choose either 'rigid' or 'warp' ";

endif

set dof_file = ${root}_firstbr_to_${target}br_transform.tfm
echo "transform file is ${dof_file}"


echo "======================================================="; 
echo ""


#-----------------------
#apply transformation
#-----------------------


echo ""
echo "======================================================="; 
echo "Apply Transformation: $align"
if ( $align == 1 ) then 

# first to first image
cp ${root}_first.idf tmp.idf
rm ${root}_first.i*
${align_tool} -k BRAINS ${root}_firstbr ${target}br ${root}_first_tmp -t ${dof_file}
resample_image_v5 << EOF
${root}_first_tmp.int2
${root}_firstbr.idf
${root}_first
t
s
EOF
mv tmp.idf ${root}_first.idf 
rm ${root}_first_tmp.*

# then to dynamic file

${apply_dynamic} ${root} ${dof_file} ${root}_dynamica
    
#     echo "${apply_dynamic} ${root} ${dof_file} ${root}_dynamica"
#     ${apply_dynamic} ${root} ${dof_file} ${root}_dynamica
#     
    mv ${root}_dynamica.int2 ${root}_dynamic.int2
    mv ${root}_dynamica.idf ${root}_dynamic.idf
    fix_rootname.x ${root}_dynamic
endif
    
echo "======================================================="; 
echo ""

