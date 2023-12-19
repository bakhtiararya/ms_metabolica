#!/bin/csh -f

# $Header: written by Yan Li 
# b3466

set pathroot = /data/spore3/brain_clinical/b3466

if ($#argv != 2) then
	echo Usage: b3466 t-ref t-working
    exit 1
endif

set tref = $1
set twork = $2

cd ${pathroot}/MRSI_Alignment/${twork}_${tref}


if (! -e ${tref}_t1va.idf) then
  nifti_file_convert --input ${tref}_t1va.nii.gz  --swap_dims --scale_nifti --output_root ${tref}_t1va
endif
if (! -e ${twork}_t1va.idf) then
  nifti_file_convert --input ${twork}_t1va.nii.gz  --swap_dims --scale_nifti --output_root ${twork}_t1va
endif

if (! -e ${twork}_fla.nii.gz) then
  nifti_file_convert --input ${pathroot}/${twork}/images/${twork}_fla.int2 --swap_dims --scale_nifti --output_root ${twork}_fla
endif
if (! -e ${twork}_fla.idf) then
   nifti_file_convert --input ${twork}_fla.nii.gz  --swap_dims --scale_nifti --output_root ${twork}_fla
endif

if (! -e ${tref}_fla.nii.gz) then
  nifti_file_convert --input ${pathroot}/${tref}/images/${tref}_fla.int2 --swap_dims --scale_nifti --output_root ${tref}_fla
endif
if (! -e ${tref}_fla.idf) then
   nifti_file_convert --input ${tref}_fla.nii.gz  --swap_dims --scale_nifti --output_root ${tref}_fla
endif

if (! -e  ${twork}_fla_to_${tref}_fla.idf) then
   BRAINSFit --fixedVolume  ${tref}_fla.nii.gz --movingVolume ${twork}_fla.nii.gz --initialTransform ${twork}_t1va_to_${tref}_t1va.tfm --transformType Affine --outputVolume ${twork}_fla_to_${tref}_fla.nii.gz
    nifti_file_convert --input  ${twork}_fla_to_${tref}_fla.nii.gz  --swap_dims --scale_nifti --output_root ${twork}_fla_to_${tref}_fla
endif



set specroot = lac_fbhsvdfcomb
if (! -e brain_analysis_${tref}_${specroot}) then
   cp -r ${pathroot}/${tref}/brain_analysis_${tref}_${specroot} .
endif
if (! -e brain_analysis_${twork}_${specroot}) then
   cp -r ${pathroot}/${twork}/brain_analysis_${twork}_${specroot} .
endif

if (! -e  ${tref}_lac_fbhsvdfcomb_sum_empcs_cor.ddf) then
   echo "can not find ${tref}_lac_fbhsvdfcomb_sum_empcs_cor.ddf" 
   exit 1
endif
if (! -e  ${twork}_lac_fbhsvdfcomb_sum_empcs_cor.ddf) then
   echo "can not find ${twork}_lac_fbhsvdfcomb_sum_empcs_cor.ddf" 
   exit 2
endif

if (! -e ${twork}_t1va_resampled.int2) then
   resample_image_spectra ${twork}_t1va ${twork}_lac_fbhsvdfcomb_sum_empcs_cor
endif
if (! -e ${tref}_t1va_resampled.int2) then
   resample_image_spectra ${tref}_t1va ${tref}_lac_fbhsvdfcomb_sum_empcs_cor
endif

if (! -e ${twork}_t1va_resampled_to_${tref}_t1va_resampled_transform.tfm) then
    align_tool -k BRAINS ${twork}_t1va_resampled ${tref}_t1va_resampled ${twork}_t1va_resampled_to_${tref}_t1va_resampled	
endif
cp ${twork}_t1va_resampled_to_${tref}_t1va_resampled_transform.tfm  brain_analysis_${twork}_${specroot}

cd brain_analysis_${twork}_${specroot}
cp ../brain_analysis_${tref}_${specroot}/${tref}_${specroot}_empcsahl_cmb_res_cho_naa.* .
set flist = `ls ${twork}*.real`
set n = 1

if (! -e ../brain_analysis_${twork}_${specroot}_to_${tref}_spec) then
     mkdir ../brain_analysis_${twork}_${specroot}_to_${tref}_spec
endif

foreach i ($flist)

	set tempf = $flist[1]
	set fname = `echo $tempf | cut -d"." -f1` 
	echo $n $fname

	if (! -e ${fname}_to_${tref}_spec.idf) then
	    align_tool -k BRAINS ${fname} ${tref}_${specroot}_empcsahl_cmb_res_cho_naa ${fname}_to_${tref}_spec -t ${twork}_t1va_resampled_to_${tref}_t1va_resampled_transform.tfm
	endif
		
	@ n++
	shift flist
	
end

mv -f *to_${tref}_spec.* ../brain_analysis_${twork}_${specroot}_to_${tref}_spec

