from ssc32_controller import SSC32Controller
from positions import *
import thread, time

class HOMER:
    def __init__(self, sock):
        self._c = SSC32Controller(14, sock)
        self.setPos(defaultPosition)
        self._status = "HOMER: Initialisation complete."
        self._pid = None

    def startRoutine(self):
        if self._pid == None:
            self._pid = thread.start_new_thread(self.mainRoutine, ())

    def getStatus(self):
        return self._status

    def setPos(self, pos):
        self._c.setPositionVector(pos)
        self._c.flush()
        while not self._c.positionIsSet():
            time.sleep(0.5)

    def mainRoutine(self):
        self._status = "HOMER: Start main routine"

        self._c.setTimeDuration(2000)
        routine = [pos0, pos1, pos2, pos3]
        for pos in routine:
            self._status = self._status + "."
            self.setPos(pos)

        routine = [pos4, pos5]
        for pos in routine:
            self._status = self._status + "."
            self.setPos(pos)

        self._c.setTimeDuration(1000)
        for i in range(3):
            for pos in [pos6, pos7]:
                self.setPos(pos)
        time.sleep(5)
        self.setPos(defaultPosition)
        self._status = "HOMER: Main routine complete."
        self._pid = None
