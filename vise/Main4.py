import sys
import os

import signal
import atexit
import time

import psutil
from PyQt4.QtCore import QProcess
from PyQt4.QtGui import QApplication, QMainWindow

from vise.vision.CameraDeviceProcess import CameraDevice
from vise.ui.main_window import Ui_MainWindow
from multiprocessing import Pipe


class Main:
    def __init__(self):
        self.app = QApplication(sys.argv)
        mother_pipe, child_pipe = Pipe()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow(mother_pipe)
        self.ui.setupUi(self.window)
        self.cam = CameraDevice(child_pipe)
        self.cam.daemon = True
        self.cam.setProcessChannelMode(QProcess.);
        self.cam.start()

        # self.processes = []
        atexit.register(self.cleanup)
        self.runner()

    def runner(self):
        self.window.show()
        sys.exit(self.app.exec_())

    def cleanup(self):
        print("cleanup")
        self.cam.stopped = True
        # self.cam.release_cam()
        time.sleep(5)
        pid = self.cam.get_pid()
        p = psutil.Process(pid)
        # p.kill
        p.terminate
        # cam = self.processes[0]
        print("killed all")
        # cam_process = psutil.Process(cam.pid)
        # cam_process.kill

if __name__ == '__main__':
    Main()