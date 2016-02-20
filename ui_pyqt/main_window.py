# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(470, 150, 306, 80))
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
        self.image_view = QtGui.QMdiArea(self.centralwidget)
        self.image_view.setGeometry(QtCore.QRect(10, 20, 441, 431))
        self.image_view.setObjectName(_fromUtf8("image_view"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.preview_on, QtCore.SIGNAL(_fromUtf8("clicked()")), self.preview_off.toggle)
        QtCore.QObject.connect(self.preview_off, QtCore.SIGNAL(_fromUtf8("clicked()")), self.preview_on.toggle)
        QtCore.QObject.connect(self.can_bus_on, QtCore.SIGNAL(_fromUtf8("clicked()")), self.can_bus_off.toggle)
        QtCore.QObject.connect(self.can_bus_off, QtCore.SIGNAL(_fromUtf8("clicked()")), self.can_bus_on.toggle)
        QtCore.QObject.connect(self.trace_on, QtCore.SIGNAL(_fromUtf8("clicked()")), self.trace_off.toggle)
        QtCore.QObject.connect(self.trace_off, QtCore.SIGNAL(_fromUtf8("clicked()")), self.trace_on.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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

