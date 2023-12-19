#!/bin/csh -f
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/perfusion/trunk/scripts/align_perf_biopsy.x $
#   $Rev: 38952 $
#   $Author: janinel@RADIOLOGY.UCSF.EDU $
#   $Date: 2016-09-26 12:16:22 -0700 (Mon, 26 Sep 2016) $
#



if (${#argv} < 3) then
  echo
  echo "align_perf_biopsy.x <root_name> <antomical_root> <alignment_type> [thresh]"
  echo
  echo "    aligns the perfusion data to the specified antomic series using vtk software "
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
  echo "                  align_perf_biopsy.x t1234 t1va warp "
  echo
  echo "               will do the following:  "
  echo "		1) extract the scalp from the t1va  "
  echo "		2) align the _first perfusion image in the perf folder to the _t1vabr " 
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
set align_rigid = /netopt/share/bin/local/brain/vtkareg_grid.x
set align_warp =  /netopt/share/bin/local/brain/vtknreg_grid
set apply_dof = /netopt/share/bin/local/brain/vtktransformation.x
set apply_dynamic = /netopt/share/bin/local/brain/apply_dof_to_dynamic_new.x
set perf = /netopt/share/bin/local/brain/make_perf

#-----------------------
#create new directory for aligned images and copy over necessary files
#-----------------------

mkdir perf_aligned

echo ""
echo "cp images/${target}.i* perf_aligned/."
cp images/${target}.i* perf_aligned/.

echo "cp perf/${root}_first.i* perf_aligned/."
cp perf/${root}_first.i* perf_aligned/.

echo "cp perf/${root}_dynamic.i* perf_aligned/."
cp perf/${root}_dynamic.i* perf_aligned/.

echo ""
echo "cd perf_aligned"
cd perf_aligned
gunzip *.gz


#------------------------
#extract brain from t1va
#------------------------
echo ""
echo "======================================================="; 
echo "Extract brain"; 
echo "Using a threshold of ${thresh} for brain extraction"
echo "${extract} ${target} ${target}br ${thresh}"
${extract} ${target} ${target}br ${thresh}
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
        echo "${align_rigid} ${target}br.idf ${root}_first.idf -rigid -dofout ${root}_rigid.dof"
        ${align_rigid} ${target}br.idf ${root}_first.idf -rigid -dofout ${root}_rigid.dof
    endif 
    set dof_file = ${root}_rigid.dof

else if (${type} == warp) then


    if ( $align == 1 ) then 

        #
        #   Check here if the slice res is < 3mm.  If so, then downsample slice res to 3mm:
        # 
        echo downsample_slice_res -i ${target}br.int2 -o ${target}br.idf
        downsample_slice_res -i ${target}br.int2 -o ${target}br.idf

        echo ${align_warp} -g qb3 "${target}br.idf ${root}_first.idf -dx 10 -dy 5 -dz 10 -dofout ${root}_warp.dof"
        ${align_warp} -g qb3 "${target}br.idf ${root}_first.idf -dx 10 -dy 5 -dz 10 -dofout ${root}_warp.dof"
    endif 
    set dof_file = ${root}_warp.dof

else

  echo "Invalid type of alignment specified, must choose either 'rigid' or 'warp' ";

endif

echo "======================================================="; 
echo ""


#-----------------------
#apply transformation
#-----------------------

echo ""
echo "======================================================="; 
echo "Apply Transformation: $align"
if ( $align == 1 ) then 
    pwd
    echo "${apply_dof} ${root}_first.idf ${root}_firsta.idf -target ${target}br.idf -dofin ${dof_file}"
    ${apply_dof} ${root}_first.idf ${root}_firsta.idf -target ${target}br.idf -dofin ${dof_file}
    
    echo "${apply_dof} ${root}_first.idf ${root}_temp.idf -dofin ${dof_file}"
    ${apply_dof} ${root}_first.idf ${root}_temp.idf -dofin ${dof_file}
    
    echo "mv ${root}_temp.int2 ${root}_first.int2"
    mv ${root}_temp.int2 ${root}_first.int2
    
    echo "mv ${root}_temp.idf ${root}_first.idf"
    mv ${root}_temp.idf ${root}_first.idf
    fix_rootname.x ${root}_first  
    
    echo "${apply_dynamic} ${root} ${dof_file} ${root}_dynamica"
    ${apply_dynamic} ${root} ${dof_file} ${root}_dynamica
    
    mv ${root}_dynamica.int2 ${root}_dynamic.int2
    mv ${root}_dynamica.idf ${root}_dynamic.idf
    fix_rootname.x ${root}_dynamic
endif
    
echo "======================================================="; 
echo ""

#-----------------------
# reprocess perfusion parameters using aligned images
#-----------------------

echo ""
echo "======================================================="; 
echo "Reprocess perf with aligned images"
echo "cd ${cur_dir}"
cd ${cur_dir}
pwd
mv perf perf_orig
mv perf_aligned perf

echo "${perf} --no_err -b -f nonlinear -m 40 --fov 200 ${root}"
${perf} --no_err -b -f nonlinear -m 40 --fov 200 ${root} 
mv perf perf_aligned
mv perf_orig perf
