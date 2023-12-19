
% SIVIC - pathways
% matlab_folder_support = '/netopt/share/lib/local/brain/matlab/';
% patient_spectra_file = '/data/waubant1/7T_NAC_MS_GSH/subj01/2016_11_04/spectra_csi/E3637_csi_cor_sum_comb_phased'

matlab_folder_support = 'Brain/matlab/';
patient_spectra_file = 'spectra_csi/E3637_csi_cor_sum_comb_phased';

addpath(matlab_folder_support);
data_file = read_ddf_image(patient_spectra_file);

addpath('/netopt/share/lib/local/brain/matlab/');
data_file = read_ddf_image('/data/waubant1/7T_NAC_MS_GSH/subj01/2016_11_04/spectra_csi/E3637_csi_cor_sum_comb_phased');


% the default range of the ppm shown in the NMR graph.
% 2048 data points are collected from the NMR 
default_start = 7.85;
default_end = 1.42;
num_steps = 2048;

% generating array of all the ppm x-value data points 
x = linspace(default_start, default_end, num_steps);

% user start and end x-axis range for desired ppm region
xaxis_start_value = 3.40;
xaxis_end_value = 1.86;

% index values of the start and end X-values in the x array
xaxis_start_value_index = -1;
xaxis_end_value_index = -1;

% looping through the x array to get the index of the cloest value to the desired xaxis_start_value
for i = 1:1:size(x, 2)
	if abs(x(i) - xaxis_start_value) <= 0.01
		xaxis_start_value_index = i;
		break;
	end
end

% looping through the x array to get the index of the cloest value to the desired xaxis_end_value
for i = 1:1:size(x, 2)
	if abs(x(i) - xaxis_end_value) <= 0.01
		xaxis_end_value_index = i;
		break;
	end
end

% the desired start and end value of the x-axis will correspond to the range of y-values
yaxis_start_value_index = xaxis_start_value_index;
yaxis_end_value_index = xaxis_end_value_index;

% slice x-axis array to get new x-axis data points in the desired range 
x = x(xaxis_start_value_index:xaxis_end_value_index);


figure;
title('Six Chemical Peak Distributions (Magnitude)');
xlabel('Chemical Shift (ppm)') 
ylabel('Strength')
grid on;
hold on;

%%%%%%%%%%%%
% TARGET 1 %
%%%%%%%%%%%%
col = 9;
row = 9;
slice = 4;
target_graph = data_file.img(:, col, row, slice);
mag_one_spectra = abs(target_graph); 
mag_one_spectra = mag_one_spectra(yaxis_start_value_index:yaxis_end_value_index);
plot(x, mag_one_spectra);


set(gca, 'XDir','reverse');

hold on; 

%{

%%%%%%%%%%%%
% TARGET 2 %
%%%%%%%%%%%%
col = 10;
row = 9;
slice = 4;
target_graph = data_file.img(:, col, row, slice);
mag_one_spectra = abs(target_graph); 
plot(x, mag_one_spectra);
hold on; 

%%%%%%%%%%%%
% TARGET 3 %
%%%%%%%%%%%%
col = 11;
row = 9;
slice = 4;
target_graph = data_file.img(:, col, row, slice);
mag_one_spectra = abs(target_graph); 
plot(x, mag_one_spectra);
hold on; 

%%%%%%%%%%%%
% TARGET 4 %
%%%%%%%%%%%%
col = 10;
row = 9;
slice = 4;
target_graph = data_file.img(:, col, row, slice);
mag_one_spectra = abs(target_graph); 
plot(x, mag_one_spectra);
hold on;

%%%%%%%%%%%%
% TARGET 5 %
%%%%%%%%%%%%
col = 10;
row = 10;
slice = 4;
target_graph = data_file.img(:, col, row, slice);
mag_one_spectra = abs(target_graph); 
plot(x, mag_one_spectra);
hold on; 

%%%%%%%%%%%%
% TARGET 6 %
%%%%%%%%%%%%
col = 10;
row = 11;
slice = 4;
target_graph = data_file.img(:, col, row, slice);
mag_one_spectra = abs(target_graph); 
plot(x, mag_one_spectra);
hold on;

legend('Target 1', 'Target 2', 'Target 3', 'Target 4', 'Target 5', 'Target 6'); 

%}

% Reverse X Axis 
set(gca, 'XDir','reverse')