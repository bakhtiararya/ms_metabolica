#!/bin/csh -f
## Inas Khayal  2/12/09
## Qiuting Wen updated 2/13/12
## align_diffu.x
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/diffusion/trunk/utilities/align_diffu.x $
#   $Rev: 25269 $
#   $Author: bolson@RADIOLOGY.UCSF.EDU $
#   $Date: 2012-06-19 12:15:30 -0700 (Tue, 19 Jun 2012) $

if (${#argv} < 1) then
  echo                      
  echo "Usage: align_diffu.x t# anatomical_root [r] [t threshold] [b bvalue] "
  echo 
  echo "Example: align_diffu.x t1234 fsea t 0.2 b 1000      "
  echo
  echo "   Aligns fsea/fla/t1ca (in order of best option)   " 
  echo "   otherwise add a flag 'r' to resample.            "
  echo "   If t is included the following value will be     "
  echo "   used as the threshold for extract_brain.x        "
  echo "   If b is included it will be assumed that the     "
  echo "   root of the diffusion files is t#_b#. For        "
  echo "   example: t1234_1000_adc.idf.                     "
  echo
  echo "   NOTE: If fsea is chosen then a 0.2 default       "
  echo "         threshold for extract_brain.x will be      "
  echo "         added.                                     "
  echo
  echo "** Run this program inside the diffusion directory**"
  echo
  exit
endif

set resample = 0
set extract_brain_threshold = "" 
set diffu_root = $1
foreach f (`seq 1 1 ${#argv}`) 
    if( $argv[$f] == 'r' ) then
        set resample = 1
    endif
    if( $argv[$f] == 't' ) then
        @ index = $f + 1
        if( $index <= ${#argv} ) then
            set extract_brain_threshold = $argv[$index] 
        endif
    endif
    if( $argv[$f] == 'b' ) then
        @ index = $f + 1
        if( $index <= ${#argv} ) then
            set diffu_root = {$1}_$argv[$index] 
        endif
    endif
end 

set log = align_diffu.log
echo "align_diffu.x $*"  >> $log 

set fl = {$1}_{$2}.idf
cp ../images/${fl:r}.* .
echo "cp ../images/${fl:r}.* . " >> $log



### Set if aligning or resampling
if ($resample) then
    set a = r
    echo "Diffusion will be resampled to $1_$2" >> $log
    echo "Diffusion will be resampled to $1_$2" 
else
    set a = a
    echo "Diffusion will be aligned to $1_$2" >> $log
    echo "Diffusion will be aligned to $1_$2"
endif



### Gunzip to ensure no images are zipped
gunzip *.gz -f

### Check if fla, t1ca, or t1va to do a brain extraction
if (${2} == 'fsea' || ${2} == 'fla' || ${2} == 't1ca' || ${2} == 't1va' && ${a} == 'a') then	
    set fl = $1_$2_brain.idf
    if (${2} == 'fsea' && $extract_brain_threshold == "" ) then
        set extract_brain_threshold = 0.2
    endif
    echo "extract_brain.x $1_$2 $1_$2_brain $extract_brain_threshold" >> $log
    extract_brain.x $1_$2 $1_$2_brain $extract_brain_threshold 

    if($status != 0) then
        echo "************************************"
        echo "ERROR! While executing:"
        echo "extract_brain.x $1_$2 $1_$2_brain"
        echo "************************************"
        exit(1)
    endif
else 
endif


### Set the variables 
set adc = {$diffu_root}_adc.idf
set fa = {$diffu_root}_fa.idf
set ev1 = {$diffu_root}_ev1.idf
set ev2 = {$diffu_root}_ev2.idf
set ev3 = {$diffu_root}_ev3.idf
set adc_dif = {$diffu_root}_adc_dif.idf
set ev1_dif = {$diffu_root}_ev1_dif.idf
set ev2_dif = {$diffu_root}_ev2_dif.idf
set ev3_dif = {$diffu_root}_ev3_dif.idf
set t2di = {$diffu_root}_t2di.idf
set multiply_dif = {$diffu_root}_multiply_dif.idf 
set transform = ${diffu_root}_t2di_to_$1_$2_brain_transform

set adca = {$diffu_root}_adc${a}.idf
set adca2 = {$diffu_root}_adc${a}.int2
set faa = {$diffu_root}_fa${a}.idf
set faa2 = {$diffu_root}_fa${a}.int2
set t2dia = {$diffu_root}_t2di${a}.idf
set t2dia2 = {$diffu_root}_t2di${a}.int2
set ev1a = {$diffu_root}_ev1${a}.idf
set ev1a2 = {$diffu_root}_ev1${a}.int2
set ev2a = {$diffu_root}_ev2${a}.idf
set ev2a2 = {$diffu_root}_ev2${a}.int2
set ev3a = {$diffu_root}_ev3${a}.idf
set ev3a2 = {$diffu_root}_ev3${a}.int2
set adc_difa = {$diffu_root}_adc_dif${a}.idf
set adc_difa2 = {$diffu_root}_adc_dif${a}.int2
set ev1_difa = {$diffu_root}_ev1_dif${a}.idf
set ev1_difa2 = {$diffu_root}_ev1_dif${a}.int2
set ev2_difa = {$diffu_root}_ev2_dif${a}.idf
set ev2_difa2 = {$diffu_root}_ev2_dif${a}.int2
set ev3_difa = {$diffu_root}_ev3_dif${a}.idf
set ev3_difa2 = {$diffu_root}_ev3_dif${a}.int2
set multiply_difa = {$diffu_root}_multiply_dif${a}.idf 
set multiply_difa2 = {$diffu_root}_multiply_dif${a}.int2


if (${a} == 'a') then 
    ### Aligning the t2di and diffusion images to the anatomical images 
    echo Aligning the t2di and diffusion images to the anatomical images 
   if (!(-e ${t2di})) then
		if (!(-d ../diffusion)) then
	    	cp ../diffusion_b=1000/${t2di:r}.i* .
	else 
	    cp ../diffusion/${t2di:r}.i* . 
		endif
   endif
   if (!(-e ${transform})) then
		echo "flirt.x ${t2di:r} ${fl:r} ${t2dia:r}" >> $log
		flirt.x ${t2di:r} ${fl:r} ${t2dia:r} 
        if($status != 0) then
	    echo "************************************"
	    echo "ERROR! While executing:"
	    echo "flirt.x ${t2di:r} ${fl:r} ${t2dia:r}"
	    echo "************************************"
	    exit(1)
		endif
   endif
    
    ### Applying the transformation to diffusion images
    echo Applying the transformation to diffusion images
    if (-e ${adc}) then
		echo "flirt_apply_transform.x ${adc:r} ${fl:r} ${adca:r} ${transform}" >> $log
		flirt_apply_transform.x ${adc:r} ${fl:r} ${adca:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${adc:r} ${fl:r} ${adca:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${fa}) then
		echo "flirt_apply_transform.x ${fa:r} ${fl:r} ${faa:r} ${transform}" >> $log
		flirt_apply_transform.x ${fa:r} ${fl:r} ${faa:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${fa:r} ${fl:r} ${faa:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${ev1}) then
		echo "flirt_apply_transform.x ${ev1:r} ${fl:r} ${ev1a:r} ${transform}" >> $log
		flirt_apply_transform.x ${ev1:r} ${fl:r} ${ev1a:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${ev1:r} ${fl:r} ${ev1a:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${ev2}) then
		echo "flirt_apply_transform.x ${ev2:r} ${fl:r} ${ev2a:r} ${transform}" >> $log
		flirt_apply_transform.x ${ev2:r} ${fl:r} ${ev2a:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${ev2:r} ${fl:r} ${ev2a:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${ev3}) then
		echo "flirt_apply_transform.x ${ev3:r} ${fl:r} ${ev3a:r} ${transform}" >> $log
		flirt_apply_transform.x ${ev3:r} ${fl:r} ${ev3a:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${ev3:r} ${fl:r} ${ev3a:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${adc_dif}) then
		echo "flirt_apply_transform.x ${adc_dif:r} ${fl:r} ${adc_difa:r} ${transform}" >> $log
		flirt_apply_transform.x ${adc_dif:r} ${fl:r} ${adc_difa:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${adc_dif:r} ${fl:r} ${adc_difa:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${multiply_dif}) then
		echo "flirt_apply_transform.x ${multiply_dif:r} ${fl:r} ${multiply_difa:r} ${transform}" >> $log
		flirt_apply_transform.x ${multiply_dif:r} ${fl:r} ${multiply_difa:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${multiply_dif:r} ${fl:r} ${multiply_difa:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${ev1_dif}) then
		echo "flirt_apply_transform.x ${ev1_dif:r} ${fl:r} ${ev1_difa:r} ${transform}" >> $log
		flirt_apply_transform.x ${ev1_dif:r} ${fl:r} ${ev1_difa:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${ev1_dif:r} ${fl:r} ${ev1_difa:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${ev2_dif}) then
		echo "flirt_apply_transform.x ${ev2_dif:r} ${fl:r} ${ev2_difa:r} ${transform}" >> $log
		flirt_apply_transform.x ${ev2_dif:r} ${fl:r} ${ev2_difa:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${ev2_dif:r} ${fl:r} ${ev2_difa:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 

    if (-e ${ev3_dif}) then
		echo "flirt_apply_transform.x ${ev3_dif:r} ${fl:r} ${ev3_difa:r} ${transform}" >> $log
		flirt_apply_transform.x ${ev3_dif:r} ${fl:r} ${ev3_difa:r} ${transform}
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "flirt_apply_transform.x ${ev3_dif:r} ${fl:r} ${ev3_difa:r} ${transform}"
		echo "************************************"
		exit(1)
        endif
    endif 


else
    ### Resampling the t2di and diffusion images to the anatomical images 
    echo Resampling the t2di and diffusion images to the anatomical images 
    if (-e ${adc}) then
        if (!(-e ${adca2})) then
            echo "resample_image ${1}_adc.int2 ${1}_${2}.idf" >> $log
            resample_image ${1}_adc.int2 ${1}_${2}.idf 
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_adc.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif
    endif

    if (-e ${fa}) then
        if (!(-e ${faa2})) then
            echo "resample_image ${1}_fa.int2 ${1}_${2}.idf" >> $log
	    resample_image ${1_fa.int2 ${1}_${2}.idf
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1_fa.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif 
    endif

    if (-e ${t2di}) then
        if (!(-e ${t2dia2})) then
            echo "resample_image ${1}_t2di.int2 ${1}_${2}.idf" >> $log
	    resample_image ${1}_t2di.int2 ${1}_${2}.idf
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_t2di.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif 
    endif

    if (-e ${ev1}) then
        if (!(-e ${ev1a2})) then
            resample_image ${1}_ev1.int2 ${1}_${2}.idf
            echo "resample_image ${1}_ev1.int2 ${1}_${2}.idf" >> $log
	    resample_image ${1}_ev1.int2 ${1}_${2}.idf
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_ev1.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif
    endif

    if (-e ${ev2}) then
        if (!(-e ${ev2a2})) then
            echo "resample_image ${1}_ev2.int2 ${1}_${2}.idf" >> $log
            resample_image ${1}_ev2.int2 ${1}_${2}.idf
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_ev2.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
	endif
    endif

    if (-e ${ev3}) then
        if (!(-e ${ev3a2})) then
            echo "resample_image ${1}_ev3.int2 ${1}_${2}.idf" >> $log  
            resample_image ${1}_ev3.int2 ${1}_${2}.idf 
	    if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_ev3.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif
    endif

    if (-e ${adc_dif}) then
        if (!(-e ${adc_difa2})) then
            echo "resample_image ${1}_adc_dif.int2 ${1}_${2}.idf" >> $log
            resample_image ${1}_adc_dif.int2 ${1}_${2}.idf 
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_adc_dif.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif
    endif

    if (-e ${multiply_dif}) then
        if (!(-e ${multiply_difa2})) then
            echo "resample_image ${1}_multiply_dif.int2 ${1}_${2}.idf" >> $log
            resample_image ${1}_multiply_dif.int2 ${1}_${2}.idf
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_multiply_dif.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif 
    endif 

    if (-e ${ev1_dif}) then
        if (!(-e ${ev1_difa2})) then
            echo "resample_image ${1}_ev1_dif.int2 ${1}_${2}.idf" >> $log
            resample_image ${1}_ev1_dif.int2 ${1}_${2}.idf
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_ev1_dif.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif
    endif

    if (-e ${ev2_dif}) then
        if (!(-e ${ev2_difa2})) then
            echo "resample_image ${1}_ev2_dif.int2 ${1}_${2}.idf" >> $log
            resample_image ${1}_ev2_dif.int2 ${1}_${2}.idf
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_ev2.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif
    endif

    if (-e ${ev3_dif}) then
        if (!(-e ${ev3_difa2})) then
            echo "resample_image ${1}_ev3_dif.int2 ${1}_${2}.idf" >> $log
            resample_image ${1}_ev3_dif.int2 ${1}_${2}.idf
            if($status != 0) then
		echo "************************************"
		echo "ERROR! While executing:"
		echo "resample_image ${1}_ev3.int2 ${1}_${2}.idf"
		echo "************************************"
		exit(1)
	    endif
        endif
    endif
endif


### Remove any vtk output or error messages
rm *mask*     
echo "rm *mask* files" >> $log
echo "Processing complete. " >> $log
echo "Processing complete. "
echo "     " >> $log

