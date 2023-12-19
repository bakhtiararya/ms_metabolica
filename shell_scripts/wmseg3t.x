#!/bin/csh -f

set snum = $1
set tnum = $2
set data_dir = /data/spore/${snum}/${tnum}

if (! -e ${data_dir}) then
   set data_dir = /data/spore/3T/${snum}/${tnum}
   if (! -e ${data_dir}) then
       echo 'Data can not find' 
       exit 1
   else 
       echo 'Data acquired at 3T'
   endif
endif

echo 'Data is located at ' ${data_dir}
echo ' '

set image_dir = ${data_dir}/images
cd $image_dir

#rm ${tnum}_t1va_*

#if (! -e ${tnum}_t1va_wm.byt.gz) then

#    segment_t1v.x ${tnum}_t1va
    segment_t1v_grid.x ${tnum}_t1va 0 1
    erode_image.x ${tnum}_t1va_wm.byt ${tnum}_t1va_wme.byt 2

    if (! -e ${data_dir}/spore_rois) then
         mkdir ${data_dir}/spore_rois
    endif

    mask_connect ${tnum}_t1va_wme ${tnum}_wm 15 4
    cp ${tnum}_wm.* ../spore_rois

#endif
