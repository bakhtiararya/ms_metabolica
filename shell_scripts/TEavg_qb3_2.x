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

/home/liyan/script/idl/comb_ac2.x $2 $1 avg
/home/liyan/script/idl/comb_ac2.x $2 $1 cor

idl /home/liyan/script/idl/runTE_avg_proc.pro



