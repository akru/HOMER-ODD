# SSC32 Servo Controller
import time

class SSC32Controller:
    """ SSC32 controller communication """
    def __init__(self, numServo, sock):
        self._nums = numServo
        self._sock = sock
        self._pvec = []
        self._time = 2000

    def setPositionVector(self, vect):
        """ Set servo position """
        self._pvec = vect

    def setTimeDuration(self, time):
        """ Set duration of movements """
        self._time = time

    def flush(self):
        """ Send state to SSC32 """
        for servo in range(self._nums):
            self._sock.send("#%d P%d" % (servo, self._pvec[servo]))
        self._sock.send(" T%d\r" % self._time)

    def positionIsSet(self):
        """ Verify position state """
        self._sock.send("Q\r")
        if self._sock.recv(1) == ".":
            return True
        return False
