import signal
import sys
import atexit
import time
from PyQt4.QtGui import QApplication, QDialog, QMainWindow
from PyQt4.QtCore import QThread
from vise.vision.CameraDevice import CameraDevice
from vise.ui.main_window import Ui_MainWindow


def exit_gracefully():
    signal.signal(signal.SIGINT, original_sigint)
    sys.exit(1)
    signal.signal(signal.SIGINT, exit_gracefully)


def runner():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    cam = CameraDevice()
    thread = QThread()
    cam.moveToThread(thread)
    thread.start()
    thread.setPriority(QThread.LowestPriority)
    atexit.register(cam.capture.release)
    cam.video_signal.connect(ui.set_image)
    ui.preview_on.clicked.connect(cam.preview_on)
    ui.preview_on.clicked.connect(cam.startVideo)
    ui.preview_off.clicked.connect(cam.preview_off)
    # ui.preview_off.clicked.disconnect(cam.startVideo)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    runner()
    # app = QApplication(sys.argv)
    # window = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(window)
    # cam = CameraDevice()
    # thread = QThread()
    # cam.moveToThread(thread)
    # thread.start()
    # thread.setPriority(QThread.LowestPriority)
    # # atexit.register(cam.capture.release)
    # cam.video_signal.connect(ui.set_image)
    # ui.preview_on.clicked.connect(cam.preview_on)
    # ui.preview_on.clicked.connect(cam.startVideo)
    # ui.preview_off.clicked.connect(cam.preview_off)
    # # ui.preview_off.clicked.disconnect(cam.startVideo)
    # window.show()
    # sys.exit(app.exec_())