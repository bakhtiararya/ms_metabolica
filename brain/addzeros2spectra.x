#!/bin/csh -f

matlab -nojvm -nosplash -nodisplay -r "addzeros2spectra($1, '$2', '$3'); exit;";


