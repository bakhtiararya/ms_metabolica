#!/bin/csh
#
#   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/MRS/trunk/mc_phase_spec/all_single_3T.x $
#   $Rev: 1545 $
#   $Author: jasonc $
#   $Date: 2008-04-01 21:35:32 -0700 (Tue, 01 Apr 2008) $
#


if ( $#argv != 4 ) then
    echo usage $0 root_in root_phased_out root_ac peak_root
    exit(1)
endif


set DEV=".dev"


cd single_coil

phase_spec_v6${DEV} << EOF
1 8 3
a
$1_1_phased.cmplx
$2_1
$1_2_phased.cmplx
$2_2
$1_3_phased.cmplx
$2_3
$1_4_phased.cmplx
$2_4
$1_5_phased.cmplx
$2_5
$1_6_phased.cmplx
$2_6
$1_7_phased.cmplx
$2_7
$1_8_phased.cmplx
$2_8
EOF

combine_spec_v6${DEV} << EOF
f
8
$2_1.cmplx
$3_calr1.real
$2_2.cmplx
$3_calr2.real
$2_3.cmplx
$3_calr3.real
$2_4.cmplx
$3_calr4.real
$2_5.cmplx
$3_calr5.real
$2_6.cmplx
$3_calr6.real
$2_7.cmplx
$3_calr7.real
$2_8.cmplx
$3_calr8.real
$2_comb
EOF
mv $2_comb.* ../.
cd ../

csi_image_v6${DEV}   << EOF
$2_comb.cmplx
s
r
2.5
$2_comb
$4.peak
21
61
0 5
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

csi_image_v6${DEV} << EOF
$2_comb_cor_sum.cmplx
s
t
$2_comb
$4.peak
21
61
0 5 
n
n
n
n
n
1 1 2 4
0 1 0
0 0 1 0
EOF
mv $2*0*.real $2_comb_cor_met/.
mv $2*0*.idf $2_comb_cor_met/.
mv $2*t.real $2_comb_cor_met/.
mv $2*t.idf $2_comb_cor_met/.
