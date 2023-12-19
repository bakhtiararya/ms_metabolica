#!/bin/csh
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/MRS/trunk/mc_phase_spec/all_lac_3T.x $
#   $Rev: 1550 $
#   $Author: jasonc $
#   $Date: 2008-04-01 23:33:13 -0700 (Tue, 01 Apr 2008) $
#


if ( $#argv != 5 ) then
    echo usage $0 root_in root_sum root_dif root_ac peak_root
    exit(1)
endif


set DEV=".dev"

cd single_coil


#
# add and subtract cycles of spectral editing acquisition. 
#
mc_phase_spec -d -r $1 



phase_spec_v6${DEV} << EOF
2 8 3
a
sum_1_phased.cmplx
$2_1
sum_2_phased.cmplx
$2_2
sum_3_phased.cmplx
$2_3
sum_4_phased.cmplx
$2_4
sum_5_phased.cmplx
$2_5
sum_6_phased.cmplx
$2_6
sum_7_phased.cmplx
$2_7
sum_8_phased.cmplx
$2_8
dif_1_phased.cmplx
$3_1
dif_2_phased.cmplx
$3_2
dif_3_phased.cmplx
$3_3
dif_4_phased.cmplx
$3_4
dif_5_phased.cmplx
$3_5
dif_6_phased.cmplx
$3_6
dif_7_phased.cmplx
$3_7
dif_8_phased.cmplx
$3_8
EOF

combine_spec_v6${DEV} << EOF
f
8
$2_1.cmplx
$4_calr1.real
$2_2.cmplx
$4_calr2.real
$2_3.cmplx
$4_calr3.real
$2_4.cmplx
$4_calr4.real
$2_5.cmplx
$4_calr5.real
$2_6.cmplx
$4_calr6.real
$2_7.cmplx
$4_calr7.real
$2_8.cmplx
$4_calr8.real
$2_comb
EOF

combine_spec_v6${DEV} << EOF
f
8
$3_1.cmplx
$4_calr1.real
$3_2.cmplx
$4_calr2.real
$3_3.cmplx
$4_calr3.real
$3_4.cmplx
$4_calr4.real
$3_5.cmplx
$4_calr5.real
$3_6.cmplx
$4_calr6.real
$3_7.cmplx
$4_calr7.real
$3_8.cmplx
$4_calr8.real
$3_comb
EOF
mv $2_comb.* ../.
mv $3_comb.* ../.
cd ../

csi_image_v6${DEV}   << EOF
$2_comb.cmplx
s
r
2.5
$2_comb
$5.peak
21
61
0 4
s
p
p
35
n
p
18
f
$2_comb_cor.cmplx
1 1 2 4
0 1 0 0 0
0 0 1 0 0
EOF
mkdir $2_comb_cor_met
mv $2*0*.real $2_comb_cor_met/.
mv $2*0*.idf $2_comb_cor_met/.
mv $2*r.real $2_comb_cor_met/.
mv $2*r.idf $2_comb_cor_met/.

csi_image_v6${DEV}   << EOF
$3_comb.cmplx
s
r
2.5
$3_comb
$5.peak
21
61
0 5
f
n
$2_comb_cor_met/$2_combrfr.real
0
f
n
$2_combrph.real
f
$3_comb_cor.cmplx
0 0 2 4
EOF
mkdir $3_comb_cor_met
mv $3*0*.real $3_comb_cor_met/.
mv $3*0*.idf $3_comb_cor_met/.
mv $3*r.real $3_comb_cor_met/.
mv $3*r.idf $3_comb_cor_met/.
