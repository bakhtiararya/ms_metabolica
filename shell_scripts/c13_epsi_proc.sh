#!/bin/csh -f

# $Header: written by Yan Li 

# 2Ddyn EPSI processing

#set root = $1
#set chan = $2
#set timept = $3
#set phasecoil = $4
#set headmask = $5

set root = dynout
set chan = 8
set timept = 24
set phasecoil = 03
set headmask = t10776_brainmask_to_t2fse_c13mrsi_percent


cp /home/liyan/script/c13scripts/2d_epsi_c13.peak .

# processing the timepoint with highest pyruvate SNR
#/home/liyan/script/c13scripts/csir.x ${root}_phased_${c}_${phasecoil} ${root}_phased_${c}_${phasecoil} 2d_epsi_c13

set c = 1
while ($c <= ${chan})	

	if ((! -e ${root}_phased_${c}_${phasecoil}tph.real) | (! -e ${root}_phased_${c}_${phasecoil}tfr.real) | (! -e ${root}_phased_${c}_${phasecoil}th05.real)) then

		/home/liyan/script/c13scripts/csi.x ${root}_phased_${c}_${phasecoil} ${root}_phased_${c}_${phasecoil} 2d_epsi_c13 ${headmask} 21 50
		mv ${root}_phased_${c}_${phasecoil}*nsd* ${root}_phased_${c}_${phasecoil}_cor_met
		mv ${root}_phased_${c}_${phasecoil}*wn* ${root}_phased_${c}_${phasecoil}_cor_met
		mv ${root}_phased_${c}_${phasecoil}tph.* ${root}_phased_${c}_${phasecoil}_cor_met
		cp ${root}_phased_${c}_${phasecoil}_cor_met/${root}_phased_${c}_${phasecoil}tph.* .
		cp ${root}_phased_${c}_${phasecoil}_cor_met/${root}_phased_${c}_${phasecoil}tfr.* .
		cp ${root}_phased_${c}_${phasecoil}_cor_met/${root}_phased_${c}_${phasecoil}th05.* .
	endif
	@ c++
end

foreach broot (${root}_phased ${root}_bicarb_phased) 

	if (-e ${broot}_1_01.cmplx) then
	
		if (-e add_spec_c13_${broot}.x) then
			/bin/rm add_spec_c13_${broot}.x
		endif
		echo "add_spec_v6 << EOF" > add_spec_c13_${broot}.x
		echo "$timept" >> add_spec_c13_${broot}.x

		set t = 1
		while ($t <= $timept)
			if ($t < 10) then	
				set tpt = 0$t
			else
				set tpt = $t
			endif
	
			if (-e combine_c13_${broot}_$tpt.x) then
				/bin/rm combine_c13_${broot}_$tpt.x
			endif
	
			echo "combine_spec_v6.dev -s << EOF" > combine_c13_${broot}_$tpt.x
			echo "f" >> combine_c13_${broot}_$tpt.x
			echo "${chan}" >> combine_c13_${broot}_$tpt.x

			set c = 1
			while ($c <= ${chan})
	
				set fname = ${broot}_${c}_$tpt
				if (! -e ${fname}_correct.cmplx) then
					/home/liyan/script/c13scripts/fpcorrect_c13.x $fname ${root}_phased_${c}_${phasecoil}tfr ${root}_phased_${c}_${phasecoil}tph
				endif
				
				echo "${fname}_correct.cmplx" >> combine_c13_${broot}_$tpt.x
				echo "${root}_phased_${c}_${phasecoil}th05.real" >>  combine_c13_${broot}_$tpt.x
		
				@ c++
			end
	
			echo "${broot}_comb_c13_${tpt}_correct" >> combine_c13_${broot}_$tpt.x
			echo "EOF" >> combine_c13_${broot}_$tpt.x
	
			chmod 775 combine_c13_${broot}_$tpt.x
			combine_c13_${broot}_$tpt.x

			/home/liyan/script/c13scripts/csi_mask.x ${broot}_comb_c13_${tpt}_correct ${broot}_comb_c13_${tpt}_correct 2d_epsi_c13 ${headmask} 21 50
	
			echo "${broot}_comb_c13_${tpt}_correct.cmplx" >> add_spec_c13_${broot}.x
			echo "1" >> add_spec_c13_${broot}.x
	
			@ t++
		end

		echo "${broot}_comb_c13_sum$tpt" >> add_spec_c13_${broot}.x
		echo "EOF" >> add_spec_c13_${broot}.x

		chmod 775 add_spec_c13_${broot}.x
		# add_spec_c13_${broot}.x
	#	echo "/home/liyan/script/c13scripts/csi_mask.x ${broot}_comb_c13_sum$tpt ${broot}_comb_c13_sum$tpt 2d_epsi_c13 ${headmask} 21 50"
		
	endif
end