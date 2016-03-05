import signal
import sys
import atexit
import time

import cv2
from PyQt4.QtGui import QApplication, QDialog, QMainWindow
from PyQt4.QtCore import QThread, SIGNAL

from vise.vision.CameraDeviceProcess import CameraDevice
from vise.ui.main_window import Ui_MainWindow
from multiprocessing import Process, Queue, Pipe
from vise.utils.Emitter import Emitter
from vise.utils.VisionEmitter import VisionEmitter


processes =[]
# def exit_gracefully():
#     signal.signal(signal.SIGINT, original_sigint)
#     sys.exit(1)
#     signal.signal(signal.SIGINT, exit_gracefully)


def runner():
    app = QApplication(sys.argv)
    mother_pipe, child_pipe = Pipe()

    window = QMainWindow()
    ui = Ui_MainWindow(mother_pipe)
    ui.setupUi(window)

    # ui.connect(ui.emitter, SIGNAL('data(QImage)'), ui.set_image)
    # form = Form(queue, emitter)
    cam = CameraDevice(child_pipe)
    cam.start()

    processes.append(cam.pid)


    # cam.start()
    # ChildProc(child_pipe, queue).start()
    # form.show()
    window.show()
    app.exec_()

def cleanup():
    print("cleanup")
    for p in processes:
        print(p)

if __name__ == '__main__':
    # original_sigint = signal.getsignal(signal.SIGINT)
    # signal.signal(signal.SIGINT, exit_gracefully)
    atexit.register(cleanup)
    # camera = cv2.VideoCapture(0)
    # camera.release
    runner()
