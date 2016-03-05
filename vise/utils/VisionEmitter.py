from PyQt4 import QtGui
from threading import Thread, Event
from multiprocessing import Pipe

import cv2
from PyQt4.QtCore import QObject, SIGNAL


class VisionEmitter(QObject, Thread):
    def __init__(self, pipe, parent=None):
        QObject.__init__(self, parent)
        Thread.__init__(self)
        self.pipe = pipe
        self.pool = Event()

    def _emit(self, signature, args=None):
        print("_emit ", signature, args)
        # self.emit(SIGNAL(signature), args)
        self.emit(SIGNAL('preview'))

    def run(self):
        while not self.pool.wait(timeout=0.500):
            try:
                signature, data = self.pipe.recv()
                # print('vision emitter recv', signature, data)
                if signature == "preview(bool)":
                    self._emit('preview', "ghj")

            except EOFError:
                break
                # else:
                # self._emit(*signature)

    def send(self, signature, data):
        try:
            self.pipe.send((signature, data))
        except BrokenPipeError:
            pass
