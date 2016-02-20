import sys

import time
from PyQt4 import QtGui,QtCore

from vise.ui import main_window
from vise.vision.CameraDevice import CameraDevice


class ExampleApp(QtGui.QMainWindow, main_window.Ui_MainWindow):
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
    vid = CameraDevice()
    vid.moveToThread(thread)
    image_viewer = ImageViewer()

    vid.video_signal.connect(image_viewer.setImage)

    #Button to start the videocapture:

    push_button = QtGui.QPushButton('Start')
    push_button.clicked.connect(vid.capture_no_thread)
    vertical_layout = QtGui.QVBoxLayout()

    vertical_layout.addWidget(image_viewer)
    vertical_layout.addWidget(push_button)

    layout_widget = QtGui.QWidget()
    layout_widget.setLayout(vertical_layout)

    main_window = QtGui.QMainWindow()
    main_window.setCentralWidget(layout_widget)
    main_window.show()
    sys.exit(app.exec_())
