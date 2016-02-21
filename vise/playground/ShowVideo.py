import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import cv2
import numpy as np

class ShowVideo(QtCore.QObject):

    #initiating the built in camera
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent = None):
        super(ShowVideo, self).__init__(parent)

    @QtCore.pyqtSlot()
    def startVideo(self):

        run_video = True
        while run_video:
            ret, image = self.camera.read()

            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            height, width, _ = color_swapped_image.shape

            qt_image = QtGui.QImage(color_swapped_image.data,
                                    width,
                                    height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)

            self.VideoSignal.emit(qt_image)