#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importing necessary libraries, mainly the OpenCV, and PyQt libraries
import cv2
import numpy as np
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
# from PyQt4 import QtWidgets
from PyQt4.QtCore import pyqtSignal

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


class ImageViewer(QtGui.QWidget):
    def __init__(self, parent = None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)


    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0,0, self.image)
        self.image = QtGui.QImage()

    def initUI(self):
        self.setWindowTitle('Test')

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)
    image_viewer = ImageViewer()

    vid.VideoSignal.connect(image_viewer.setImage)

    #Button to start the videocapture:

    push_button = QtGui.QPushButton('Start')
    push_button.clicked.connect(vid.startVideo)
    vertical_layout = QtGui.QVBoxLayout()

    vertical_layout.addWidget(image_viewer)
    vertical_layout.addWidget(push_button)

    layout_widget = QtGui.QWidget()
    layout_widget.setLayout(vertical_layout)

    main_window = QtGui.QMainWindow()
    main_window.setCentralWidget(layout_widget)
    main_window.show()
    sys.exit(app.exec_())