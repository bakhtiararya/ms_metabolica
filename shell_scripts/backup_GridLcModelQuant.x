#!/bin/csh -f

# $Header: written by Yan Li 

if ($#argv < 1) then   
    	echo "Usage: GridLcModelQuant rootname [--lcsetup] [--lcquant] [--lcconvert] [--lcnorun] [--lcwater]"
	echo "	--lcsetup	generating raw file and control files"
	echo "	--lcquant	running lcmodel quantification"
	echo "	--lcconvert	converting quantification results to cmplx and real files"
	echo "  --lcwater 	water scaling and eddy-current correction [water file name = rootname_water]"
	echo "	--lcnorun	no running"
    exit
endif

# Processing Steps Setting
set rname = $1
if (! -e ${rname}.ddf) then
	echo "${rname}.ddf does not exist"
	exit
endif

if (($#argv) == 1) then
	set lcsetup = 1
	set lcquant = 1
	set lcconvert = 1
	set lcwater = 1
else
	set lcsetup = 0
	set lcquant = 0
	set lcconvert = 0
	set lcwater = 0
endif

set varname = `echo $argv`
set num = 2
while ($num <= ($#argv))
    set tvar = `echo $varname | cut -d" " -f$num`
    if ($tvar == "--lcsetup") then
    	set lcsetup = 1
    endif
    if ($tvar  == "--lcquant") then
      	set lcquant = 1
    endif   
    if ($tvar  == "--lcconvert") then
      	set lcconvert = 1
    endif
    if ($tvar  == "--lcwater") then
    	set lcwater = 1
    endif
    if ($tvar == "--lcnorun") then 
   		set lcsetup = 0
		set lcquant = 0
		set lcconvert = 0
		set lcwater = 0
		break
    endif
    @ num++
end

if (($lcwater == 1) & (! -e ${rname}_water.ddf)) then
	echo "${rname}_water.ddf does not exist"
	echo "No water scaling and Eddy-current correction"
	set lcwater = 0
endif

echo " "
echo " rootname $rname"
echo " lcsetup $lcsetup"
echo " lcquant $lcquant"
echo " lcconvert $lcconvert"
echo " lcwater $lcwater"
echo " "

# Setup files
set echotime = `grep -w "echo time" ${rname}.ddf`
set echotime = `echo $echotime | cut -d":" -f2 | cut -d"." -f1`
set field = `grep -w "field strength" ${rname}.ddf`
set field = `echo $field | cut -d":" -f2 | cut -d"." -f1`
echo " Echo Time = $echotime ms"
echo " Field Strength = $field T"

set basis_type = sim
if ($field == 7) then
	switch (${echotime})
		case 30
			set basisset = sim_se30_qb37t_tumor.basis
			set datatype = 7tshort
			set fvalue =
			breaksw
		case 68
			set basisset = mega_te68_qb37t3.basis
			set fvalue = 
			set datatype = 7tgaba
			breaksw
		default:
	        set basisset = sim_se${echotime}_qb37t.basis
			set datatype = 7tshort
	endsw
else
	switch (${echotime})
		case 144
			set basisset = sim_te144_qb33t.basis
			set fvalue = 
			set datatype = 3tlong
			breaksw
		case 288
			set basisset = sim_te288_15t.basis
			set fvalue = 
			set datatype = 3tlong
			breaksw
		case 35
			if (${basis_type} =~ sim) then
				set basisset = sim_te35_qb33t.basis
				set fvalue = 
			else
				set basisset = press_te35_3t_2014.basis
				set fvalue =
			endif
			set datatype = 3tshort
			breaksw
		case 30
			set basisset = sim_te30_3t.basis
			set datatype = 3tshort
			breaksw
		case 97
			if ( ${basis_type} =~ sim) then
				set basisset = sim_te97_3t.basis
				set fvalue =
			else
				set basisset = asym_trey.basis
				set fvalue =
			endif
			set datatype = 3tlong
			breaksw
		default:
			echo "Can not find basis-set to use?"
			return
	endsw
endif

echo " Basis = ${basisset}"
echo " Datatype = ${datatype}"
echo " "

set lcbasis = /home/liyan/.lcmodel_solaris/basis-sets/${basisset}

set lcdir = LcGrid
if (! -e $lcdir) then
	mkdir $lcdir
endif
cd $lcdir

if (! -e ${rname}.cmplx) then
	cp ../${rname}.cmplx .
	cp ../${rname}.ddf .
endif
if (! -e ${rname}_inv.cmplx) then
	svk_fft -i ${rname}.cmplx -o ${rname}_inv --spec -t 2
	echo " "
endif
if (${lcwater} == 1) then
	if (! -e ${rname}_water.cmplx) then
		cp ../${rname}_water.cmplx .
		cp ../${rname}_water.ddf .
	endif
	if ($ -e ${ranme}_water_inv.cmplx) then
		svk_fft -i ${rname}_water.cmplx -o ${rname}_water_inv --spec -t 2
	endif
endif

if (${lcsetup} == 1) then
	svk_lcmodel_writer.dev -i ${rname}_inv.ddf -o ${rname}_inv --basis ${lcbasis}
	echo "*** No tramp correction ***"
	
	if ($lcwater == 1) then
		svk_lcmodel_writer.dev -i ${rname}_water_inv.ddf -o ${rname}_water_inv --basis ${lcbasis}
		/bin/rm ${rname}_water_inv*.control
	endif
#	set trampw = `grep -w TRAMP ${rname}.raw | cut -d"=" -f2`
#	if ($trampw != $tramporig) then
#		if (-e ${rname}_test.raw) then
#			/bin/rm ${rname}_test.raw
#		endif
#		echo "replace TRAMP from $trampw to $tramporig"
#		sed -e s/TRAMP=${trampw}/TRAMP=${tramporig}/ ${rname}.raw > ${rname}_test.raw	
#		mv ${rname}_test.raw	${rname}.raw
#	endif

	set offset = `grep -w "frequency offset"  ${rname}_inv.ddf | cut -d":" -f2`
	set offset = `echo $offset | awk '{print $1}' | cut -d"." -f1`
	set tempppm = `grep "ppm reference" ${rname}_inv.ddf | cut -d":" -f2`
	set centerppm = `echo $tempppm | awk '{print $1}'`										

	set sweep = `grep -w "sweepwidth" ${rname}.ddf | cut -d":" -f2`
	set sweep = `echo $sweep |  awk '{print $1}'`
	set fieldfreq = `grep -w "center frequency" ${rname}.ddf | cut -d":" -f2`
	set fieldfreq = `echo $fieldfreq |  awk '{print $1}'`
	set rppm = `arithmetic $sweep / $fieldfreq`
	set rppm = `arithmetic $rppm / 2`
	set lend = `arithmetic $centerppm - $rppm`
	set lendd = `echo $lend | cut -d"." -f1`
	set lende = `echo $lend | cut -d"." -f2 | cut -c1`

	if (($lendd =~ 1)) then
		set ppmst = 4.1
   		 set ppmend = 1.8
	else	
		if ($lendd == 0) then
			if (($lende == 1) || ($lende ==0)) then
				set ppmst = 4.1
				set ppmend = 0.2
			else
				set ppmst = 4.1
    			set ppmend = 0.5
    		endif
    	else
    		set ppmst = 4.1
    		set ppmend = 0.2
    	endif
	endif

	set controllist = `ls *.control`
	set ncontrol = `ls *.control | wc -l`
	if (${%controllist} > 0) then
		set nc = 1
		set cexample = `echo $controllist | cut -d" " -f${nc}`
		set cexamplecenter = `grep -i ppmcen $cexample`
		if (${%cexamplecenter} == 0) then
			echo "	Changing control files"										
			while ($nc <= $ncontrol)
				set tempcontrol = `echo $controllist | cut -d" " -f${nc}`
				echo $tempcontrol
			
				if (${datatype} == 3tlong) then
					edit_control_use1.x $tempcontrol 3 "'Cho','NAA','Cr'"
				endif
				if (${datatype} == 3tshort) then
					edit_control_use1.x $tempcontrol 5 "'Cho','NAA','Cr','Glu','mI'"
				endif
				if (${datatype} == 7tgaba) then
					edit_control_use1.x $tempcontrol 3 "'NAA','Glu','GABA'"
				endif
				if (${datatype} == 7tshort) then
					edit_control_use1.x $tempcontrol 5 "'NAA','GPC','Cr','mI','Glu'"
				endif
												
				echo " PPMCEN = $centerppm" 
				if ($offset > 0) then
					sed "4 i\ PPMCEN = $centerppm" $tempcontrol > ${tempcontrol}2
					mv ${tempcontrol}2 $tempcontrol
				endif
				
				sed "15 i\ NRATIO = 0" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
				if ((${datatype} == 7tshort) | (${datatype} == 3tshort)) then
					sed "16 i\ DKNTMN = 0.25" $tempcontrol > ${tempcontrol}2
				else
					sed "16 i\ DKNTMN = 0.10" $tempcontrol > ${tempcontrol}2
				endif
				mv ${tempcontrol}2 $tempcontrol
				sed "17 i\ SDDEGP = 6.00" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
				sed "18 i\ DEGPPM = 0.00" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
				sed "19 i\ DEGZER = 0.00" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
				sed "20 i\ SDDEGZ = 20.00" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
				sed "21 i\ LPRINT = 6" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
				sed "22 i\ FILPRI = ${rname}_LCM_metab.PRINT" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
				sed "2 i\ PPMST = $ppmst" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
				sed "3 i\ PPMEND = $ppmend" $tempcontrol > ${tempcontrol}2
				mv ${tempcontrol}2 $tempcontrol
																	
				if (${lcwater} == 1) then
					sed "27 i\ ATTMET = 1" $tempcontrol > ${tempcontrol}2
					mv ${tempcontrol}2 $tempcontrol
					sed "28 i\ ATTH2O = 1" $tempcontrol > ${tempcontrol}2
					mv ${tempcontrol}2 $tempcontrol
					sed "29 i\ DOWS = T" $tempcontrol > ${tempcontrol}2
					mv ${tempcontrol}2 $tempcontrol
					sed "30 i\ DOECC = T" $tempcontrol > ${tempcontrol}2
					mv ${tempcontrol}2 $tempcontrol
					sed "31 i\ FILH2O = ${rname}_water_inv.raw" $tempcontrol > ${tempcontrol}2
					mv ${tempcontrol}2 $tempcontrol
				endif 


				@ nc++
			end
		endif
	else
		echo "	Grid analysis has not been started"										
	endif
endif

if (${lcquant} == 1) then
	echo "	running lcmodel for ${rname}_inv"
	qsub ${rname}_inv.grid
endif					    			  
     		
set ncontrol = `ls *.control | wc -l`
set nps = `ls *.ps | wc -l`
if ((${%ncontrol} > 0) & (${%nps} > 0)) then
	@ ndiff++
	echo "	$ncontrol control / $nps PS ($ndiff)" 	 
endif
					
     							
if (${lcconvert} == 1) then
   	set a = `ls ${rname}_inv*.csv`
   	set na = `ls ${rname}_inv*.csv | wc -l`
   	set nna = 1
   	while ($nna <= $na)
   		set fsize = `ls -ltr $a[$nna]`
   		set fsize = `echo $fsize | cut -d" " -f5`
   		if ($fsize > 0) then
   			set metfile1 = $a[$nna]
			head -1 $a[$nna] > ${rname}_inv_header.csv	
			break	
		else
			@ nna++
		endif	
	end		
	
	if (! -e ${rname}_LCM_phased.cmplx) then
		set a = `ls ${rname}_inv_*coord`
		svk_lcmodel_reader.dev -i ${rname}.ddf --coord $a[1] -o ${rname}
		svk_file_convert.dev -i ${rname}_LCM_fit.dcm -o ${rname}_LCM_fit -t 2
		svk_file_convert.dev -i ${rname}_LCM_phased.dcm -o ${rname}_LCM_phased -t 2
		svk_file_convert.dev -i ${rname}_LCM_baseline.dcm -o ${rname}_LCM_baseline -t 2
	endif
	if (! -e ${rname}_LCM_cor.cmplx) then
		svk_spec_diff --s1 ${rname}_LCM_phased.cmplx --s2 ${rname}_LCM_fit.cmplx -o ${rname}_LCM_residual 
		svk_spec_diff --s1 ${rname}_LCM_fit.cmplx --s2 ${rname}_LCM_baseline.cmplx -o ${rname}_LCM_cor
	endif
	
	if (! -e LCM_Met) then
		mkdir LCM_Met
	endif
	if (! -e LCM_Met/${rname}_LCM_NAA.real) then
		set ncsvcol = `awk -F, '{print NF}' ${rname}_inv_header.csv`
		set headf = `cat ${rname}_inv_header.csv`
		set i = 3
		set j = 1
		set metall =
		while ($i <= $ncsvcol)
        	set met = `echo $headf | cut -d"," -f$i`
        	echo "$i $j $met Converting"
        	svk_lcmodel_reader.dev -i ${rname}.ddf --met $met --csv $metfile1 -o ${rname}_LCM_$met 
			svk_lcmodel_reader.dev -i ${rname}.ddf --met "$met %SD" --csv $metfile1 -o ${rname}_LCM_${met}SD
			svk_lcmodel_reader.dev -i ${rname}.ddf --met "$met/Cr" --csv $metfile1 -o ${rname}_LCM_${met}Cr	
			svk_file_convert.dev -i ${rname}_LCM_${met}.dcm -o ${rname}_LCM_${met} -t 3
			svk_file_convert.dev -i ${rname}_LCM_${met}SD.dcm -o ${rname}_LCM_${met}SD -t 3
			svk_file_convert.dev -i ${rname}_LCM_${met}Cr.dcm -o ${rname}_LCM_${met}Cr -t 3
        	@ i++
        	@ i++
        	@ i++
        	@ j++
        	set metall = `echo $metall $met`
        	mv ${rname}_LCM_${met}* LCM_Met
		end
		echo "Results Converted: $metall"
	endif
	
endif
