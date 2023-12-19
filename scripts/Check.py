import pprint

class ddf_struct:

	def __init__(self, field_defs_structure):
		self.filename = "DEFAULT"
		for row in field_defs_structure:
			if (row[3] == "Array"):
				if not hasattr(self, row[2]):
					setattr(self, row[2], [])
			else:
				setattr(self, row[2], "DEFAULT")

	def __str__(self):
		print("\n --- ddf Properties --- \n")
		pprint.pprint(self.__dict__)
		return "\n --- End of ddf Properties --- "

def is_number(n):
	try:
		float(n)
	except ValueError:
		return False
	return True

def get_numbers(input_string):
	return [float(n) for n in input_string.split() if is_number(n)]

def get_words(input_string):
	return [w for w in input_string.split() if not is_number(w)]

field_defs = [ \
	    ['version',                      'flt',  'version'         , "Single Value"], \
	    ['object type',                  'str',  'object_type'     , "Single Value"], \
	    ['patient id',                   'str',  'patient_id'      , "Single Value"], \
	    ['patient name',                 'str',  'patient_name'    , "Single Value"], \
	    ['patient code',                 'str',  'patient_code'    , "Single Value"], \
	    ['date of birth',                'str',  'dob'             , "Single Value"], \
	    ['sex',                          'str',  'sex'             , "Single Value"], \
	    ['study id',                     'str',  'studyid'         , "Single Value"], \
		['study code',                   'str',  'study_code'      , "Single Value"], \
		['study date',                   'str',  'study_date'      , "Single Value"], \
		['accession number',             'str',  'accession_number', "Single Value"], \
		['root name',                    'str',  'root_name'       , "Single Value"], \
		['series number',                'int',  'series'          , "Single Value"], \
		['series description',           'str',  'series_description', "Single Value" ], \
		['comment',                      'str',  'comment'         , "Single Value"], \
		['patient entry',                'str',  'patient_entry'   , "Single Value"], \
		['patient position',             'str',  'patient_position', "Single Value"], \
		['orientation',                  'str',  'orientation'     , "Single Value"], \
		['data type',                    'str',  'data_type'       , "Single Value"], \
		['number of components',         'int',  'num_components'  , "Single Value"], \
		['source description',           'str',  'source_description', "Single Value"], \
		['number of dimensions',         'int',  'numdim'          , "Single Value"], \
		['dimension 1',                  'str',  'dimension_type'  , "Array"], \
		['dimension 2',                  'str',  'dimension_type'  , "Array"], \
		['dimension 3',                  'str',  'dimension_type'  , "Array"], \
		['dimension 4',                  'str',  'dimension_type'  , "Array"], \
		['center(lps, mm)',              'flt',  'center'          , "Single Value"], \
		['toplc(lps, mm)',               'flt',  'toplc'           , "Single Value"], \
		['dcos0',                        'flt',  'dcos0'           , "Single Value"], \
		['dcos1',                        'flt',  'dcos1'           , "Single Value"], \
		['dcos2',                        'flt',  'dcos2'           , "Single Value"], \
		['coil name',                    'str',  'coil_name'       , "Single Value"], \
		['slice gap(mm)',                'flt',  'slice_gap'       , "Single Value"], \
		['echo time(ms)',                'flt',  'TE'              , "Single Value"], \
		['repetition time(ms)',          'flt',  'TR'              , "Single Value"], \
		['inversion time(ms)',           'flt',  'TI'              , "Single Value"], \
		['flip angle',                   'flt',  'flip_angle'      , "Single Value"], \
		['pulse sequence name',          'str',  'sequence'        , "Single Value"], \
		['transmitter frequency(MHz)',   'flt',  'transmit_freq'   , "Single Value"], \
		['isotope',                      'str',  'isotope'         , "Single Value"], \
		['field strength(T)',            'flt',  'field_strength'  , "Single Value"], \
		['number of sat bands',          'int',  'num_sat_bands'   , "Single Value"], \
		['localization type',            'str',  'loc_type'        , "Single Value"], \
		['center frequency(MHz)',        'flt',  'centfreq'        , "Single Value"], \
		['ppm reference',                'flt',  'ppm_ref'         , "Single Value"], \
		['sweepwidth(Hz)',               'flt',  'sweepwidth'      , "Single Value"], \
		['dwelltime(ms)',                'flt',  'dwelltime'       , "Single Value"], \
		['frequency offset(Hz)',         'flt',  'freq_offset'     , "Single Value"], \
		['centered on water',            'str',  'center_on_water' , "Single Value"], \
		['suppression technique',        'str',  'suppresion_tech' , "Single Value"], \
		['residual water',               'str',  'residual_water'  , "Single Value"], \
		['number of acquisitions',       'int',  'num_acquisitions', "Single Value"], \
		['chop',                         'str',  'chop'            , "Single Value"], \
		['even symmetry',                'str',  'even_sym'        , "Single Value"], \
		['data reordered',               'str',  'data_reordered'  , "Single Value"], \
		['acq. toplc(lps, mm)',          'flt',  'acq_toplc'       , "Single Value"], \
		['acq. spacing(mm)',             'flt',  'acq_spacing'     , "Single Value"], \
		['acq. number of data points',   'int',  'acq_n_data_points', "Single Value"], \
		['acq. number of points',        'int',  'acq_n_points'    , "Single Value"], \
		['acq. dcos1',                   'flt',  'acq_dcos1'       , "Single Value"], \
		['acq. dcos2',                   'flt',  'acq_dcos2'       , "Single Value"], \
		['acq. dcos3',                   'flt',  'acq_dcos3'       , "Single Value"], \
		['selection center(lps, mm)',    'flt',  'box_center'      , "Single Value"], \
		['selection size(mm)',           'flt',  'box_size'        , "Single Value"], \
		['selection dcos1',              'flt',  'box_dcos1'       , "Single Value"], \
		['selection dcos2',              'flt',  'box_dcos2'       , "Single Value"], \
		['selection dcos3',              'flt',  'box_dcos3'       , "Single Value"] \
	]

extended_fields = [ \
	    ['npoints',                      'int_PASS',	'npix',					"Array"], \
	    ['pixel spacing(mm)',            'flt_PASS',	'pixel_spacing',		"Array"], \
	    ['sat band thickness',           'flt_PASS',  	'satband_thickness',	"Array"], \
	    ['sat band orientation',         'flt_PASS',  	'satband_orientation',	"Array"], \
	    ['sat band position',            'flt_PASS',  	'satband_position',		"Array"] \
	]

field_defs.extend(extended_fields)

field_dict = {"npoints":[], "pixel spacing(mm)":[], "sat band thickness": [], 
					"sat band orientation":[], "sat band position":[]}

with open("Testing 1 2 3.txt") as ddf_data_file:
	count_first_header = 0
	for line in ddf_data_file:

		if "DATA DESCRIPTOR FILE" in line:
			count_first_header += 1

		if count_first_header > 1:
			ddf_data_file.close()
			break;

		if ":" in line:
			line = line.rstrip()
			lst = line.split(": ", 1)
			num_lst = get_numbers(line)
			key = lst[0]
			val = "N/A"
			if(len(lst) != 1):
				val = lst[1]
			else:
				key = lst[0][:-1]
			field_dict[key] = val

		# hard Coded

		if "dimension" in line and "type" in line and "1:" not in line:
			field_dict["npoints"].append(num_lst[0])
			field_dict["pixel spacing(mm)"].append(num_lst[1])

		elif "sat band" in line:
			if "thickness" in line:
				field_dict["sat band thickness"].append(num_lst[1])
			elif "orientation" in line:
				field_dict["sat band orientation"].append(num_lst[1:])
			elif "position" in line:
				field_dict["sat band position"].append(num_lst[1:])

# For testing purposes
# pprint.pprint(field_dict)

ddf = ddf_struct(field_defs)

for row in field_defs:
	
	if row[0] not in field_dict.keys():
		raise RuntimeError("Unable to find field '" + row[0] + "' from the .ddf file")

	if isinstance(field_dict[row[0]], list):
		val_tokens = field_dict[row[0]]
	else:
		val_tokens = field_dict[row[0]].split()

	for i in range(0, len(val_tokens)):
		if val_tokens[i] != "N/A":
			if row[1] == "flt":
				val_tokens[i] = float(val_tokens[i])
			elif row[1] == "int":
				val_tokens[i] = int(float(val_tokens[i]))

	if(row[3] == "Single Value"):
		setattr(ddf, row[2], val_tokens[0])
	else:
		setattr(ddf, row[2], val_tokens)

"""
     For v6, we also read in all the other "stuff" that is tacked on to the end of the DDF.  
     This typically has information about all the processing that happened to be used to create 
     this file. Thus, it has no predefined form, so we just grab everything and dump it into a 
     giant string so we can write it back out or access it later, if required.
"""
separator = "==================================================="
ddf_data_file = open("Testing 1 2 3.txt", 'r')
text_info = ddf_data_file.read()
start_index = text_info.index(separator, 2) + len(separator)
ddf.misc_info = text_info[start_index:text_info.index(separator, start_index)]
ddf_data_file.close()

# ddf.read_in_time = datestr(clock,0);
# ddf.npix = ddf.npts; % For backwards compatibility!

# For backwards compatibility!
if (ddf.version >= 6):
  ddf.encode_fov = [a*b for a,b in zip(ddf.npix, ddf.pixel_spacing)]