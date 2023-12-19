#!/bin/csh -f

if (${#argv} < 1) then
  echo 
  echo "Usage: anon_idf.x rootname"
  echo 
  echo "       Strips the studyid, studynum, and comment"
  echo      
  exit
endif

set temp_file = /tmp/temp_$$

set rootname = $1 

if (!(-e ${rootname})) then
  echo
  echo anon_idf.x: Unable to find file ${rootname} ... aborting!
  echo
  exit
endif

setenv current_date "`date`"

set basename = `basename ${rootname}`

if (${#argv} > 1) then
  if (-e $2) then
    echo ${cwd} : ${basename} >> $2
  else 
    echo ${cwd} : ${basename} > $2
  endif
  date                        >> $2
  grep studyid ${rootname}    >> $2
  grep 'study #:' ${rootname} >> $2
  grep comment ${rootname}    >> $2
  echo >> $2
endif

gawk '$1 != "studyid:" && $1 != "study" && $1 != "comment:" {print $0};  \\
      $1 == "studyid:" {print "studyid: 12345678"};  \\
      $1 == "study"    {print "study #:    12345"};  \\
      $1 == "comment:" {print "comment: Anonymized on " ENVIRON["current_date"]}; ' \
      $1 > ${temp_file}

mv ${temp_file} $1

unsetenv current_date



