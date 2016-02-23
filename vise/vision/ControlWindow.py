from PyQt4 import QtGui, QtCore

from vise.vision.QtCapture import QtCapture


class ControlWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.capture = None

        self.start_button = QtGui.QPushButton('Start')
        self.start_button.clicked.connect(self.startCapture)
        self.quit_button = QtGui.QPushButton('End')
        self.quit_button.clicked.connect(self.endCapture)
        self.end_button = QtGui.QPushButton('Stop')

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)
        self.setLayout(vbox)
        self.setWindowTitle('Control Panel')
        self.setGeometry(100,100,200,200)
        self.show()

    def startCapture(self):
        if not self.capture:
            self.capture = QtCapture(0)
            self.end_button.clicked.connect(self.capture.stop)
            # self.capture.setFPS(1)
            self.capture.setParent(self)
            self.capture.setWindowFlags(QtCore.Qt.Tool)
        self.capture.start()
        self.capture.show()

    def endCapture(self):
        self.capture.deleteLater()
        self.capture = None


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = ControlWindow()
    sys.exit(app.exec_())