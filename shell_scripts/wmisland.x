
#! /bin/csh -f

erode_image.x $1_wm.byt $1_wme.byt 2
mask_connect $1_wme $1_wm 15 4

