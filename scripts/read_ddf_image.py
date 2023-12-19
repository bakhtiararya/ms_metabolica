# -----------------------------------------------------------------------------
# Name:       read_ddf_image.py
# Purpose:   
#
# Author:      Arya Haghighi
# Date:        06/19/2019
# -----------------------------------------------------------------------------
'''
    READ_DDF_IMAGE Reads an DDF file and associated data file
 
    DATA_STRUCTURE = READ_DDF_IMAGE(ROOTNAME) reads two files for this
    dataset.  First, it reads 'ROOTNAME.ddf' which gives it the associated
    header information.  This DDF can be either an MRSC v5 or v6 file.  
    A data file is then read; these are always .cmplx files, consisting of
    a set of 32-bit float pairs representing real and imaginary parts
    of each value.  The results are returned as a structure with two fields.
    The first is IMAGE_STRUCTURE.DDF where DDF is itself a structure with
    fields corresponding to data entries found in the IDF file.  The second
    is the complex data, which can come in a variety of user
    specified formats (see below).
 
    IMAGE_STRUCTURE = READ_DDF_IMAGE(ROOTNAME, DISPLAYFLAG) does the same
    thing, but if DISPLAYFLAG is a 0, then it doesn't print out information
    about what file it's opening.  This is useful in those cases when you
    are trying to have a nice clean uncluttered screen.
 
    IMAGE_STRUCTURE = READ_DDF_IMAGE(ROOTNAME, DISPLAYFLAG, FORMATFLAG) 
    There are 3 integer options for the format of the complex data,
    as described here:
 
       0 (default)    a 4-D array of complex values, accessed as 
                      IMAGE_STRUCTURE.IMG(FREQUENCY, X, Y, Z)
                      ... which returns a complex value.
 
       1              a 3-D array of structures.  Each element of
                      the array is a structure with a REAL field
                      and an IMAGINARY field.  Access these as
                      IMAGE_STRUCTURE.IMG(X,Y,Z).REAL(FREQUENCY) and 
                      ...IMAGINARY(FREQUENCY).
                      (This is the old READ_DDF_IMAGE style)
 
       2              Two 3-D arrays of doubles.  Access these as
                      IMAGE_STRUCTURE.REAL(FREQ,X,Y,Z) and IMAG(FREQ,X,Y,Z)
                      (This is the style in READ_DDF_CMPLX)
 
    Note that this code can be used on gzip'd files.  These files are 
    unzipped and reszipped during the reading process, using a shell
    command.  This can be problematic if you are running on a Windows 
    PC and the call SYSTEM('GUNZIP') doesn't mean anything to your PC.
 
    Note that in general, this will NOT work on v3 files.
 
    See also READDDF_FILE, WRITEDDF_FILE, WRITE_DDF_IMAGE.
 
      Michael C. Lee, Ph.D.
      Department of Radiology
      University of California, San Francisco
 
 
    Copyright (c) 2009 Regents of the University of California.
    All rights reserved.  This software provided pursuant to a
    license agreement containing restrictions on its disclosure,
    duplication and use.  This notice must be embedded in or
    attached to all copies, including partial copies, of the
    software or any revisions or derivations thereof.
 
    $URL: https://intrarad.ucsf.edu/svn/rad_software/surbeck/brain/libs/file_io/trunk/read_ddf_image.m $
    $Rev: 14674 $
    $Author: jasonc@RADIOLOGY.UCSF.EDU $
    $Date: 2009-08-25 16:29:52 -0700 (Tue, 25 Aug 2009) $
'''
import importlib
import array
import subprocess
import struct
import os
from os import path
from functools import reduce
import numpy as np
from operator import mul
from readddf_file import *
import pdb
import struct

def read_ddf_image(rootname = "E3650_csi_cor_sum_comb_phased", displayflag = True, complexformat = 0):
	"""
 
	"""
	rootname = str(rootname)

	unzipped_flag = False

	if (displayflag):
		print("\n  Reading DDF file:    {0}.ddf".format(rootname))

	output = data_image()
	output.ddf = readddf_file(rootname)

	datafilename = rootname + ".cmplx"

	if os.path.exists(datafilename):
		datafile = open(datafilename, 'rb') 
	elif (path.exists(datafilename + ".gz")):
		unzipped_flag = True
		subprocess.run("gunzip " + datafilename + ".gz", shell=True)
		datafile = open(rootname + ".cmplx", "rb")
	else:
		raise RuntimeError("Could not find data file {0} or {0}.gz".format(datafilename))

	num_data_points = reduce(lambda x, y: x*y, output.ddf.npix) * output.ddf.specpoints
	number_of_total_floats = num_data_points * 2
	expected_total_bytes = number_of_total_floats * 4

	cmplxinfo_bytes = os.path.getsize(datafilename)
	if (cmplxinfo_bytes != expected_total_bytes): 
		raise RuntimeError("Expected {0} to be {1} bytes; found {2} bytes on disk".format(datafilename,num_data_points*2*4,cmplxinfo_bytes))
	
	if (displayflag):
	  print("\n  Reading data file:   " + datafilename)

	if (complexformat == 0):

		# --- for testing purpose ONLY ---
		test_count = 0
		
		raw_data = datafile.read()
		float_values = []
		struct_directive = "<f"
		for i in range(0, len(raw_data), 4):
			float_block = raw_data[i:i+4]
			
			value = struct.unpack(struct_directive, float_block)
			
			if (test_count == 43544):
				print()
				print("For 43544")
				print("----------------")
				print("float_block: " + str(float_block))
				print("value: " + str(value))
				print("vale[0]: " + str(value[0]))
				print()

			if(abs(-1*3.286e-38 - value[0]) < 0.001e-38):
				#print(i)
				print(len(float_values)-1)

			# --- for testing purpose ONLY ---
			#if (i % 100000 == 0):
			#	print("successfully decoded {0} as {1} which starts as index {2}".format(float_block, value, i))
			
			float_values.append(value[0])
			
			# --- for testing purpose ONLY ---
			test_count += 1

		print(float_values[43543])
		print(float_values[1517867])
		print(float_values[2545691])
		print(float_values[2653766])
		print(float_values[3111847])
		print(float_values[3647358])
		print(float_values[4037446])
		print(float_values[5125975])
		print(float_values[5717738])
		print(float_values[8786016])
		print(float_values[9415000])
		print(float_values[9488046])
		print(float_values[11146940])
		print(float_values[11242317])
		print(float_values[12192754])

		# --- for testing purpose ONLY ---
		#raw_data = datafile.read()
		#unpacking_direction = "<{0}f".format(number_of_total_floats)
		#complex_data = struct.unpack(unpacking_direction, raw_data)

		num_points_read = len(float_values)
		if num_points_read != number_of_total_floats:
			RuntimeError("Only able to read {0} floats, expected {1}".format(number_of_total_floats, num_points_read))

		assert number_of_total_floats % 2 == 0, "there is {0} total points, as this is not even we cannot convert all the numbers to complex numbers".format(num_points_read)

		complex_values = []
		for i in range(0, len(float_values), 2):
			complex_point = complex(float_values[i], float_values[i+1])
			complex_values.append(complex_point)
		output.img = np.array(complex_values)

		format_array_dimension = output.ddf.npix[:]
		format_array_dimension.insert(0, output.ddf.specpoints)

		output.img = np.reshape(output.img, format_array_dimension)

		# --- for testing purpose ONLY ---
		#print(output.img[1][10][11][1])
	
	elif (complexformat == 1):
		raise NotYetImplementedError("Complex Format 1 has not been implemented in Python yet")
		# for z in range(output.ddf.npix[3]):
		# 	for y in range(output.ddf.npix[2]):
		# 		for x in range(output.ddf.npix[1]):
		# 			temp_data = array.array("f")
		# 			temp_data.fromfile(datafile, output.ddf.specpoints*2)
		# 			if num_temp_data != num_data_points*2:
		# 				RuntimeError("cmplx file seems too short when reading ({0},{1},{2})".format(x,y,z))
		# 	        if max(abs(temp_data)) > eps:
		# 	        	output.img[x,y,z].real = temp_data[1:2:]
		# 	       		output.img[x,y,z].imaginary = temp_data[2:2:]   
		# 	        else:
		# 	        	output.img[x,y,z].real = []
		# 	        	output.img[x,y,z].imaginary = []
	elif (complexformat == 2):
		raise NotYetImplementedError("Complex Format 1 has not been implemented in Python yet")
		# temp_data = array.array("f")
		# temp_data.fromfile(datafile, num_data_points) 
		# num_temp_data = num_matrix_data(temp_data)
		# if num_temp_data != num_data_points*2:
		# 	RuntimeError("Only able to read {0} floats, expected {1}".format(num_temp_data,num_data_points*2))

		# temp_complex = [[0] for i in range(len(temp_data)/2)]
		# temp_complex = complex(temp_data[1:2:len(temp_data)], temp_data[2:2:len(temp_data)])
		# output.img = reshape_data(output.img, output.ddf.specpoints, output.ddf.npix)
		#output.real = real(temp_complex)
		#output.imag = imag(temp_complex)
	

	if (unzipped_flag):
		subprocess.run("gzip " + datafilename, shell=True)

	datafile.close()

	#return output


def main():
	read_ddf_image()

class data_image:

	def __init__(self):
		self.ddf = ddf_struct(DEFUALT_FIELD)
		self.img = "DEFUALT"

	def __str__(self):
		print("\n ++++++++++ data_image Properties ++++++++++ \n")
		print(self.ddf)
		print()
		print("--------- img Property --------- ")
		pprint.pprint(self.img)
		print("--------- End of img Property --------- ")
		print()
		return "\n ++++++++++ End of ddf Properties ++++++++++ "

main()