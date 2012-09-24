#!/bin/sh

##
#
# Homer - ODD start script
#
##


./tsr.py -b 115200 /dev/ttyUSB0 &
./odd.py &
feh -Z -F -R 1 shot.jpg

