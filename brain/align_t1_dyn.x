#!/bin/csh -f

if (${#argv} < 1) then
  echo
  echo "align_t1_dyn.x <root_name>"
  echo
  echo "    Aligns the first image of the t1 dynamic series to the t1va antomic series using vtk software "
  echo "    Should be run from inside the t1_dyn folder. "
  echo "             where:  <root_name>        is the t - number  "
  echo 
  echo
  echo
  echo "              For example: "
  echo
  echo "                  align_t1_dyn.x t1234 "
  echo
  echo "               will do the following:  "
  echo "		1) copy the _t1va image from images folder to the t1_dyn folder "
  echo "		2) rigidly align the _1 image in the t1_dyn folder to the _t1va " 
  echo "                3) apply the alignment to the entire dynamic dataset"
  echo
  echo "              Troubleshooting: "
  echo "                Make sure all images are in the same t1_dyn folder "
  echo "                Make sure script is called from inside t1_dyn folder "
  echo
  echo "              Visual Alignment Check:  "
  echo "                Look at _1a image and _t1va image and visually confirm they are aligned. "
  echo
  echo "     Written by:    Emma Essock-Burns and Janine M. Lupo, Ph.D."
  exit
endif

set root = $1


#make sure all images are in the same folder

cp ../images/${root}_t1va.* .

gunzip *.gz

#apply rigid vtk alignment

vtkareg_grid.x ${root}_t1va.idf ${root}_1.idf  -rigid -dofout t1_dyn.dof 


vtktransformation.x ${root}_kps.idf ${root}_kpsa.idf -target ${root}_t1va.idf -dofin t1_dyn.dof

vtktransformation.x ${root}_fbv.idf ${root}_fbva.idf -target ${root}_t1va.idf -dofin t1_dyn.dof


vtktransformation.x ${root}_1.idf ${root}_1a.idf -target ${root}_t1va.idf -dofin t1_dyn.dof


