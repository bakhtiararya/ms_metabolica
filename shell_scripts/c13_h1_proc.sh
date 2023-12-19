#!/bin/csh -f

# $Header: written by Yan Li 

set projectpath = /home/liyan/projects/c13_h1_epsi
set processdate = `date +"%y%m%d"`
set outputroot = c13h1_epsi_datastatus_20${processdate}

if (-e ${projectpath}/${outputroot}.txt) then
	/bin/rm ${projectpath}/${outputroot}.txt
endif
if (-e ${projectpath}/${outputroot}.csv) then
	/bin/rm ${projectpath}/${outputroot}.csv
endif

if (-e ${projectpath}/${outputroot}.csv) then
	/bin/rm ${projectpath}/${outputroot}.csv
endif
echo "No, bnum, H-tnum, C-tnum, Vcel, Vt2all, C13 res" > ${projectpath}/${outputroot}.csv



# processing H-1 Data to the location of C-13 EPSI

# 2D CSI and 2D Dyn
set blist = (b4214 b3531 b4222 b2284 b4223 b1557 b3263 b446)
set tlist = (t10776 t10781 t10797 t10798 t10799 t11033 t11099 t11100 t11169 t11298)
# varied flip angle 2D Dyn
set blist = (b3996 b3776)
set tlist = (t10224 t10259)
# ALL EPSI dataset
set blist = (b4214 b3531 b4222 b2284 b4223 b1557 b3263 b446 b3996 b3776)
set tlist = (t10776 t10781 t10797 t10798 t10799 t11033 t11099 t11100 t11169 t11298 t10224 t10193)

set blist = (b4214 b3531 b2284 b4223 b3996 b3776)
set tlist = (t10776 t10781 t10798 t10799 t10224 t10193)


set pathroot = /data/bioe3/C13_analysis

set n = 1
foreach tnum ($tlist)
	foreach bnum ($blist)
		set datapath = ${pathroot}/${bnum}/${tnum}
		if (-e $datapath) then
			set outputstring = 
			set notnum = `echo $tnum | cut -c2-6`
			set examdate = `brain_db_exams -t $notnum | grep $tnum`
     		set examdate = `echo $examdate | cut -d" " -f3 | sed  's/-//g'` 
     		#for b3996 and b3776, H-1 and C13 were not acquired on the same day
            set examdateoff1 = 20160126
            set examdateoff2 = 20160115		
			foreach c13dir (c13_${examdate} c13_${examdate}_1 c13_${examdate}_2 c13_${examdateoff1} c13_${examdateoff2})
				if (-e ${pathroot}/${bnum}/${c13dir}) then
			#		echo $n $bnum $tnum $c13dir $examdate
			
					# H-1 to C-13 analysis 
					if ((-e ${pathroot}/${bnum}/c13_${examdate}) | (-e ${pathroot}/${bnum}/c13_${examdate}_1) | (-e ${pathroot}/${bnum}/c13_${examdate}_2))  then
						set newpath = ${tnum}_to_c13_${examdate}
					else
						set newpath = ${tnum}_to_${c13dir}
					endif				
					if (! -e ${pathroot}/${bnum}/${newpath}) then
						mkdir ${pathroot}/${bnum}/${newpath}
					endif	
					# Prepration steps for registering H-1 MRSI to C13 EPSI (next step: Matlab)		
					foreach c13acq (c13_2Ddyn c13_2Dcsi)
						if (-e ${pathroot}/${bnum}/${c13dir}/${c13acq}) then
							echo "$n $bnum $tnum $c13dir $c13acq"
						#	echo "$n $bnum $tnum $c13dir $c13acq" >> ${projectpath}/${outputroot}.txt
							set outputstring = `echo "$n,$bnum,$tnum,$c13dir"` 
							dcm_exam_info -t $notnum  >> ${projectpath}/${outputroot}.txt
							echo " " >> ${projectpath}/${outputroot}.txt
							# 2D dyn
						#	if (-e ${pathroot}/${bnum}/${c13dir}/c13_2Ddyn/spectra/ind_files/dynout_7_08_correct.ddf) then
						#		cd ${pathroot}/${bnum}/${c13dir}/c13_2Ddyn/spectra/ind_files/
						#		modify_ddf_4_13C.x dynout_7_08_correct h1_c13_${tnum}
						#		mv h1_c13_${tnum}.ddf ${pathroot}/${bnum}/${newpath}
						#		cp dynout_7_08_correct.cmplx ${pathroot}/${bnum}/${newpath}/h1_c13_${tnum}.cmplx
						#		cp dynout_7_08_correct.* ${pathroot}/${bnum}/${newpath}
						#	endif
							# 2D CSI
						#	if (-e ${pathroot}/${bnum}/${c13dir}/${c13acq}/spectra/2Dcsiout_new_8_cor.ddf) then
						#		cd ${pathroot}/${bnum}/${c13dir}/${c13acq}/spectra/
						#		modify_ddf_4_13C.x 2Dcsiout_new_8_cor h1_c13_${tnum}
						#		mv h1_c13_${tnum}.ddf ${pathroot}/${bnum}/${newpath}
						#		cp 2Dcsiout_new_8_cor.cmplx ${pathroot}/${bnum}/${newpath}/h1_c13_${tnum}.cmplx
						#		cp 2Dcsiout_new_8_cor.* ${pathroot}/${bnum}/${newpath}
						#	endif
							# varied flip angle dataset
						#	if (-e ${pathroot}/${bnum}/${c13dir}/c13_2Ddyn/spectra/ind_files/dynout_new_7_08_correct.ddf) then
						#		cd ${pathroot}/${bnum}/${c13dir}/c13_2Ddyn/spectra/ind_files/
						#		modify_ddf_4_13C.x dynout_7_08_correct h1_c13_${tnum}
						#		mv h1_c13_${tnum}.ddf ${pathroot}/${bnum}/${newpath}
						#		cp dynout_7_08_correct.cmplx ${pathroot}/${bnum}/${newpath}/h1_c13_${tnum}.cmplx
						#		cp dynout_7_08_correct.* ${pathroot}/${bnum}/${newpath}
						#	endif
						endif
					end
					
					# find Sarah's processing results
					if (-e ${pathroot}/${bnum}/${c13dir}/c13_2Ddyn) then
						cd ${pathroot}/${bnum}/${c13dir}/c13_2Ddyn
						if (! -e  ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output) then
							mkdir ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output
						endif
						# spectra data
						if (! -e spectra_original/dynoutb_phased_comb_c13_sum_correct_cor.cmplx) then
							echo " $bnum $c13dir can not find dynoutb_phased_comb_c13_sum_correct_cor.cmplx"
						else 
							cp spectra_original/dynoutb_phased_comb_c13_sum_correct_cor.* ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output
						endif
						if (! -e spectra_original/dynoutb_bicarb_phased_comb_c13_sum_correct_cor.cmplx) then
							echo " $bnum $c13dir can not find dynoutb_bicarb_phased_comb_c13_sum_correct_cor.cmplx"
						else
							cp spectra_original/dynoutb_bicarb_phased_comb_c13_sum_correct_cor.* ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output
						endif				
						# ratios
						if (! -e spectra_original/dynoutb_ratio_bp_phased.real) then
							echo " $bnum $c13dir can not find dynoutb_ratio_bp_phased.real"
						else
							cp spectra_original/dynoutb_ratio_bp_phased.* ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output
						endif
						if (! -e spectra_original/dynoutb_ratio_lp_phased.real) then
							echo " $bnum $c13dir can not find dynoutb_ratio_lp_phased.real"
						else
							cp spectra_original/dynoutb_ratio_lp_phased.* ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output
						endif
						# summed files
						if (! -e spectra_original/dynoutb_bicarb_phased_comb_c13_sum_brain_correctth02_scale.real) then
							echo " $bnum $c13dir can not find dynoutb_bicarb_phased_comb_c13_sum_brain_correctth02_scale.real"
						else
							cp spectra_original/dynoutb_bicarb_phased_comb_c13_sum_brain_correctth02_scale.* ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output
						endif
						if (! -e spectra_original/dynoutb_phased_comb_c13_sum_brain_correctth01_scale.real) then
							echo " $bnum $c13dir can not find dynoutb_phased_comb_c13_sum_brain_correctth01_scale.real"
						else
							cp spectra_original/dynoutb_phased_comb_c13_sum_brain_correctth01_scale.* ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output
						endif
						if (! -e spectra_original/dynoutb_phased_comb_c13_sum_brain_correctth05_scale.real) then
							echo " $bnum $c13dir can not find dynoutb_phased_comb_c13_sum_brain_correctth05_scale.real"
						else
							cp spectra_original/dynoutb_phased_comb_c13_sum_brain_correctth05_scale.* ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output
						endif						
					endif
					
					# C13 reprocessing
					set reprocessing = 0
					if ($reprocessing == 1) then								
						foreach c13acq (c13_2Ddyn c13_2Dcsi)
							if (-e ${pathroot}/${bnum}/${c13dir}/${c13acq}) then
								if (! -e ${pathroot}/${bnum}/${newpath}/${c13acq}) then
									mkdir ${pathroot}/${bnum}/${newpath}/${c13acq}
									if (-e ${pathroot}/${bnum}/${c13dir}/${c13acq}/2Dcsi) then
										cp ${pathroot}/${bnum}/${c13dir}/${c13acq}/2Dcsi ${pathroot}/${bnum}/${newpath}/${c13acq}
									else
										cp ${pathroot}/${bnum}/${c13dir}/${c13acq}/dyn?? ${pathroot}/${bnum}/${newpath}/${c13acq}
									endif
								endif
								cd ${pathroot}/${bnum}/${newpath}/
								if (-e c13_2Dcsi) then
									cd ${c13acq}
									if (! -e spectra) then
								# error when running process_fid_sym_epsi.x
								#		process_fid_sym_epsi.x 2dcsi 2Dcsiout
									endif							
								else		
									cd ${c13acq}						
									if (! -e spectra) then
										set npfile = `ls dyn* | wc -l`
										if ($npfile > 0) then
											set np = 1
											while ($np <= $npfile)
												if ($np < 10) then
													mv dyn0${np} P1110${np}.7
												else
													mv dyn${np} P111${np}.7
												endif
												@ np++
											end	
										else
											set npfile = `ls P111*.7 | wc -l`	
										endif										
										process_fid_sym_epsi.x -b -p 11101 dyn dynout $npfile
									endif
									set npfile = `ls dyn* | wc -l`
									echo "   ${c13acq} $npfile"		
								# reprocessing data to be finalized
							#		if () then
							#			cd ${pathroot}/${bnum}/${c13dir}/${c13acq}/spectra/ind_files
							#			set chan = 8
							#			set highcoil = 03
							#			set headmask = ${tnum}_brainmask_to_t2fse_c13mrsi_percent
							#			c13_epsi_proc.sh dynout $chan $npfile $highcoil $headmask
							#		endif
								endif
							endif
						end
					endif					
					
					# check H-1 MRSI processing
					if (! -e ${pathroot}/${bnum}/${tnum}/spectra_lac) then
						echo " no ${pathroot}/${bnum}/${tnum}/spectra_lac"
					endif		
					# Metabolite files alignment
					foreach dirtype (sum_empcs dif_empcs)
					
						cd ${pathroot}/${bnum}/${newpath}
						if (! -e ${tnum}_lac_fbhsvdfcomb_${dirtype}_cor_met) then
							echo "   copy ${tnum}_lac_fbhsvdfcomb_${dirtype}_cor_met"
							cp -r  ${pathroot}/${bnum}/${tnum}/spectra_lac/${tnum}_lac_fbhsvdfcomb_${dirtype}_cor_met .
						endif
						if (! -e ${tnum}_lac_fbhsvdfcomb_${dirtype}_cor_met_to_c13) then
							mkdir ${tnum}_lac_fbhsvdfcomb_${dirtype}_cor_met_to_c13
						endif
						
						cd ${tnum}_lac_fbhsvdfcomb_${dirtype}_cor_met
						# 1) copy fla images
						if (! -e ${tnum}_fla.int2) then 
							echo "  copy ${tnum}_fla.int2"
							cp ${pathroot}/${bnum}/${tnum}/images/${tnum}_fla.* .
						endif
						# 2) copy spectra files
						if (! -e ${tnum}_lac_fbhsvdfcomb_${dirtype}_cor.cmplx) then
							echo "   copy ${tnum}_lac_fbhsvdfcomb_${dirtype}_cor.cmplx"
							cp ../${tnum}_lac_fbhsvdfcomb_${dirtype}_cor.* .
						endif
						# 3) copy t2fse files
						if (! -e t2fse.int2) then
							echo "  copy t2fse.int2"
							cp ${pathroot}/${bnum}/${c13dir}/images/t2fse.* .
						endif
					end
					
					cd ${pathroot}/${bnum}/${newpath}/${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met
						# 4) generate sample_met_c13.real/.idf files
						#  	convert_ddf_idf_v6
						#		h1_c13_t10193_zeropad.ddf
						#		7
						#		n
						#		sample_met_c13   
						#	copy H1 real to sample_met_c13.real as a dummy file
					if (! -e sample_met_c13.idf) then
						echo "   generating sample_met_c13.idf"
						cd ../
						convert_ddfidf.x h1_c13_${tnum}.ddf sample_met_c13
						modify_idf_filetype.x sample_met_c13.idf 7
						cd ${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met
						cp ../sample_met_c13.idf .
					endif
					if (! -e sample_met_c13.real) then
						echo "   generating sample_met_c13.cmplx"
						cp ${tnum}_lac_fbhsvdfcomb_sum_empcsa03.real sample_met_c13.real
					endif					
					set nc13 = `ls ../${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met_to_c13/* | wc -l`
					if ($nc13 < 10) then
						echo "   align metablite files for sum metabolite files"
						met_h1_to_c13.x ${tnum}					
						mv -f *_to_c13.* ../${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met_to_c13	
					endif				
			#		svk_multi_view t2fse.idf ../${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met_to_c13/${tnum}_fla_resampled_to_c13.idf
					
					
					cd ${pathroot}/${bnum}/${newpath}/${tnum}_lac_fbhsvdfcomb_dif_empcs_cor_met
					if (! -e ${tnum}_fla_resampled_to_t2fse_transform.tfm) then
						cp ../${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met/${tnum}_fla_resampled_to_t2fse_transform.tfm .
					endif
					if (! -e sample_met_c13.real) then 
						cp ../${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met/sample_met_c13.* .
					endif					
					set nc13 = `ls ../${tnum}_lac_fbhsvdfcomb_dif_empcs_cor_met_to_c13/* | wc -l`
					if ($nc13 < 10) then
						echo "   align metablite files for dif metabolite files"
						met_h1_to_c13.x ${tnum}
						mv -f *_to_c13.* ../${tnum}_lac_fbhsvdfcomb_dif_empcs_cor_met_to_c13
					endif
					
					# H-1 ROI analysis (check existence and perform WM segmentation)
					if (! -e ${pathroot}/${bnum}/${tnum}/rois) then
						mkdir ${pathroot}/${bnum}/${tnum}/rois
					else
						set cel = 0
						set t2l = 0
						set wm = 0
						if (! -e ${pathroot}/${bnum}/${tnum}/rois/${tnum}_t2all.byt) then
							echo "   No T2all ROI"
						else
							set t2l = 1
						endif
						if (-e ${pathroot}/${bnum}/${tnum}/rois/${tnum}_cel.byt) then
				#			echo "   CEL exists"
							set cel = 1
						endif
						if (! -e ${pathroot}/${bnum}/${tnum}/rois/${tnum}_wm.byt) then
							if (! -e ${pathroot}/${bnum}/${tnum}/images/${tnum}_wm.idf) then
								echo "   no WM ROI"
								if (-e ${pathroot}/${bnum}/${tnum}/images/${tnum}_t1va.idf) then
						    		cd ${pathroot}/${bnum}/${tnum}
									echo "segment_wm.x ${tnum} t1va"
								else
									echo "   no t1va for WM segmentation"
								endif
							else
								cp ${pathroot}/${bnum}/${tnum}/images/${tnum}_wm.* ${pathroot}/${bnum}/${tnum}/rois/
								set wm = 1
							#	echo "   where is WM ROI"
							endif
						else
							set wm = 1
						endif			
						if (! -e ${pathroot}/${bnum}/${tnum}/rois/${tnum}_nawm.byt) then
							cd ${pathroot}/${bnum}/${tnum}/rois
							if (($wm == 1) & ($t2l == 1) & ($cel == 1)) then
								mask_math ${tnum}_wm -not ${tnum}_cel -not ${tnum}_t2all ${tnum}_nawm
							endif
							if (($wm == 1) & ($t2l == 1) & ($cel == 0)) then
								mask_math ${tnum}_wm -not ${tnum}_t2all ${tnum}_nawm
							endif
						endif	
					endif
					# align H-1 ROIs and brainmask to C-13 dimensions
					cd ${pathroot}/${bnum}/${newpath}/
					if (! -e rois) then
						mkdir rois
					endif
					cd rois
					if (! -e ${tnum}_brainmask.byt) then
						if (-e ${pathroot}/${bnum}/${tnum}/images/${tnum}_brainmask.byt) then
							cp ${pathroot}/${bnum}/${tnum}/images/${tnum}_brainmask.* .
						endif
					endif
					if (! -e ${tnum}_gm.byt) then
						if (-e ${pathroot}/${bnum}/${tnum}/images/${tnum}_t1va_gm.byt) then
							cp ${pathroot}/${bnum}/${tnum}/images/${tnum}_t1va_gm.idf ${tnum}_gm.idf
							cp ${pathroot}/${bnum}/${tnum}/images/${tnum}_t1va_gm.byt ${tnum}_gm.byt
							fix_rootname.x ${tnum}_gm
						endif
					endif
					if (! -e ${tnum}_csf.byt) then
						if (-e ${pathroot}/${bnum}/${tnum}/images/${tnum}_t1va_csf.byt) then
							cp ${pathroot}/${bnum}/${tnum}/images/${tnum}_t1va_csf.idf ${tnum}_csf.idf
							cp ${pathroot}/${bnum}/${tnum}/images/${tnum}_t1va_csf.byt ${tnum}_csf.byt
							fix_rootname.x ${tnum}_csf
						endif
					endif
					foreach rtype (cel t2all nawm wm brainmask gm csf)
						if ((-e ${pathroot}/${bnum}/${tnum}/rois/${tnum}_${rtype}.byt) | (-e ${tnum}_${rtype}.byt)) then
							echo "   align $rtype"
							if (! -e ${tnum}_${rtype}.byt) then
								cp ${pathroot}/${bnum}/${tnum}/rois/${tnum}_${rtype}.* .
							endif
							if (! -e ${tnum}_fla.int2) then 
								cp ${pathroot}/${bnum}/${tnum}/images/${tnum}_fla.* .
							endif
							if (! -e t2fse.int2) then
								cp ${pathroot}/${bnum}/${c13dir}/images/t2fse.* .
							endif
							if (! -e ${tnum}_fla_to_t2fse_transform.tfm) then
								align_tool.dev -k BRAINS ${tnum}_fla t2fse ${tnum}_fla_to_t2fse	
							endif
							if (! -e ${tnum}_${rtype}_to_t2fse.idf) then
								align_tool.dev -k BRAINS ${tnum}_${rtype} t2fse ${tnum}_${rtype}_to_t2fse -t ${tnum}_fla_to_t2fse_transform.tfm
							endif
					#		svk_multi_view t2fse.int2 ${tnum}_fla_to_t2fse.int2 ${tnum}_${rtype}_to_t2fse.idf
							if (! -e ${tnum}_lac_fbhsvdfcomb_sum_empcs_cor.idf ) then
								cd ../
								convert_ddfidf.x ${tnum}_lac_fbhsvdfcomb_sum_empcs_cor.ddf ${tnum}_lac_fbhsvdfcomb_sum_empcs_cor
								cd rois
								cp ../${tnum}_lac_fbhsvdfcomb_sum_empcs_cor.idf .
							endif
							if (! -e sample_met_c13.idf) then
								cp ../sample_met_c13.idf .
							endif
							if (! -e c13_mrsi.idf) then
								cd ../
								if (-e dynout_7_08_correct.ddf) then
									convert_ddfidf.x dynout_7_08_correct.ddf c13_mrsi
								endif
								if (-e 2Dcsiout_new_8_cor.ddf) then
									convert_ddfidf.x  2Dcsiout_new_8_cor.ddf c13_mrsi
								endif
								if (-e dynoutb_phased_comb_c13_10_correct_cor.ddf) then
									convert_ddfidf.x dynoutb_phased_comb_c13_10_correct_cor.ddf c13_mrsi
								endif
								if (-e dynout_new_3_08_correct.ddf) then
									convert_ddfidf.x dynout_new_3_08_correct.ddf c13_mrsi
								endif
								cd rois
								cp ../c13_mrsi.idf .
							endif
							if (! -e ${tnum}_${rtype}_h1mrsi_percent.idf) then
								percent_image.x ${tnum}_${rtype}.byt ${tnum}_lac_fbhsvdfcomb_sum_empcs_cor.idf ${tnum}_${rtype}_h1mrsi_percent
							endif
							if (! -e ${tnum}_${rtype}_to_t2fse_c13mrsi_percent.idf) then
								percent_image.x ${tnum}_${rtype}_to_t2fse.int2 sample_met_c13.idf ${tnum}_${rtype}_to_t2fse_h1mrsi_percent
							endif
							if (! -e  ${tnum}_${rtype}_to_t2fse_c13mrsi_percent.idf) then
								percent_image.x ${tnum}_${rtype}_to_t2fse.int2 c13_mrsi.idf ${tnum}_${rtype}_to_t2fse_c13mrsi_percent
							endif
						endif
					end
					cd ${pathroot}/${bnum}/${newpath}/rois
					if (-e ${tnum}_cel.byt) then
						if (! -e ${tnum}_fla_${tnum}_cel_params.txt) then
							get_mask_values ${tnum}_cel ${tnum}_fla
						endif
						set tempv = `grep "mask volume" ${tnum}_fla_${tnum}_cel_params.txt`
						set vol = `echo $tempv | cut -d" " -f3`
						set outputstring = `echo $outputstring,$vol`
					else
						set outputstring = `echo $outputstring,`
					endif
					if (! -e ${tnum}_fla_${tnum}_t2all_params.txt) then
						get_mask_values ${tnum}_t2all ${tnum}_fla
					endif
					set tempv = `grep "mask volume" ${tnum}_fla_${tnum}_t2all_params.txt`
					set vol = `echo $tempv | cut -d" " -f3`
					set pixelsize = `grep "pixelsize(mm)" c13_mrsi.idf | cut -d":" -f5`
					set outputstring = `echo $outputstring,$vol,$pixelsize`
					echo $outputstring >> ${projectpath}/${outputroot}.csv

					# convert 1H metabolites to C13 resolution for direct comparison
					if (-e ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output/dynoutb_ratio_lp_phased.idf) then
						cd ${pathroot}/${bnum}/${newpath}
						if (! -e brain_analysis_${tnum}_lac_fbhsvdfcomb) then
							echo "   copy brain_analysis_${tnum}_lac_fbhsvdfcomb"
							cp -r  ${pathroot}/${bnum}/${tnum}/brain_analysis_${tnum}_lac_fbhsvdfcomb .
						endif
						if (! -e brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13) then
							mkdir brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13
						endif
						cd 	brain_analysis_${tnum}_lac_fbhsvdfcomb
						if (! -e ${tnum}_fla_resampled_to_t2fse_transform.tfm) then
							cp ../${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met/${tnum}_fla_resampled_to_t2fse_transform.tfm .
						endif
						if (! -e sample_met_c13.real) then 
							cp ../${tnum}_lac_fbhsvdfcomb_sum_empcs_cor_met/sample_met_c13.* .
						endif						
						set flist = `ls ${tnum}*.real`
						set rf = 1
						set nc13 = `ls ../brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13/* | wc -l`
						if ($nc13 < 5) then
							echo "   align metablite files in brain_analysis_${tnum}_lac_fbhsvdfcomb"
							foreach i ($flist)
								set tempf = $flist[1]
								set fname = `echo $tempf | cut -d"." -f1` 						
								if ((! -e ${fname}_to_c13.real) & (! -e ../brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13/${fname}_to_c13.real))  then
									echo $rf $fname
									align_tool.dev -k BRAINS ${fname} sample_met_c13 ${fname}_to_c13 -t ${tnum}_fla_resampled_to_t2fse_transform.tfm				
								endif
								@ rf++
								shift flist
							end
							mv *_to_c13.* ../brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13					
						endif
					
						if (! -e ${pathroot}/${bnum}/${newpath}/brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13_mrsi) then
							mkdir ${pathroot}/${bnum}/${newpath}/brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13_mrsi
						endif
						cd ${pathroot}/${bnum}/${newpath}/brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13						
						if (! -e dynoutb_ratio_lp_phased.idf) then
							cp ${pathroot}/${bnum}/${newpath}/c13_2Ddyn/output/dynoutb_ratio_lp_phased.idf .
						endif
						set flist = `ls ${tnum}*_to_c13.real`
						set rf = 1
						set nc13 = `ls ../brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13_mrsi/* | wc -l`
						if ($nc13 < 5) then
							foreach i ($flist)
								set tempf = $flist[1]
								set fname = `echo $tempf | cut -d"." -f1` 
								if ((! -e ${fname}_mrsi.real) & (! -e ../brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13_mrsi/${fname}_mrsi.real)) then
									echo $rf $fname
									resample_image_v5_mine.x $fname real dynoutb_ratio_lp_phased ${fname}_mrsi
								endif
								@ rf++
								shift flist
							end
							mv *_to_c13_mrsi.* ../brain_analysis_${tnum}_lac_fbhsvdfcomb_to_c13_mrsi
						endif
						
					endif
					# ADC
					#cd ${pathroot}/${bnum}/${tnum}/
					#if (! -e diffusion_b=1000) then
					#	echo "   no diffusion"
					#endif
					
					@ n++
				endif
			end
		endif		
	end
	echo " "
end
	