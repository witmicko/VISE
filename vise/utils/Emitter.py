from PyQt4 import QtGui
from threading import Thread
from multiprocessing import Pipe
import cv2

from PyQt4.QtCore import QObject, SIGNAL


class Emitter(QObject, Thread):
    def __init__(self, pipe, parent=None):
        QObject.__init__(self,parent)
        Thread.__init__(self)
        self.pipe = pipe

    def _emit(self, signature, args=None):
        # print("emit ",signature, args)
        if args:
            self.emit(SIGNAL(signature), args)
        else:
            self.emit(SIGNAL(signature))

    def run(self):
        while True:
            try:
                signature, data = self.pipe.recv()
                if signature == 'data(QImage)':
                    color_swapped_image = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
                    height, width, _ = color_swapped_image.shape

                    qt_image = QtGui.QImage(color_swapped_image.data,
                                            width,
                                            height,
                                            color_swapped_image.strides[0],
                                            QtGui.QImage.Format_RGB888)
                    # print(height, width)
                    self._emit('data(QImage)', qt_image)

            except EOFError:
                break
            # else:
                # self._emit(*signature)

    def send(self, signature, data):
        # print("send", signature, data)
        self.pipe.send((signature, data))
