function output = read_ddf_cmplx(rootname, displayflag)
% READ_DDF_IMAGE Reads an DDF file and associated data file
%
%   IMAGE_STRUCTURE = READ_DDF_IMAGE(ROOTNAME) reads two files for this
%   dataset.  First, it reads 'ROOTNAME.ddf' which gives it the associated
%   header information.  This DDF can be either an MRSC v3 or v5 file.  
%   A data file is then read; these are always .cmplx files, consisting of
%   a set of 32-bit float pairs representing real and imaginary parts
%   of each value.  The results are returned as a structure with two fields.
%   The first is IMAGE_STRUCTURE.DDF where DDF is itself a structure with
%   fields corresponding to data entries found in the IDF file.  The second
%   is a 3D array, where each element of the array is a structure with
%   real and complex fields.  IMAGE_STRUCTURE.IMG(I,J,K).REAL will give
%   all the real values for the voxel at coordinates (I,J,K).  
%
%   IMAGE_STRUCTURE = READ_DDF_IMAGE(ROOTNAME, DISPLAYFLAG) does the same
%   thing, but if DISPLAYFLAG is a 0, then it doesn't print out information
%   about what file it's opening.  This is useful in those cases when you
%   are trying to have a nice clean uncluttered screen.
%
%
%   See also READDDF_FILE, read_ddf_image
%
if (nargin < 1)
  help read_ddf_cmplx;
  error('Not enough input arguments --- must at least give rootname')
end

if (nargin < 2) displayflag = 1; end;

rootname = char(rootname);
unzipped_flag = 0;

if (displayflag == 1)
  disp(sprintf('\n  Reading DDF file:    %s.ddf',rootname));
end

output.ddf = readddf_file(rootname);
dynam_vol = output.ddf.npix(1)*output.ddf.npix(2)*output.ddf.npix(3)*output.ddf.specpoints*2;

datafilename = strcat(rootname,'.cmplx');

datafile = fopen(datafilename,'r','b');
if (datafile < 0) 
  unzipped_flag = 1;
  system(sprintf('gunzip %s.gz',datafilename));
  datafile = fopen(strcat(rootname,'.cmplx'),'r','b');  
  if (datafile < 0) 
    disp(sprintf('\n-- Error!  Data file %s not found! --\n',datafilename));
    return;
  end
end

if (displayflag == 1)
  disp(sprintf('  Reading data file:   %s',datafilename));
end

temp_data=fread(datafile, dynam_vol, 'float32');
real=reshape(temp_data(1:2:dynam_vol-1), output.ddf.specpoints, ...
	     output.ddf.npix(1), output.ddf.npix(2), output.ddf.npix(3));

imag=reshape(temp_data(2:2:dynam_vol), output.ddf.specpoints, ...
	     output.ddf.npix(1), output.ddf.npix(2), output.ddf.npix(3));


output.real = real;
output.imag = imag;

if (unzipped_flag == 1)
  system(sprintf('gzip %s', datafilename));
end

fclose(datafile);



