#!/usr/bin/env python
#from bluetooth import BluetoothSocket, RFCOMM
from homer import HOMER
from fd import face_detect
import socket, os

#BLUETOOTH_ADDR = "00:0A:84:02:5F:47"

if __name__ == '__main__':
#	sock = BluetoothSocket( RFCOMM )
#	sock.connect((BLUETOOTH_ADDR, 1))
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('', 50007))
    while 1:
        os.system("fswebcam --no-banner --jpeg 40 -F 2 -S 1 -q shot.jpg")
        if face_detect("shot.jpg"):
            homer.startRoutine()
            time.sleep(5)
        else:
            time.sleep(0.5)