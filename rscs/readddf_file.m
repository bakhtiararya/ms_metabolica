function ddf = readddf_file(rootname)
%
%   READDDF_FILE Reads a DDF file (but not the complex file)
%
%   READDDF_FILE(ROOTNAME) reads in ROOTNAME.DDF and stores the
%   data as a Matlab structure.  This structure can be viewed easily
%   in Matlab, and can be passed to WRITEDDF_FILE or 
%   WRITE_DDF_IMAGE for automated writing to disk.  Works for v3, v5 or 
%   v6 style DDFs.
%
%   See also READDDF_FILE, WRITEDDF_FILE, WRITE_DDF_IMAGE.
%
%     Michael C. Lee, Ph.D.
%     Department of Radiology
%     University of California, San Francisco
%
%
%   Copyright (c) 2009 Regents of the University of California.
%   All rights reserved.  This software provided pursuant to a
%   license agreement containing restrictions on its disclosure,
%   duplication and use.  This notice must be embedded in or
%   attached to all copies, including partial copies, of the
%   software or any revisions or derivations thereof.
%
%   $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/libs/file_io/trunk/readddf_file.m $
%   $Rev: 14674 $
%   $Author: jasonc@RADIOLOGY.UCSF.EDU $
%   $Date: 2009-08-25 16:29:52 -0700 (Tue, 25 Aug 2009) $
%

%{ 
     input check
     throws an error if you have not input a rootname as the function input
%}
if (nargin == 0)
  error('You must specify the rootname as the input argument');
end

%{ 
     adds ".ddf" to the end of the rootname pathway 
     e.g --> DDFname = 'DDFname = 'C:\Users\Arya\Desktop\E3637_csi_cor_sum_comb_phased.ddf
%}
DDFname = strcat(rootname, '.ddf');

%{
     opens the binary data of the ddf file
     fopen returns a binary array; returns -1 if error 
     AMIT's worksheet
%}
fid = fopen(DDFname,'r','b');

if (fid < 0) 
  error('Unable to open specified file: %s', DDFname);
end

%{
     the ddf object is first being built; first attribute is the file name
     the ddf is NOT from memory 
%}
ddf.filename = DDFname;

v5a_field_defs = ...
    {'version',                       '%f',  inf, 'version'         , []  
     'study id:',                     '%c',  inf, 'studyid'         , []
     'study # :',                     '%c',  inf, 'studynum'        , []
     'position:',                     '%c',  inf, 'position'        , []
     'coil:',                         '%c',  inf, 'coil'            , []
     'series #:'                      '%d',  inf, 'series'          , []
     'orientation:'                   '%d',  inf, 'orientation'     , []
     'echo/time/met index:',          '%d',  inf, 'index'           , []
     'value:',                        '%f',  inf, 'value'           , []
     'name:',                         '%c',  inf, 'rootname'        , []
     'comment:',                      '%c',  inf, 'comment'         , []
     'sequence name:',                '%c',  inf, 'sequence'        , []
     'localization type:',            '%d',  inf, 'localizationtype', []
     ':',                             '%f',  inf, 'specfrequency'   , []
     'sweepwidth(Hz):',               '%f',  inf, 'sweepwidth'      , []
     'dwelltime:',                    '%f',  inf, 'dwelltime'       , []
     'satpulse pos(Hz):',             '%f',  inf, 'satpulsepos'     , []
     'bandwidth(Hz):',                '%f',  inf, 'bandwidth'       , []
     'beginning of acquisition (ms):','%f',  inf, 'acqbeginning'    , []
     'gradient on time (ms):',        '%f',  inf, 'gradontime'      , []
     'nex:',                          '%f',  inf, 'nex'             , []
     'chop:',                         '%f',  inf, 'chop'            , []
     'even_sym:',                     '%f',  inf, 'even_sym'        , []
     'pe_order:',                     '%f',  inf, 'pe_order'        , []
     'datatype:',                     '%d',  inf, 'datatype'        , []
     'number of dimensions:',         '%d',  inf, 'numdim'          , []
     'npts:',                         '%d',  inf, 'specpoints'      , []
     'acqpts:',                       '%d',  inf, 'acqspec'         , []
     'npts:',                         '%d',  inf, 'npix'            , 1
     'fov:',                          '%f',  inf, 'fov'             , 1
     'acqpts:',                       '%d',  inf, 'acqpts'          , 1     
     'npts:',                         '%d',  inf, 'npix'            , 2
     'fov:',                          '%f',  inf, 'fov'             , 2
     'acqpts:',                       '%d',  inf, 'acqpts'          , 2
     'npts:',                         '%d',  inf, 'npix'            , 3
     'fov:',                          '%f',  inf, 'fov'             , 3     
     'acqpts:',                       '%d',  inf, 'acqpts'          , 3     
     'center:',                       '%f',[1,3], 'recon_center'    , []
     'toplc:',                        '%f',[1,3], 'recon_toplc'     , []
     'dcos:',                         '%f',[1,3], 'recon_dcos1'     , []
     'dcos:',                         '%f',[1,3], 'recon_dcos2'     , []
     'dcos:',                         '%f',[1,3], 'recon_dcos3'     , []
     'pcenter:',                      '%f',[1,3], 'encode_center'   , []
     'pfov:',                         '%f',[1,3], 'encode_fov'      , []
     'pmatrix:',                      '%d',[1,3], 'encode_matrix'   , []
     'reverse:',                      '%d',[1,3], 'encode_reverse'  , []
     'pdcos:',                        '%f',[1,3], 'encode_dcos1'    , []
     'pdcos:',                        '%f',[1,3], 'encode_dcos2'    , []
     'pdcos:',                        '%f',[1,3], 'encode_dcos3'    , []
     'bcenter:',                      '%f',[1,3], 'box_center'      , []
     'bsize:',                        '%f',[1,3], 'box_size'        , []
     'bdcos:',                        '%f',[1,3], 'box_dcos1'       , []
     'bdcos:',                        '%f',[1,3], 'box_dcos2'       , []
     'bdcos:',                        '%f',[1,3], 'box_dcos3'       , []
     'refacq:',                       '%c',  inf, 'refacq'          , []
     'refrecon:',                     '%c',  inf, 'refrecon'        , []
    };

v5b_field_defs = ...
    {'version',                       '%f',  inf, 'version'         , []  
     'study id:',                     '%c',  inf, 'studyid'         , []
     'study # :',                     '%c',  inf, 'studynum'        , []
     'position:',                     '%c',  inf, 'position'        , []
     'coil:',                         '%c',  inf, 'coil'            , []
     'series #:'                      '%d',  inf, 'series'          , []
     'orientation:'                   '%d',  inf, 'orientation'     , []
     'echo/time/met index:',          '%d',  inf, 'index'           , []
     'value:',                        '%f',  inf, 'value'           , []
     'name:',                         '%c',  inf, 'rootname'        , []
     'comment:',                      '%c',  inf, 'comment'         , []
     'sequence name:',                '%c',  inf, 'sequence'        , []
     'localization type:',            '%d',  inf, 'localizationtype', []
     ':'             ,                '%f',  inf, 'specfrequency'   , []
     'sweepwidth(Hz):',               '%f',  inf, 'sweepwidth'      , []
     'dwelltime:',                    '%f',  inf, 'dwelltime'       , []
     'centfreq pos(Hz):',             '%f',  inf, 'centfreq'        , []
     'pulse type:',                   '%d',  inf, 'pulsetype'        , []
     'beginning of acquisition (ms):','%f',  inf, 'acqbeginning'    , []
     'gradient on time (ms):',        '%f',  inf, 'gradontime'      , []
     'nex:',                          '%f',  inf, 'nex'             , []
     'chop:',                         '%f',  inf, 'chop'            , []
     'even_sym:',                     '%f',  inf, 'even_sym'        , []
     'pe_order:',                     '%f',  inf, 'pe_order'        , []
     'datatype:',                     '%d',  inf, 'datatype'        , []
     'number of dimensions:',         '%d',  inf, 'numdim'          , []
     'npts:',                         '%d',  inf, 'specpoints'      , []
     'acqpts:',                       '%d',  inf, 'acqspec'         , []
     'npts:',                         '%d',  inf, 'npix'            , 1
     'fov:',                          '%f',  inf, 'fov'             , 1
     'acqpts:',                       '%d',  inf, 'acqpts'          , 1     
     'npts:',                         '%d',  inf, 'npix'            , 2
     'fov:',                          '%f',  inf, 'fov'             , 2
     'acqpts:',                       '%d',  inf, 'acqpts'          , 2
     'npts:',                         '%d',  inf, 'npix'            , 3
     'fov:',                          '%f',  inf, 'fov'             , 3     
     'acqpts:',                       '%d',  inf, 'acqpts'          , 3     
     'center:',                       '%f',[1,3], 'recon_center'    , []
     'toplc:',                        '%f',[1,3], 'recon_toplc'     , []
     'dcos:',                         '%f',[1,3], 'recon_dcos1'     , []
     'dcos:',                         '%f',[1,3], 'recon_dcos2'     , []
     'dcos:',                         '%f',[1,3], 'recon_dcos3'     , []
     'pcenter:',                      '%f',[1,3], 'encode_center'   , []
     'pfov:',                         '%f',[1,3], 'encode_fov'      , []
     'pmatrix:',                      '%d',[1,3], 'encode_matrix'   , []
     'reverse:',                      '%d',[1,3], 'encode_reverse'  , []
     'pdcos:',                        '%f',[1,3], 'encode_dcos1'    , []
     'pdcos:',                        '%f',[1,3], 'encode_dcos2'    , []
     'pdcos:',                        '%f',[1,3], 'encode_dcos3'    , []
     'bcenter:',                      '%f',[1,3], 'box_center'      , []
     'bsize:',                        '%f',[1,3], 'box_size'        , []
     'bdcos:',                        '%f',[1,3], 'box_dcos1'       , []
     'bdcos:',                        '%f',[1,3], 'box_dcos2'       , []
     'bdcos:',                        '%f',[1,3], 'box_dcos3'       , []
     'refacq:',                       '%c',  inf, 'refacq'          , []
     'refrecon:',                     '%c',  inf, 'refrecon'        , []
    };

v6_field_defs = ...
    {'version:',                      '%f',  inf, 'version'         , []
     'object type:',                  '%c',  inf, 'object_type'     , []
     'patient id:',                   '%c',  inf, 'patient_id'      , []
     'patient name:',                 '%c',  inf, 'patient_name'    , []
     'patient code:',                 '%c',  inf, 'patient_code'    , []
     'date of birth:',                '%c',  inf, 'dob'             , []
     'sex:',                          '%c',  inf, 'sex'             , []
     'study id:',                     '%c',  inf, 'studyid'         , []
     'study code:',                   '%c',  inf, 'study_code'      , []
     'study date:',                   '%c',  inf, 'study_date'      , []
     'accession number:',             '%c',  inf, 'accession_number', []
     'name:',                         '%c',  inf, 'root_name'       , []
     'series number:',                '%d',  inf, 'series'          , []
     'series description:'            '%c',  inf, 'series_description', []
     'comment:'                       '%c',  inf, 'comment'         , []
     'patient entry:',                '%c',  inf, 'patient_entry'   , []
     'patient position:',             '%c',  inf, 'patient_position', []
     'orientation:',                  '%c',  inf, 'orientation'     , []
     'data type:',                    '%c',  inf, 'data_type'       , []
     'number of components:',         '%d',  inf, 'num_components'  , []
     'source description:',           '%c',  inf, 'source_description', []
     'number of dimensions:',         '%d',  inf, 'numdim'          , []
     'type:',                         '%c',  inf, 'dimension_type'  , 1
     'npoints:',                      '%d',  inf, 'specpoints'      , []
     'type:',                         '%c',  inf, 'dimension_type'  , 2
     'npoints:',                      '%d',  inf, 'npix'            , 1
     'pixel spacing(mm):',            '%f',  inf, 'pixel_spacing'   , 1     
     'type:',                         '%c',  inf, 'dimension_type'  , 3
     'npoints:',                      '%d',  inf, 'npix'            , 2
     'pixel spacing(mm):',            '%f',  inf, 'pixel_spacing'   , 2     
     'type:',                         '%c',  inf, 'dimension_type'  , 4
     'npoints:',                      '%d',  inf, 'npix'            , 3
     'pixel spacing(mm):',            '%f',  inf, 'pixel_spacing'   , 3 
     'center(lps, mm):',              '%f',[1,3], 'center'          , []
     'toplc(lps, mm):',               '%f',[1,3], 'toplc'           , []
     'dcos0:',                        '%f',[1,3], 'dcos0'           , []
     'dcos1:',                        '%f',[1,3], 'dcos1'           , []
     'dcos2:',                        '%f',[1,3], 'dcos2'           , []
     'coil name:',                    '%c',  inf, 'coil_name'       , []
     'slice gap(mm):',                '%f',  inf, 'slice_gap'       , []
     'echo time(ms):',                '%f',  inf, 'TE'              , []
     'repetition time(ms):',          '%f',  inf, 'TR'              , []     
     'inversion time(ms):',           '%f',  inf, 'TI'              , []
     'flip angle:',                   '%f',  inf, 'flip_angle'      , []
     'pulse sequence name:',          '%c',  inf, 'sequence'        , []
     'transmitter frequency(MHz):',   '%f',  inf, 'transmit_freq'   , []
     'isotope:',                      '%c',  inf, 'isotope'         , []
     'field strength(T):',            '%f',  inf, 'field_strength'  , []
     'number of sat bands:',          '%d',  inf, 'num_sat_bands'   , []
     'localization type:',            '%c',  inf, 'loc_type'        , []
     'center frequency(MHz):',        '%f',  inf, 'centfreq'        , []
     'ppm reference:',                '%f',  inf, 'ppm_ref'         , []
     'sweepwidth(Hz):',               '%f',  inf, 'sweepwidth'      , []
     'dwelltime(ms):',                '%f',  inf, 'dwelltime'       , []
     'frequency offset(Hz):',         '%f',  inf, 'freq_offset'     , []
     'centered on water:',            '%c',  inf, 'center_on_water' , []
     'suppression technique:',        '%c',  inf, 'suppresion_tech' , []
     'residual water:',               '%c',  inf, 'residual_water'  , []
     'number of acquisitions:',       '%d',  inf, 'num_acquisitions', []
     'chop:',                         '%c',  inf, 'chop'            , []
     'even symmetry:',                '%c',  inf, 'even_sym'        , []
     'data reordered:',               '%c',  inf, 'data_reordered'  , []
     'acq. toplc(lps, mm):',          '%f',[1,3], 'acq_toplc'       , []
     'acq. spacing(mm):',             '%f',[1,3], 'acq_spacing'     , []
     'acq. number of data points:',   '%d',  inf, 'acq_n_data_points'   , []
     'acq. number of points:',        '%d',[1,3], 'acq_n_points'    , []
     'acq. dcos1:',                   '%f',[1,3], 'acq_dcos1'       , []
     'acq. dcos2:',                   '%f',[1,3], 'acq_dcos2'       , []
     'acq. dcos3:',                   '%f',[1,3], 'acq_dcos3'       , []
     'selection center(lps, mm):',    '%f',[1,3], 'box_center'      , []     
     'selection size(mm):',           '%f',[1,3], 'box_size'        , []
     'selection dcos1:',              '%f',[1,3], 'box_dcos1'       , []
     'selection dcos2:',              '%f',[1,3], 'box_dcos2'       , []
     'selection dcos3:',              '%f',[1,3], 'box_dcos3'       , []
    };

v6p1_field_defs = cat(1, v6_field_defs, ...
    {
     'reordered toplc(lps, mm):',     '%f',[1,3], 'reordered_toplc'      , []
     'reordered center(lps, mm):',    '%f',[1,3], 'reordered_center'     , []
     'reordered spacing(mm):',        '%f',[1,3], 'reordered_spacing'    , []
     'reordered number of points:',   '%d',[1,3], 'reordered_n_points'   , []
     'reordered dcos1:',              '%f',[1,3], 'reordered_dcos1'      , []
     'reordered dcos2:',              '%f',[1,3], 'reordered_dcos2'      , []
     'reordered dcos3:',              '%f',[1,3], 'reordered_dcos3'      , []
    });

%{
     converting a binary buffer into a character array (1010101 -> /data...) 
     closes the file after it is finish reading 
%}
entire_file = fscanf(fid,'%c'); 
fclose(fid);

%{
     Find the version number through a really...bad way...of finding it
     strfind returns an array of the starting index for all of the occurances of the specified word
     sscanf looks for the first float value 
     version: 6.1
%}

% First thing to do is find the version number
version = sscanf(entire_file(strfind(entire_file, 'version')+8:end), '%f');

%{
     checks for version input for attributes 
     checking for version or not valid input 
%}
if (version == 3)  % Convert to v5   
  temp_input_name = sprintf('/tmp/read_ddf_input_%010d.txt',sum(clock));
  temp_ddf_name   = sprintf('/tmp/read_ddf_v5_%010d',sum(clock));
  temp_input = fopen(temp_input_name,'w');
  fprintf(temp_input, '%s.ddf\n%s\n', rootname, temp_ddf_name);
  fclose(temp_input);
  system(sprintf('convert_ddf_v5 < %s > /dev/null', temp_input_name));
  delete(temp_input_name);  
  ddf = readddf_file(temp_ddf_name);
  ddf.filename = strcat(DDFname);
  delete(strcat(temp_ddf_name,'.ddf')); 
  return;
elseif (abs(version - 5) < 0.5) 
  if (~isempty(strfind(entire_file,'satpulse')))
    field_defs = v5a_field_defs;
  else
    field_defs = v5b_field_defs;
  end
elseif (version == 6)
  field_defs = v6_field_defs;
elseif (version == 6.1)
  field_defs = v6p1_field_defs;
else
  error('Sorry, ddf version %g is not supported\n', version);
end

% number_of_fields is the number of rows in the entire struct
number_of_fields = size(field_defs,1);

location_end = 1; 

% =======================================================================
% Begin reading the actual data
% =======================================================================

for (fieldnum = 1:number_of_fields)

  %{
     The data is located between this field name and the next field name:
     the fields in 'field_defs' are given in order, so only have to look
     in a small region to find the field we want.  This is important
     since the DDF has a lot of other information about the
     processing at the end of the DDF ... consequently, there may be
     multiple instances of fields ... for example it may specify
     'dcos' 3 or 4 times within a given DDF file, but we only want
     to read in a specific instance of this.
  %}
  
  %{ 
     location_start returns beginning index position of the a specific category/field VALUE (as seen in the header) in the .ddf file

     field_defs{fieldnum,1} - returns specific category/field vairable shown in the header 
     strfind(entire_file(location_end:end), field_defs{fieldnum,1}) - returns an index array of all instances of desired phrase
     min(strfind(entire_file(location_end:end), field_defs{fieldnum,1})) - returns first instance (smallest index) of desired phrase
     length(field_defs{fieldnum,1}) - returns string length of specific category/field vairable shown in the header

     e.g.
     ...
     version: 6.1
     object type: MR Spectroscopy
     patient id: 32883940
     patient name: CHAMBERLAIN CLAUDIA
     patient code: 
     date of birth: 04/28/1967
     ...

     For "version:" (field_defs(1,1)), location_start returns 32 (beginning index of "6.1 ...")
   %}
  location_start = ...
      min(strfind(entire_file(location_end:end), field_defs{fieldnum,1})) + length(field_defs{fieldnum,1}) + location_end;
  
  % an error is reported when the value of a specific category/field vairable cannot be found in the .ddf file    
  if (isempty(location_start))
    error('Unable to find field "%s" in file "%s"', ...
          field_defs{fieldnum,1}(1:end-1), DDFname);
  end
  
  %{ 
     location_end is being changed to 

     entire_file(location_start:end) - returns string of remaining .ddf file starting from the specific category/field VALUE
     field_defs{fieldnum + 1, 1} - returns specific category/field of the NEXT row
     strfind(entire_file(location_start:end), field_defs{fieldnum + 1, 1}) - returns an index array of all instances of desired phrase
     min(strfind(entire_file(location_start:end), field_defs{fieldnum + 1, 1})) - returns first instance (smallest index) of desired phrase

     e.g.
     6.1
     object type: MR Spectroscopy
     patient id: 32883940
     patient name: CHAMBERLAIN CLAUDIA
     patient code: 
     date of birth: 04/28/1967
     ...

     For "version:" , (field_defs(1,1)), location_end is being changed to 37. entire_file(32:37) is "6.1 o"
  %} 
  if (fieldnum ~= number_of_fields)  
    location_end = min(strfind(entire_file(location_start:end), field_defs{fieldnum + 1, 1})) - 1 + location_start;
  else
    location_end = length(entire_file)+1;
  end
  
  % field_name is the name category/field without the ":"
  % e.g. "version"
  field_name  = field_defs{fieldnum,4};  
  
  %{
     Assigning field_value to the value of the specific category/field of current row in iteration
     sscanf returns formatted data from string (str, formatSpec, sizeA)

     Note: string contained unnecssary end characters from the previous part to account for that fact that slicing does
     not include end characters

     location_start:location_end-1 - interval of region of value of the specific category/field in .ddf file INCLUDING a SPACE
     entire_file(location_start:location_end-1) - returns 
     field_defs{fieldnum,2} - 2nd column formatSpec (e.g %f, %c, %d ... etc)
     field_defs{fieldnum,3} - 3rd column sizeA (e.g inf or [1,3])

     e.g.
     For "version:" , field_value returns 6.1000
  %}
  field_value = sscanf(entire_file(location_start:location_end-1), field_defs{fieldnum,2}, field_defs{fieldnum,3});

  % Clean up the data, in the case of strings
  % NOTE: this utility code is needed for strings with \n due to the way the field_value was found in the previous part
  if (isstr(field_value))
    field_value = trimWhitespace(field_value);  
    if (isempty(field_value))
      field_value = '';
    end
  end

  %{ 
     Assign the data into the structure
  
     looks at the 5th column in field for instruction regarding the index ([] or Integer)

     case []: just assign value to specified field of ddf

     case Integer: add assign value to specified field ARRAY of ddf
          check to see if the array field exists for ddf, if not create empty array
          Numerical values (arrays) and Strings (cells)
          add/update field to the ddf
  %}
  array_index = field_defs{fieldnum,5};

  if (isempty(array_index))
    ddf = setfield(ddf, field_name, field_value);
  else
    if (isfield(ddf, field_name))
      temp_value = getfield(ddf, field_name);
    else
      temp_value = [];    
    end
    if (isstr(field_value)) 
      temp_value{array_index} = field_value;
    else
      temp_value(array_index) = field_value;      
    end
    ddf = setfield(ddf, field_name, temp_value);
  end

end

if (version >= 6)

  %{ 
     For v6 data, we read in the sat band information. We weren't able to do this beforehand, 
     because the number of sat bands was not determined until we've read in the bulk of the 
     DDF file. num_sat_bands is shown in the .ddf file
  %}
  
  % loop through each of n sat bands 
  for (satnum = 1:ddf.num_sat_bands)
    
    %{ 
       Obtain thickness(mm) of sat band n by slicing text region between end of "thickness(mm):" and before "orientation:"

       Find the location of the line "sat band n thickness(mm):" + length of the string itself
       Find the location of the line "sat band n orientation:" 
    %}
    location_start = min(strfind(entire_file, sprintf('sat band %d thickness(mm):', satnum))) + length(sprintf('sat band %d thickness(mm):', satnum));
    location_end = min(strfind(entire_file, sprintf('sat band %d orientation:',satnum))) - 1;
    ddf.satband_thickness(satnum,1) = sscanf(entire_file(location_start:location_end), '%f', satnum);
    
    %{ 
       Obtain orientation of sat band n by slicing text region between end of "orientation:" and before "position(lps, mm):"

       Find the location of the line "sat band n orientation:" + length of the string itself
       Find the location of the line "sat band n position(lps, mm):" 
    %}
    location_start = min(strfind(entire_file, sprintf('sat band %d orientation:', satnum))) + length(sprintf('sat band %d orientation:',satnum));
    location_end = min(strfind(entire_file, sprintf('sat band %d position(lps, mm):', satnum))) - 1;
    ddf.satband_orientation(satnum,:) = sscanf(entire_file(location_start:location_end), '%f', [1,3]);
    
    %{
       Obtain position(lps, mm) of sat band by finding position of 

       Find the location of the line "sat band %d position(lps, mm):" + length of the string itself
       Get length of the rest of the file

       sscanf returns formatted data from string (str, formatSpec, sizeA)

       Note: sscanf(entire_file(location_start:location_end), '%f') returns [1x3] of the numerical values. 
             sscanf ignores anything past \n

       e.g
          x = "3.33 4.565 0.78374 \n 0.874875";
          y = sscanf(x, '%f', [1,3]);

          y =

              3.3300    4.5650    0.7837
    %}
    location_start = min(strfind(entire_file, sprintf('sat band %d position(lps, mm):', satnum))) + length(sprintf('sat band %d position(lps, mm):',satnum));
    location_end = length(entire_file);
    ddf.satband_position(satnum,:) = sscanf(entire_file(location_start:location_end), '%f', [1,3]);  
  
  end

  %{ 
     For v6, we also read in all the other "stuff" that is tacked on to the end of the DDF.  
     This typically has information about all the processing that happened to be used to create 
     this file. Thus, it has no predefined form, so we just grab everything and dump it into a 
     giant string so we can write it back out or access it later, if required.
  %}
  separator = '===================================================';
  locations = strfind(entire_file, separator)+length(separator)+1;
  
  if (length(locations) >= 3)
    ddf.misc_info = entire_file(locations(3):end);
  else
    ddf.misc_info = [];
  end
end

% ddf.read_in_time = datestr(clock,0);
% ddf.npix = ddf.npts; % For backwards compatibility!
if (ddf.version >= 6)
  ddf.encode_fov = ddf.npix .* ddf.pixel_spacing;   % For backwards compatibility!
end


% ====================================

function input_string = trimWhitespace(input_string)

if (~isempty(input_string))
  first_newline = min(find(input_string == sprintf('\n')));
  if (~isempty(first_newline))
    input_string = input_string(1:first_newline-1);
  end
end

if (~isempty(input_string))
  while (input_string(end) == sprintf('\n') | input_string(end) == ' ')
    input_string = input_string(1:end-1);
    if (isempty(input_string)) 
      break;
    end
  end
end

if (~isempty(input_string))
  while (input_string(1) == sprintf('\n') | input_string(1) == ' ')
    input_string = input_string(2:end);
    if (isempty(input_string)) 
      break;
    end
  end
end