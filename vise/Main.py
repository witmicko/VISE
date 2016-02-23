import sys

import time
from PyQt4 import QtGui,QtCore

from vise.ui import main_window
from vise.vision.CameraDevice import CameraDevice


class ViseApp(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ViseApp, self).__init__(parent)
        self.setupUi(self)


    @QtCore.pyqtSlot(QtGui.QImage)
    def set_image(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image_view.setPixmap(QtGui.QPixmap.fromImage(image))
        # if image.size() != self.size():
        #     self.setFixedSize(image.size())
        self.update()


def main():
    app = QtGui.QApplication(sys.argv)
    thread = QtCore.QThread()
    thread.start()

    cam = CameraDevice()
    # cam.capture_no_thread()
    cam.moveToThread(thread)

    main_window = ViseApp()

    # main.preview_on.toggled.connect(cam.capture_no_thread)

    cam.video_signal.connect(main_window.set_image)


    # main.preview_on.clicked.connect(cam.capture_no_thread)
    # main.preview_off.clicked.disconnect(cam.capture_no_thread)



    main_window.show()
    app.exec_()

if __name__ == '__main__':
   main()
