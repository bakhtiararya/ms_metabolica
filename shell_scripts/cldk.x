#!/bin/csh -f

# $Header: written by Yan Li 

switch ($#argv)
  case 2
     set root = $1
     set cl_type = $2
  breaksw
  case 1
     set root = $1
     set cl_type = 0
  breaksw
  default:
    echo Usage: cldk.x rootname cl_type
    echo "      cl_type = 0 (default) or 1 (whole)"
    exit 1
endsw


set chan = 32

set tempc = `arithmetic $chan + $chan`
set tempc = `echo $tempc | cut -d"." -f1`

set tempc2 =  `arithmetic $tempc + $tempc`
set tempc2 = `echo $tempc2 | cut -d"." -f1`

set num = 1
while ($num <= $tempc)
    foreach fext (cmplx ddf cmplx.gz)
        if (-e $1_${num}.${fext}) then
	    echo "deleting $1_${num}.${fext}"
	    /bin/rm $1_${num}.${fext}
        endif
    end
    foreach ftag (fb phased cor cor_back cor_selbox selbox)
		foreach fext (cmplx ddf cmplx.gz)
             set fname = $1_${num}_${ftag}.${fext}
	     if (-e ${fname}) then
		echo "deleting ${fname}"
		/bin/rm ${fname}
             endif
        end
    end	 
    foreach ftag (cor cor_back cor_selbox selbox)
		foreach fext (cmplx ddf cmplx.gz)
            set fname = $1_${num}_dif_${ftag}.${fext}
	     	if (-e ${fname}) then
				echo "deleting ${fname}"
				/bin/rm ${fname}
             endif
        end
    end	 
    set num = `arithmetic $num + 1`
    set num = `echo $num | cut -d"." -f1`
end


set num = 1
while ($num <= $tempc2)
    foreach fext (cmplx ddf cmplx.gz)
        if (-e $1_${num}.${fext}) then
	    echo "deleting $1_${num}.${fext}"
	    /bin/rm $1_${num}.${fext}
        endif
    end
    foreach ftag (bas1 bas2 dif water)
		foreach fext (cmplx ddf cmplx.gz)
             set fname = $1_${ftag}_${num}.${fext}
	     if (-e ${fname}) then
		echo "deleting ${fname}"
		/bin/rm ${fname}
             endif
        end
    end	 
    foreach ftag (fb)
		foreach fext (cmplx ddf cmplx.gz)
             set fname = $1_${num}_${ftag}.${fext}
	     if (-e ${fname}) then
		echo "deleting ${fname}"
		/bin/rm ${fname}
             endif
        end
    end	 
    set num = `arithmetic $num + 1`
    set num = `echo $num | cut -d"." -f1`
end



set num = 1
while ($num <= $chan)
     foreach ftag (fb_cmb fb_cmb_phased fb_cmb_correct fb_cmb_cor_back fb_cmb_cor)
         foreach fext (cmplx ddf cmplx.gz)
	    set fname = $1_${num}_${ftag}.${fext}
            if (-e ${fname}) then
		echo "deleting ${fname}"
                /bin/rm ${fname}
            endif
         end
     end
     if (-e $1_${num}_cor_met) then
	echo "deleting $1_${num}_cor_met"
	 /bin/rm -r $1_${num}_cor_met
     endif
     set num = `arithmetic $num + 1`
     set num = `echo $num | cut -d"." -f1`
end

set num = 1
while ($num <= $chan)
	 foreach cycles (cyc1 cyc2)
     	foreach ftag (fb_cmb fb_cmb_phased fb_cmb_correct fb_cmb_cor_back fb_cmb_cor)
         	foreach fext (cmplx ddf cmplx.gz)
	    		set fname = $1_${cycles}_${num}_${ftag}.${fext}
           		if (-e ${fname}) then
					echo "deleting ${fname}"
                	/bin/rm ${fname}
            	endif
         	end
     	end
     end
     if (-e $1_${num}_cor_met) then
		echo "deleting $1_${num}_cor_met"
		/bin/rm -r $1_${cycles}_${num}_cor_met
     endif
     set num = `arithmetic $num + 1`
     set num = `echo $num | cut -d"." -f1`
end


if (${cl_type} == 1) then
     set num = 1
     while ($num <= $chan)
       foreach fext (cmplx ddf cmplx.gz)
           set fname = $1_${num}_fb_cmb_cor_sum.${fext}
           if (-e $fname) then
		echo "deleting $fname"
		/bin/rm $fname
           endif
       end
      # /bin/rm *_ac_${num}.int2 *_ac_${num}.idf *_ac_${num}r.real *_ac_${num}r.idf
        set num = `arithmetic $num + 1`
        set num = `echo $num | cut -d"." -f1`
     end
endif
