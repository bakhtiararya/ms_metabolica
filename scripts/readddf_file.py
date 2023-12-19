# -----------------------------------------------------------------------------
# Name:       readddf_file.py
# Purpose:    Constructs a ddf object given a .ddf file with spectra info
#
# Author:      Arya Haghighi
# Date:        06/17/2019
# -----------------------------------------------------------------------------
'''
a python method that constructs a ddf object with various attributes regarding
spectra image

The method takes a .ddf file and opens it to read the content inside. The
information inside of the file is then translated into a dictionary, where the
the dictionary is used to build a object containing various attributes. 
'''

import math
import time
import datetime
import pprint
import subprocess
import sys
import os
from os import path

def readddf_file(rootname):
	"""
	a method that reads a .ddf file and constructs a ddf object based on information
	provided by the file

	Arguments:
	rootname (string) -- name of the file that is being used to read the spectra data
	"""
	DDFname = rootname + ".ddf"

	field_dict = {"npoints":[], "specpoints": 0, "pixel spacing(mm)":[], "sat band thickness": [], 
		"sat band orientation":[], "sat band position":[]}

	if not os.path.exists(DDFname):
		raise RuntimeError("Unable to open specified file " + DDFname)

	with open(DDFname) as ddf_data_file:
		count_first_header = 0
		for line in ddf_data_file:

			if "DATA DESCRIPTOR FILE" in line:
				count_first_header += 1

			# termination/base case
			if count_first_header > 1:
				ddf_data_file.close()
				break

			# single line data case
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

			# --- Hard Coded Portion ---

			# Dimension data (dimension n: type: XYZ npoints: ## pixel spacing(mm): ##.####)
			if "dimension" in line and "type" in line:
				if "1:" in line:
					field_dict["specpoints"] = str(num_lst[0])
				else:
					field_dict["npoints"].append(num_lst[0])
					field_dict["pixel spacing(mm)"].append(num_lst[1])


			# Sat band Data
			elif "sat band" in line:
				if "thickness" in line:
					field_dict["sat band thickness"].append(num_lst[1])
				elif "orientation" in line:
					field_dict["sat band orientation"].append(num_lst[1:])
				elif "position" in line:
					field_dict["sat band position"].append(num_lst[1:])

	# --- For testing purposes ONLY ---
	# pprint.pprint(field_dict)
	
	if "version" not in field_dict.keys():
	   raise RuntimeError("Could not find Version of .ddf file")
	version = float(field_dict["version"]) 

	if (version == 3):
		time_stamp = datetime.datetime.now().strftime('%Y-%m-int-%H-%M-%S')
		temp_input_name = '/tmp/read_ddf_input_'+ time_stamp + '.txt'
		temp_ddf_name   = '/tmp/read_ddf_v5_' + time_stamp
		temp_input = open(temp_input_name,'w')
		temp_input.write(rootname + ".ddf\n" + temp_ddf_name + "\n")
		temp_input.close()
		os.system("convert_ddf_v5 < " + temp_input_name + " > /dev/null")
		os.remove(temp_input_name)
		ddf = readddf_file(temp_ddf_name)
		ddf.filename = DDFname
		os.remove(temp_ddf_name + '.ddf')
	elif (abs(version - 5) < 0.5):
		if "satpulse pos(Hz)" in field_dict.keys():
			field_defs = v5a_field_defs
		else:
			field_defs = v5b_field_defs
	elif (version == 6):
		field_defs = v6_field_defs
	elif (version == 6.1):
		field_defs = v6p1_field_defs
	else:   
		raise RuntimeError("Sorry, ddf version " + version + " is not supported\n")

	# --- ddf object construction --- 

	ddf = ddf_struct(field_defs)

	ddf.filename = DDFname
	
	for row in field_defs:
		
		if row[0] not in field_dict.keys():
			raise RuntimeError("Unable to find field '" + row[0] + "' from the .ddf file")

		if isinstance(field_dict[row[0]], list):
			val_tokens = field_dict[row[0]]
		else:
			val_tokens = field_dict[row[0]].split()

		# String to numeric conversion
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
	ddf_data_file = open(DDFname, 'r')
	text_info = ddf_data_file.read()
	start_index = text_info.index(separator, 2) + len(separator)
	ddf.misc_info = text_info[start_index:text_info.index(separator, start_index)]
	ddf_data_file.close()

	# ddf.read_in_time = datestr(clock, 0)
	# For backwards compatibility!
	# ddf.npix = ddf.npts

	# For backwards compatibility!
	if (ddf.version >= 6):
	  ddf.encode_fov = [a*b for a,b in zip(ddf.npix, ddf.pixel_spacing)]

	# --- for testing purposes ONLY ---
	# print(ddf)

	return ddf



####################	
# Helper Functions #
####################

def is_number(s):
	"""
	a method that returns true or false if a string is a number

	Arguments:
	s (string) -- phrase that is tested 
	"""
	try:
		float(s)
	except ValueError:
		return False
	return True

def get_numbers(input_string):
	"""
	a method that returns all the numbers in a given string

	Arguments:
	input_string (string) -- phrase that may contain words and numbers
	"""
	return [float(n) for n in input_string.split() if is_number(n)]

def get_words(input_string):
	"""
	a method that returns all the words (not numbers) in a given string

	Arguments:
	input_string (string) -- phrase that may contain words and numbers
	"""
	return [w for w in input_string.split() if not is_number(w)]

class ddf_struct:
	"""
	class for constructing ddf objects with various attributes

	Methods:
	__init__(self, field_defs_structure) -- Constructor
	__str__(self) 						 -- custimized method to print ddf objects

	Attributes:
	filename (string) -- name of the .ddf file where data originated
	version (int) 	  -- version of field 2D array for data collection
	... See field array for More Attributes
	"""
	def __init__(self, field_defs_structure):
		"""
		constructor method for ddf_struct class. Sets every possible attribute 
		to "DEFUALT" value based on attribute field version. 

		Arguments:
		self (ddf_struct) 				-- ddf object
		field_defs_structure (2D-array) -- attribute 2D array info
		"""
		self.filename = "DEFAULT"
		for row in field_defs_structure:
			if (row[3] == "Array"):
				if not hasattr(self, row[2]):
					setattr(self, row[2], [])
			else:
				setattr(self, row[2], "DEFAULT")

	def __str__(self):
		"""
		a custimized method to print ddf objects to show all attributes neatly

		Arguments:
		self (ddf_struct) -- ddf object
		"""
		print("\n --------- ddf Properties --------- \n")
		print("The source of the data: " + self.filename)
		print()
		pprint.pprint(self.__dict__)
		print()
		return "\n --------- End of ddf Properties --------- "

# --- field 2D Arrays ---

DEFUALT_FIELD = [ \
	['XXXXXXX',                      'XXX',			'XXXXXXX'         , "XXXXXXXXXXXX"], \
	['XXXXXXX',                      'XXX',			'XXXXXXX'         , "XXXXXXXXXXXX"],
	['XXXXXXX',                      'XXX',			'XXXXXXX'         , "XXXXXXXXXXXX"]
]


v5a_field_defs = [ \
	['version',                      'flt',			'version'         , "Single Value"], \
	['study id',                     'str',			'studyid'         , "Single Value"], \
	['study # ',                     'str',			'studynum'        , "Single Value"], \
	['position',                     'str',			'position'        , "Single Value"], \
	['coil',                         'str',			'coil'            , "Single Value"], \
	['series #'                      'int',			'series'          , "Single Value"], \
	['orientation'                   'int',			'orientation'     , "Single Value"], \
	['echo/time/met index',          'int',			'index'           , "Single Value"], \
	['value',                        'flt',			'value'           , "Single Value"], \
	['root name',                    'str',			'rootname'        , "Single Value"], \
	['comment',                      'str',			'comment'         , "Single Value"], \
	['sequence name',                'str',			'sequence'        , "Single Value"], \
	['localization type',            'int',			'localizationtype', "Single Value"], \
	['',                             'flt',			'specfrequency'   , "Single Value"], \
	['sweepwidth(Hz)',               'flt',			'sweepwidth'      , "Single Value"], \
	['dwelltime',                    'flt',			'dwelltime'       , "Single Value"], \
	['satpulse pos(Hz)',             'flt',			'satpulsepos'     , "Single Value"], \
	['bandwidth(Hz)',                'flt',			'bandwidth'       , "Single Value"], \
	['beginning of acquisition (ms)','flt',			'acqbeginning'    , "Single Value"], \
	['gradient on time (ms)',        'flt',			'gradontime'      , "Single Value"], \
	['nex',                          'flt',			'nex'             , "Single Value"], \
	['chop',                         'flt',			'chop'            , "Single Value"], \
	['even_sym',                     'flt',			'even_sym'        , "Single Value"], \
	['pe_order',                     'flt',			'pe_order'        , "Single Value"], \
	['datatype',                     'int',			'datatype'        , "Single Value"], \
	['number of dimensions',         'int',			'numdim'          , "Single Value"], \
	['acqpts',                       'int',			'acqspec'         , "Single Value"], \
	['fov',                          'flt',			'fov'             , "Array"], \
	['acqpts',                       'int',			'acqpts'          , "Array"], \
	['fov',                          'flt',			'fov'             , "Array"], \
	['acqpts',                       'int',			'acqpts'          , "Array"], \
	['fov',                          'flt',			'fov'             , "Array"], \
	['acqpts',                       'int',			'acqpts'          , "Array"], \
	['center',                       'flt',			'recon_center'    , "Single Value"], \
	['toplc',                        'flt',			'recon_toplc'     , "Single Value"], \
	['dcos',                         'flt',			'recon_dcos1'     , "Single Value"], \
	['dcos',                         'flt',			'recon_dcos2'     , "Single Value"], \
	['dcos',                         'flt',			'recon_dcos3'     , "Single Value"], \
	['pcenter',                      'flt',			'encode_center'   , "Single Value"], \
	['pfov',                         'flt',			'encode_fov'      , "Single Value"], \
	['pmatrix',                      'int',			'encode_matrix'   , "Single Value"], \
	['reverse',                      'int',			'encode_reverse'  , "Single Value"], \
	['pdcos',                        'flt',			'encode_dcos1'    , "Single Value"], \
	['pdcos',                        'flt',			'encode_dcos2'    , "Single Value"], \
	['pdcos',                        'flt',			'encode_dcos3'    , "Single Value"], \
	['bcenter',                      'flt',			'box_center'      , "Single Value"], \
	['bsize',                        'flt',			'box_size'        , "Single Value"], \
	['bdcos',                        'flt',			'box_dcos1'       , "Single Value"], \
	['bdcos',                        'flt',			'box_dcos2'       , "Single Value"], \
	['bdcos',                        'flt',			'box_dcos3'       , "Single Value"], \
	['refacq',                       'str',			'refacq'          , "Single Value"], \
	['refrecon',                     'str',			'refrecon'        , "Single Value"]  \
]

v5b_field_defs = [ \
    ['version',                      'flt',			'version'         , "Single Value"], \
    ['study id',                     'str',			'studyid'         , "Single Value"], \
    ['study # ',                     'str',			'studynum'        , "Single Value"], \
    ['position',                     'str',			'position'        , "Single Value"], \
    ['coil',                         'str',			'coil'            , "Single Value"], \
    ['series #'                      'int',			'series'          , "Single Value"], \
    ['orientation'                   'int',			'orientation'     , "Single Value"], \
    ['echo/time/met index',          'int',			'index'           , "Single Value"], \
    ['value',                        'flt',			'value'           , "Single Value"], \
    ['root name',                    'str',			'rootname'        , "Single Value"], \
    ['comment',                      'str',			'comment'         , "Single Value"], \
    ['sequence name',                'str',			'sequence'        , "Single Value"], \
    ['localization type',            'int',			'localizationtype', "Single Value"], \
    [''             ,                'flt',			'specfrequency'   , "Single Value"], \
    ['sweepwidth(Hz)',               'flt',			'sweepwidth'      , "Single Value"], \
    ['dwelltime',                    'flt',			'dwelltime'       , "Single Value"], \
    ['centfreq pos(Hz)',             'flt',			'centfreq'        , "Single Value"], \
    ['pulse type',                   'int',			'pulsetype'       , "Single Value"], \
    ['beginning of acquisition (ms)','flt',			'acqbeginning'    , "Single Value"], \
    ['gradient on time (ms)',        'flt',			'gradontime'      , "Single Value"], \
    ['nex',                          'flt',			'nex'             , "Single Value"], \
    ['chop',                         'flt',			'chop'            , "Single Value"], \
    ['even_sym',                     'flt',			'even_sym'        , "Single Value"], \
    ['pe_order',                     'flt',			'pe_order'        , "Single Value"], \
    ['datatype',                     'int',			'datatype'        , "Single Value"], \
    ['number of dimensions',         'int',			'numdim'          , "Single Value"], \
    ['acqpts',                       'int',			'acqspec'         , "Single Value"], \
    ['fov',                          'flt',			'fov'             , "Array"], \
    ['acqpts',                       'int',			'acqpts'          , "Array"], \
    ['fov',                          'flt',			'fov'             , "Array"], \
    ['acqpts',                       'int',			'acqpts'          , "Array"], \
    ['fov',                          'flt',			'fov'             , "Array"], \
    ['acqpts',                       'int',			'acqpts'          , "Array"], \
    ['center',                       'flt',			'recon_center'    , "Single Value"], \
    ['toplc',                        'flt',			'recon_toplc'     , "Single Value"], \
    ['dcos',                         'flt',			'recon_dcos1'     , "Single Value"], \
    ['dcos',                         'flt',			'recon_dcos2'     , "Single Value"], \
    ['dcos',                         'flt',			'recon_dcos3'     , "Single Value"], \
    ['pcenter',                      'flt',			'encode_center'   , "Single Value"], \
    ['pfov',                         'flt',			'encode_fov'      , "Single Value"], \
    ['pmatrix',                      'int',			'encode_matrix'   , "Single Value"], \
    ['reverse',                      'int',			'encode_reverse'  , "Single Value"], \
    ['pdcos',                        'flt',			'encode_dcos1'    , "Single Value"], \
    ['pdcos',                        'flt',			'encode_dcos2'    , "Single Value"], \
    ['pdcos',                        'flt',			'encode_dcos3'    , "Single Value"], \
    ['bcenter',                      'flt',			'box_center'      , "Single Value"], \
    ['bsize',                        'flt',			'box_size'        , "Single Value"], \
    ['bdcos',                        'flt',			'box_dcos1'       , "Single Value"], \
    ['bdcos',                        'flt',			'box_dcos2'       , "Single Value"], \
    ['bdcos',                        'flt',			'box_dcos3'       , "Single Value"], \
    ['refacq',                       'str',			'refacq'          , "Single Value"], \
    ['refrecon',                     'str',			'refrecon'        , "Single Value"], \
    ['npoints',                      'int',			'npix'	   		  , "Array"] \
]

v6_field_defs = [ \
    ['version',                      'flt',  		'version'         , "Single Value"], \
    ['object type',                  'str',  		'object_type'     , "Single Value"], \
    ['patient id',                   'str',  		'patient_id'      , "Single Value"], \
    ['patient name',                 'str',  		'patient_name'    , "Single Value"], \
    ['patient code',                 'str',  		'patient_code'    , "Single Value"], \
    ['date of birth',                'str',  		'dob'             , "Single Value"], \
    ['sex',                          'str',  		'sex'             , "Single Value"], \
    ['study id',                     'str',  		'studyid'         , "Single Value"], \
	['study code',                   'str',  		'study_code'      , "Single Value"], \
	['study date',                   'str',  		'study_date'      , "Single Value"], \
	['accession number',             'str',  		'accession_number', "Single Value"], \
	['root name',                    'str',  		'root_name'       , "Single Value"], \
	['series number',                'int',  		'series'          , "Single Value"], \
	['series description',           'str',  		'series_description', "Single Value" ], \
	['comment',                      'str',  		'comment'         , "Single Value"], \
	['patient entry',                'str',  		'patient_entry'   , "Single Value"], \
	['patient position',             'str',  		'patient_position', "Single Value"], \
	['orientation',                  'str',  		'orientation'     , "Single Value"], \
	['data type',                    'str',  		'data_type'       , "Single Value"], \
	['number of components',         'int',  		'num_components'  , "Single Value"], \
	['source description',           'str',  		'source_description', "Single Value"], \
	['number of dimensions',         'int',  		'numdim'          , "Single Value"], \
	['dimension 1',                  'str',  		'dimension_type'  , "Array"], \
	['dimension 2',                  'str',  		'dimension_type'  , "Array"], \
	['dimension 3',                  'str',  		'dimension_type'  , "Array"], \
	['dimension 4',                  'str',  		'dimension_type'  , "Array"], \
	['center(lps, mm)',              'flt',  		'center'          , "Single Value"], \
	['toplc(lps, mm)',               'flt',  		'toplc'           , "Single Value"], \
	['dcos0',                        'flt',  		'dcos0'           , "Single Value"], \
	['dcos1',                        'flt',  		'dcos1'           , "Single Value"], \
	['dcos2',                        'flt',  		'dcos2'           , "Single Value"], \
	['coil name',                    'str',  		'coil_name'       , "Single Value"], \
	['slice gap(mm)',                'flt',  		'slice_gap'       , "Single Value"], \
	['echo time(ms)',                'flt',  		'TE'              , "Single Value"], \
	['repetition time(ms)',          'flt',  		'TR'              , "Single Value"], \
	['inversion time(ms)',           'flt',  		'TI'              , "Single Value"], \
	['flip angle',                   'flt',  		'flip_angle'      , "Single Value"], \
	['pulse sequence name',          'str',  		'sequence'        , "Single Value"], \
	['transmitter frequency(MHz)',   'flt',  		'transmit_freq'   , "Single Value"], \
	['isotope',                      'str',  		'isotope'         , "Single Value"], \
	['field strength(T)',            'flt',  		'field_strength'  , "Single Value"], \
	['number of sat bands',          'int',  		'num_sat_bands'   , "Single Value"], \
	['localization type',            'str',  		'loc_type'        , "Single Value"], \
	['center frequency(MHz)',        'flt',  		'centfreq'        , "Single Value"], \
	['ppm reference',                'flt',  		'ppm_ref'         , "Single Value"], \
	['sweepwidth(Hz)',               'flt',  		'sweepwidth'      , "Single Value"], \
	['dwelltime(ms)',                'flt',  		'dwelltime'       , "Single Value"], \
	['frequency offset(Hz)',         'flt',  		'freq_offset'     , "Single Value"], \
	['centered on water',            'str',  		'center_on_water' , "Single Value"], \
	['suppression technique',        'str',  		'suppresion_tech' , "Single Value"], \
	['residual water',               'str',  		'residual_water'  , "Single Value"], \
	['number of acquisitions',       'int',  		'num_acquisitions', "Single Value"], \
	['chop',                         'str',  		'chop'            , "Single Value"], \
	['even symmetry',                'str',  		'even_sym'        , "Single Value"], \
	['data reordered',               'str',  		'data_reordered'  , "Single Value"], \
	['acq. toplc(lps, mm)',          'flt',  		'acq_toplc'       , "Single Value"], \
	['acq. spacing(mm)',             'flt',  		'acq_spacing'     , "Single Value"], \
	['acq. number of data points',   'int',  		'acq_n_data_points', "Single Value"], \
	['acq. number of points',        'int',  		'acq_n_points'    , "Single Value"], \
	['acq. dcos1',                   'flt',  		'acq_dcos1'       , "Single Value"], \
	['acq. dcos2',                   'flt',  		'acq_dcos2'       , "Single Value"], \
	['acq. dcos3',                   'flt',  		'acq_dcos3'       , "Single Value"], \
	['selection center(lps, mm)',    'flt',  		'box_center'      , "Single Value"], \
	['selection size(mm)',           'flt',  		'box_size'        , "Single Value"], \
	['selection dcos1',              'flt',  		'box_dcos1'       , "Single Value"], \
	['selection dcos2',              'flt',  		'box_dcos2'       , "Single Value"], \
	['selection dcos3',              'flt',  		'box_dcos3'       , "Single Value"], \
	['npoints',                      'int',			'npix',	   				"Array"], \
	['pixel spacing(mm)',            'flt_PASS',	'pixel_spacing',		"Array"], \
    ['sat band thickness',           'flt_PASS',  	'satband_thickness',	"Array"], \
    ['sat band orientation',         'flt_PASS',  	'satband_orientation',	"Array"], \
    ['sat band position',            'flt_PASS',  	'satband_position',		"Array"], \
    ['specpoints',					 'int',			'specpoints',			"Single Value"] \
]

v6p1_ext_defs = [ \
     ['reordered toplc(lps, mm)',     'flt',  		'reordered_toplc'      , "Single Value"], \
     ['reordered center(lps, mm)',    'flt',  		'reordered_center'     , "Single Value"], \
     ['reordered spacing(mm)',        'flt',  		'reordered_spacing'    , "Single Value"], \
     ['reordered number of points',   'int',  		'reordered_n_points'   , "Single Value"], \
     ['reordered dcos1',              'flt',  		'reordered_dcos1'      , "Single Value"], \
     ['reordered dcos2',              'flt',  		'reordered_dcos2'      , "Single Value"], \
     ['reordered dcos3',              'flt',  		'reordered_dcos3'      , "Single Value"]  \
]
v6p1_field_defs = [row[:] for row in v6_field_defs]
v6p1_field_defs.extend(v6p1_ext_defs)