from PyQt4 import QtGui
from threading import Thread
from multiprocessing import Pipe

import cv2
from PyQt4.QtCore import QObject, SIGNAL


class VisionEmitter(QObject, Thread):
    def __init__(self, pipe, parent=None):
        QObject.__init__(self, parent)
        Thread.__init__(self)
        self.pipe2 = pipe

    def _emit(self, signature, args=None):
        # print("emit ",signature, args)
        if args:
            self.emit(SIGNAL(signature), args)
        else:
            self.emit(SIGNAL(signature))

    def run(self):
        while True:
            try:
                signature, data = self.pipe2.recv()
                print(signature, data)

            except EOFError:
                break
                # else:
                # self._emit(*signature)

    def send(self, signature, data):
        self.pipe2.send((signature, data))
