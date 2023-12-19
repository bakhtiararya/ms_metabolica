#!/bin/csh -f

# processing PET and SWI for HIV-MRI study
# 2017/06/14

# $Header: written by Yan Li 

set image = $1
set magn = $2

if (! -e HarvardOxford_analysis/) then
    ln -s ../t1analysis/HarvardOxford_analysis/
endif
    		
set atlasroi = `ls ./HarvardOxford_analysis/HO*.int2`
set natlasroi = `ls ./HarvardOxford_analysis/HO*.int2 | wc -l`

if (! -e HarvardOxford_analysis_QSM) then
    mkdir HarvardOxford_analysis_QSM
endif
if (! -e ${image}_to_${magn}.int2) then
	align_tool ${image} ${magn} ${image}_to_${magn}	
endif

set r = 1
while ($r <= ${natlasroi})
	set roi = `echo $atlasroi[$r] | cut -d"." -f1-2`
	set outputname = `echo $roi | cut -d"/" -f3`
	cd ../t1analysis/HarvardOxford_analysis/
	/home/liyan/script/cshellscript/resample_image_v5_mine.x $outputname int2 ${image} ${outputname}_t1v
	cd ../../qsmanalysis
	
	echo "  $r $roi ${outputname}_${magn}"
	if (! -e HarvardOxford_analysis_QSM/${outputname}_${magn}.int2) then 						
		align_tool ${roi}_t1v ${magn} ${outputname}_${magn} -t ${image}_to_${magn}_transform
		mv ${outputname}_${magn}.* HarvardOxford_analysis_QSM
	endif
	@ r++
end
	
cd ../t1analysis/HarvardOxford_analysis/
if (! -e temp_t1v) then
	mkdir temp_t1v
	mv *_t1v.* temp_t1v
endif
