import signal
import sys
import atexit
import time
from PyQt4.QtGui import QApplication, QDialog, QMainWindow
from PyQt4.QtCore import QThread, SIGNAL
from vise.vision.CameraDeviceProcess import CameraDevice
from vise.ui.main_window import Ui_MainWindow
from multiprocessing import Process, Queue, Pipe
from vise.utils.Emitter import Emitter



if __name__ == '__main__':

    app = QApplication(sys.argv)
    mother_pipe, child_pipe = Pipe()
    queue = Queue()
    emitter = Emitter(mother_pipe)

    window = QMainWindow()
    ui = Ui_MainWindow(queue,emitter)
    ui.setupUi(window)
    # ui.connect(ui.emitter, SIGNAL('data(QImage)'), ui.set_image)
    # form = Form(queue, emitter)
    CameraDevice(child_pipe, queue).start()
    # ChildProc(child_pipe, queue).start()
    # form.show()
    window.show()
    app.exec_()