#!/bin/csh -f

# $Header: written by Yan Li 

set datapath = `pwd`
echo "reorganize data at $datapath"

if (! -e rawfiles) then
	echo "$datapath/rawfiles does not exist"
	exit 1
endif

set nexam = `ls -d ./E* | wc -l`
if ($nexam == 1) then
	set exam = `ls -d ./E* | cut -d"/" -f2`
endif
if ($nexam == 1) then
	set exam = `ls -d ./E* | cut -d"/" -f2`
	set exam = `echo $exam[1]`
endif
if ($nexam == 0) then
	set exam = t0000
endif
echo "file root = $exam"
cd rawfiles

set npfiles = `ls -S --ignore='*.*' | wc -l`
set pfiles = `ls -S --ignore='*.*'`
set p = 1
set q = 1
		
while ($p <= $npfiles)
	set pname = `echo $pfiles[$p]`
	set psdname = `rdump -A $pname | grep -i "image.psdname" | cut -d"=" -f2 | cut -d"#" -f1`
	if ($psdname == prose7T_yan) then
		set psize = `stat -c %s $pname`
		set pdescription = `rdump -p $pname | grep "Series description" | cut -d":" -f2 | cut -d" " -f4-10`
		set pdescription = `echo $pdescription | sed -e 's/ /_/g'`
		set snum = `rdump -p $pname | grep -i "series #" | cut -d"#" -f3`
		if ($psize > 35229056) then
			set pacq = met
			set newname = ${exam}_${pdescription}					
			if (! -e ../spectra_${pdescription}) then 
				mkdir ../spectra_${pdescription}
				cp $pname ../spectra_${pdescription}/${newname}
				echo "$p $q $npfiles $pname $snum $pdescription ($psize) -> spectra_${pdescription}/${newname}"
			else
				set snum1 = `rdump -p ../spectra_${pdescription}/$newname | grep -i "series #" | cut -d"#" -f3`
				if (! -e ../spectra_${pdescription}_2) then
					if ($snum1 < $snum) then
						mkdir ../spectra_${pdescription}_2
						cp $pname ../spectra_${pdescription}_2/${newname}_2
						echo "spectra_${pdescription} series $snum1 vs. spectra_${pdescription}_2 series $snum"
					else
						if ($snum1 > $snum) then
							mv ../spectra_${pdescription} ../spectra_${pdescription}_2
							mv ../spectra_${pdescription}_2/$newname ../spectra_${pdescription}_2/${newname}_2
							echo "    mv  ../spectra_${pdescription} ../spectra_${pdescription}_2"
							mkdir ../spectra_${pdescription}
							cp $pname ../spectra_${pdescription}/${newname}
							echo "$p $q $npfiles $pname $snum $pdescription ($psize) -> spectra_${pdescription}/${newname}"
							set snum1 = `rdump -p ../spectra_${pdescription}/$newname | grep -i "series #" | cut -d"#" -f3`
							set snum2 = `rdump -p ../spectra_${pdescription}_2/${newname}_2 | grep -i "series #" | cut -d"#" -f3`
							echo "spectra_${pdescription} series $snum1 vs. spectra_${pdescription}_2 series $snum2"
						endif
					endif 
				else
					echo "Error $pname $pdescription > 2 files"
				endif
			endif
		else
			set pacq = water
			set newname = ${exam}_${pdescription}_water
			set snumb =
			if (-e ../spectra_${pdescription}) then
				set sumb = `rdump -p ../spectra_${pdescription}/${exam}_${pdescription} | grep -i "series #" | cut -d"#" -f3`
				if ($sumb == $snum) then
					cp $pname ../spectra_${pdescription}/${newname}
					echo "$p $q $npfiles $pname $snum $pdescription ($psize) -> spectra_${pdescription}/${newname}"
				else
					if (! -e ../spectra_${pdescription}_2) then
						echo "$pname $snum ($snumb $snumb) spectra_${pdescription}_2 does not exist"
					else
						set sumb = `rdump -p ../spectra_${pdescription}_2/${exam}_${pdescription}_2 | grep -i "series #" | cut -d"#" -f3`
						if ($sumb == $snum) then
							cp $pname ../spectra_${pdescription}_2/${exam}_${pdescription}_2_water
							echo "$p $q $npfiles $pname $snum $pdescription ($psize) -> spectra_${pdescription}_2/${exam}_${pdescription}_2_water"
						else
							echo "Error $pname water $pdescription > 2 files"
						endif
					endif
				endif
			else
				echo "$pname ($snum $snumb) spectra_${pdescription} does not exist"
			endif
										
		endif		
		@ q++
	endif
	@ p++
end