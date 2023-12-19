csi_image_v6   << EOF
$1.cmplx
w
t10798_dynout_mrs_mask.real
0.8
t
$1fb
2d_epsi_c13.peak
1
21
0 5
n
p
25
n
n
f
$1fb_cor.cmplx
0 0 2 4
EOF

cp $1.ddf $1fb_cor.ddf
cp $1.ddf $1fb_cor_back.ddf
cp $1.ddf $1fb_cor_sum.ddf
mkdir $1fb_cor_met
mv $1fb*0*.real $1fb_cor_met/.
mv $1fb*0*.idf $1fb_cor_met/.
mv $1fb*tfr.real $1fb_cor_met/.
mv $1fb*tfr.idf $1fb_cor_met/.
mv $1fb*tph.real $1fb_cor_met/.
mv $1fb*tph.idf $1fb_cor_met/.
mv $1fb*tnsd.real $1fb_cor_met/.
mv $1fb*tnsd.idf $1fb_cor_met/.
mv $1fb*tpar.real $1fb_cor_met/.
mv $1fb*tpar.idf $1fb_cor_met/.
mv $1fb*trefh.idf $1fb_cor_met/.
mv $1fb*trefh.real $1fb_cor_met/.
mv $1fb*wn*.idf $1fb_cor_met/.
mv $1fb*wn*.real $1fb_cor_met/.
mv $1fb*.tab $1fb_cor_met/.

