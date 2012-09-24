#!/usr/bin/env python
#from bluetooth import BluetoothSocket, RFCOMM
from homer import HOMER
from fd import face_detect
import socket, os, time

#BLUETOOTH_ADDR = "00:0A:84:02:5F:47"

if __name__ == '__main__':
#	sock = BluetoothSocket( RFCOMM )
#	sock.connect((BLUETOOTH_ADDR, 1))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('', 7777))
    homer = HOMER(sock)
    while 1:
        os.system("fswebcam -d /dev/video1 --title \"H.O.M.E.R. - Open Door Day\" -r 640x480 -F 2 -S 1 -q shot.jpg")
        if face_detect("shot.jpg"):
            homer.startRoutine()
            time.sleep(5)
        else:
            time.sleep(0.5)
