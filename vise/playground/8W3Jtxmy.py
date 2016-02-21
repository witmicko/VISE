#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui
import cv2
import numpy as np
import sys

#Importing necessary libraries, mainly the OpenCV, and PyQt libraries

from PyQt4.QtCore import pyqtSignal

from vise.playground.ImageViewer import ImageViewer
from vise.playground.ShowVideo import ShowVideo

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