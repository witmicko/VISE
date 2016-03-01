# -*- coding: utf-8 -*-
import cv2
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL

from vise.utils.Emitter import Emitter

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtCore.QObject):
    def __init__(self, mother_pipe, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.emitter = Emitter(mother_pipe)
        self.emitter.daemon = True
        self.emitter.start()

    def setupUi(self, MainWindow):
        # MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 290, 306, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setIndent(0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(15, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.preview_on = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.preview_on.setChecked(False)
        self.preview_on.setAutoExclusive(False)
        self.preview_on.setObjectName(_fromUtf8("preview_on"))
        self.horizontalLayout_2.addWidget(self.preview_on)
        self.preview_off = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.preview_off.setChecked(True)
        self.preview_off.setAutoExclusive(False)
        self.preview_off.setObjectName(_fromUtf8("preview_off"))
        self.horizontalLayout_2.addWidget(self.preview_off)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setIndent(0)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(15, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.can_bus_on = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.can_bus_on.setChecked(False)
        self.can_bus_on.setAutoExclusive(False)
        self.can_bus_on.setObjectName(_fromUtf8("can_bus_on"))
        self.horizontalLayout_4.addWidget(self.can_bus_on)
        self.can_bus_off = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.can_bus_off.setChecked(True)
        self.can_bus_off.setAutoExclusive(False)
        self.can_bus_off.setObjectName(_fromUtf8("can_bus_off"))
        self.horizontalLayout_4.addWidget(self.can_bus_off)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setIndent(0)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem2 = QtGui.QSpacerItem(15, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.trace_on = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.trace_on.setChecked(False)
        self.trace_on.setAutoExclusive(False)
        self.trace_on.setObjectName(_fromUtf8("trace_on"))
        self.horizontalLayout_6.addWidget(self.trace_on)
        self.trace_off = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.trace_off.setChecked(True)
        self.trace_off.setAutoExclusive(False)
        self.trace_off.setObjectName(_fromUtf8("trace_off"))
        self.horizontalLayout_6.addWidget(self.trace_off)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        #image view
        self.group_box = QtGui.QGroupBox(self.centralwidget)
        self.group_box.setGeometry(QtCore.QRect(60, 20, 601, 251))
        self.group_box.setObjectName(_fromUtf8("group_box"))
        self.image_view = QtGui.QLabel(self.group_box)
        self.image_view.setGeometry(QtCore.QRect(0, 0, 601, 251))
        self.image_view.setFrameShadow(QtGui.QFrame.Raised)
        self.image_view.setObjectName(_fromUtf8("label"))
        self.image_view.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)


        #trace
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 390, 721, 181))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # slots and connections
        self.preview_on.clicked.connect(self.preview_off.toggle)
        self.preview_on.clicked.connect(self.test)
        self.preview_off.clicked.connect(self.preview_on.toggle)

        self.can_bus_on.clicked.connect(self.can_bus_off.toggle)
        self.can_bus_off.clicked.connect(self.can_bus_on.toggle)

        self.trace_on.clicked.connect(self.trace_off.toggle)
        self.trace_off.clicked.connect(self.trace_on.toggle)

        self.connect(self.emitter, SIGNAL('data(QImage)'), self.set_image)

        # self.connect(self.emitter, SIGNAL('data(int)'), self.set_image)
        # self.connect(self.emitter, SIGNAL('data(int)'), self.test)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Preview", None))
        self.preview_on.setText(_translate("MainWindow", "on", None))
        self.preview_off.setText(_translate("MainWindow", "off", None))
        self.label_4.setText(_translate("MainWindow", "CAN bus", None))
        self.can_bus_on.setText(_translate("MainWindow", "on", None))
        self.can_bus_off.setText(_translate("MainWindow", "off", None))
        self.label_6.setText(_translate("MainWindow", "Debug trace", None))
        self.trace_on.setText(_translate("MainWindow", "on", None))
        self.trace_off.setText(_translate("MainWindow", "off", None))

    # def paintEvent(self, event):
    #     painter = QtGui.QPainter(self)
    #     painter.drawImage(0,0, self.image)
    #     self.image = QtGui.QImage()
    def test(self,int):
        print(int)

    def set_image(self, qt_image):
        print("set Image")
        if qt_image.isNull():
            print("Viewer Dropped frame!")

        pixmap = QtGui.QPixmap.fromImage(qt_image)
        size = self.image_view.size()
        width = size.width()
        height = size.height()
        # print(width)
        pixmap_scaled = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding)
        self.image_view.setPixmap(pixmap_scaled)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0,0, self.image)
        self.image = QtGui.QImage()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
