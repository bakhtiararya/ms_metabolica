#!/bin/csh -f

if (${#argv} < 1) then
  echo
  echo Usage: anon_idf_dir.x <dir> [absolute_path_to_logfile]
  echo
endif

if (${#argv} == 2) then
  set logfile = $2
else
  set logfile = ''
endif

cd $1

echo ---------------------------------------------------
echo Entering directory $cwd
echo ---------------------------------------------------


foreach idffile (`ls *.idf`)
  echo "  Anonymizing ${idffile}"
  anon_idf.x $idffile ${logfile}
end

foreach other_file (`ls -d *`)

  set is_link = `readlink ${other_file} | wc -l`

  if (-d ${other_file} && ${is_link} == 0) then
    anon_idf_dir.x ${other_file} ${logfile}
  endif
end
