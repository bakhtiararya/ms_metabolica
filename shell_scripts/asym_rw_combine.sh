#!/bin/csh -f

# $Header: written by Yan Li 

switch ($#argv)
	case 2
		set tnum = $1
		set spec = $2
	breaksw
	case 1
		set tnum = $1
		set spec = $2
	breaksw
	default: 
		echo "asym_rw_combine.sh water_spec_name combine_spec_name"
		exit 1
endsw
set chan = 32

set n = 1
while ($n <= $chan)
	cp ${tnum}_water_${n}_cor_met/${tnum}_water_${n}rh01.idf ${tnum}rw_cal_${n}.idf
	cp ${tnum}_water_${n}_cor_met/${tnum}_water_${n}rh01.real ${tnum}rw_cal_${n}.real
	fix_rootname.x ${tnum}rw_cal_${n}
	@ n++
end

combine32.x ${spec} cor_sum ${tnum}rw_cal cmb_mrs_met single
combine32.x ${tnum}_water cor_sum ${tnum}rw_cal cmb_mrs_met single

cp ${tnum}_water_comb_cor_sum.ddf ${spec}_comb_cor_sum_water.ddf
cp ${tnum}_water_comb_cor_sum.cmplx ${spec}_comb_cor_sum_water.cmplx

