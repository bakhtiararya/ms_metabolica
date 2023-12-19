/bin/rm $1_?.*

mv $1_avg_1.cmplx $1_1.cmplx
mv $1_avg_2.cmplx $1_2.cmplx
mv $1_avg_3.cmplx $1_3.cmplx
mv $1_avg_4.cmplx $1_4.cmplx
mv $1_avg_5.cmplx $1_5.cmplx
mv $1_avg_6.cmplx $1_6.cmplx
mv $1_avg_7.cmplx $1_7.cmplx
mv $1_avg_8.cmplx $1_8.cmplx

mv $1_avg_1.ddf $1_1.ddf
cp $1_1.ddf $1_2.ddf
cp $1_1.ddf $1_3.ddf
cp $1_1.ddf $1_4.ddf
cp $1_1.ddf $1_5.ddf
cp $1_1.ddf $1_6.ddf
cp $1_1.ddf $1_7.ddf
cp $1_1.ddf $1_8.ddf

/home/liyan/script/TEavg7t/set_teavg7t.x $1_1 $1

process_spec_v6 -p $1.par $1_1.cmplx
process_spec_v6 -p $1.par $1_2.cmplx
process_spec_v6 -p $1.par $1_3.cmplx
process_spec_v6 -p $1.par $1_4.cmplx
process_spec_v6 -p $1.par $1_5.cmplx
process_spec_v6 -p $1.par $1_6.cmplx
process_spec_v6 -p $1.par $1_7.cmplx
process_spec_v6 -p $1.par $1_8.cmplx

