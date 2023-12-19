addpath('/netopt/share/lib/local/brain/matlab/');

% data = read_ddf_image('/data/waubant1/7T_NAC_MS_GSH/subj01/2016_11_04/spectra_ACC_GSH_TE68/E3637_GSH_ACC_avg_dif_phased_phasebyw_cor_sum_comb_phased');
% imag_one_spectra = imag(data.img); 
% real_one_spectra = real(data.img); 
% mag_one_spectra = abs(data.img); 

data_file = read_ddf_image('/data/waubant1/7T_NAC_MS_GSH/subj01/2016_11_04/spectra_csi/E3637_csi_cor_sum_comb_phased');

col = 2;
row = 8;
slice = 5;

target_graph = data_file.img(:, col, row, slice);

imag_one_spectra = imag(target_graph); 
real_one_spectra = real(target_graph); 
mag_one_spectra = abs(target_graph); 

figure;
subplot(3,1,1);
x = 1:2048;
plot(x, imag_one_spectra);
title('Imaginary');

subplot(3,1,2);
plot(x, real_one_spectra);
title('Real');

subplot(3,1,3);
plot(x, mag_one_spectra);
title('Magnitude');