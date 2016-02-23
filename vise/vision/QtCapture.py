import cv2
from PyQt4 import QtGui, QtCore


class QtCapture(QtGui.QWidget):
    def __init__(self, *args):
        super(QtGui.QWidget, self).__init__()

        self.fps = 24
        self.cap = cv2.VideoCapture(*args)

        self.video_frame = QtGui.QLabel()
        lay = QtGui.QVBoxLayout()
        lay.setMargin(0)
        lay.addWidget(self.video_frame)
        self.setLayout(lay)

    def setFPS(self, fps):
        self.fps = fps

    def nextFrameSlot(self):
        ret, frame = self.cap.read()
        # My webcam yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)

    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./self.fps)

    def stop(self):
        self.timer.stop()

    def deleteLater(self):
        self.cap.release()
        super(QtGui.QWidget, self).deleteLater()