import sys

import time
from PyQt4 import QtGui,QtCore

from vise.ui import main_window3
from vise.vision.CameraDevice import CameraDevice


class ExampleApp(QtGui.QMainWindow, main_window3.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)
    thread = QtCore.QThread()
    thread.start()

    cam = CameraDevice()
    # cam.capture_no_thread()
    cam.moveToThread(thread)

    main = ExampleApp()

    # main.preview_on.toggled.connect(cam.capture_no_thread)
    cam.video_signal.connect(main.set_image())
    main.preview_on.clicked.connect(cam.capture_no_thread)
    # main.preview_off.clicked.disconnect(cam.capture_no_thread)



    main.show()
    app.exec_()

if __name__ == '__main__':
   main()
