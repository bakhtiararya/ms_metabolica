#!/bin/csh -f

if (${#argv} < 3) then
  echo
  echo "Usage: zero_slices.x <rootname> <first_to_keep> <last_to_keep>"
  echo
  echo "       Zeros out all pixels except those in the specified slices"
  echo 
  echo "       Last modified: 28 October 2004"
  echo
  exit
endif

set rootname    = $1
set first_slice = $2
set last_slice  = $3

if (!(-e ${rootname}.idf)) then
  echo 
  echo File ${rootname}.idf not found
  echo
  exit
endif

set READ_IDF_FIELD = /netopt/share/bin/local/brain/read_idf_field.x
set ZERO_SLICES    = /netopt/bin/local/brain/zero_slices

set npix     = `${READ_IDF_FIELD} ${rootname}.idf npix`
set filetype = `${READ_IDF_FIELD} ${rootname}.idf filetype`

switch ($filetype[1])
  case "2":
    set bytes_per_pixel = 1
    set extension       = "byt"
    breaksw
  case "3":
    set bytes_per_pixel = 2
    set extension       = "int2"
    breaksw
  case "7":
    set bytes_per_pixel = 4
    set extension       = "real"
    breaksw
  default:
    echo
    echo Don't recognize filetype ${filetype}!
    echo
endsw

if (!(-e ${rootname}.${extension})) then
  echo 
  echo File ${rootname}.${extension} not found
  echo
  exit
endif

${ZERO_SLICES} ${rootname}.${extension} ${first_slice} ${last_slice} \
                 $npix[1] $npix[2] $npix[3] $bytes_per_pixel

