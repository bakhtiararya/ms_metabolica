filename=$1
export filename

# TE increment
Int=5.0
export Int

# last echo, n=n_te, e=50-200ms, s=last echo depending on SNR
func='s'
export func

idl /home/liyan/script/idl/runTE_7t.pro


