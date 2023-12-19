filename=$1
export filename

# 3pt,Exp,n
func='n'
export func

# either Vol or anything for phantom
Obj='Phan'
export Obj

# TE increment
Int=40
export Int

idl /home/liyan/script/idl/runTE_avg_signa.pro

cp ../images/$2_ac* .
	


