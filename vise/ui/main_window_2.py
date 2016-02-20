# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\witmi\PycharmProjects\Vise\ui_pyqt\main_window.ui'
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
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(600, 10, 171, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setIndent(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(15, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
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
        spacerItem1 = QtGui.QSpacerItem(15, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cam_preview_on_btn = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.cam_preview_on_btn.setChecked(True)
        self.cam_preview_on_btn.setObjectName(_fromUtf8("cam_preview_on_btn"))
        self.horizontalLayout_2.addWidget(self.cam_preview_on_btn)
        self.cam_preview_off_btn = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.cam_preview_off_btn.setObjectName(_fromUtf8("cam_preview_off_btn"))
        self.horizontalLayout_2.addWidget(self.cam_preview_off_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setIndent(0)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(15, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.radioButton_7 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.horizontalLayout_4.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.horizontalLayout_4.addWidget(self.radioButton_8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setIndent(0)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem3 = QtGui.QSpacerItem(15, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.radioButton_11 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_11.setChecked(True)
        self.radioButton_11.setObjectName(_fromUtf8("radioButton_11"))
        self.horizontalLayout_6.addWidget(self.radioButton_11)
        self.radioButton_12 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_12.setObjectName(_fromUtf8("radioButton_12"))
        self.horizontalLayout_6.addWidget(self.radioButton_12)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Preview", None))
        self.radioButton_2.setText(_translate("MainWindow", "on", None))
        self.radioButton.setText(_translate("MainWindow", "off", None))
        self.label_2.setText(_translate("MainWindow", "Preview", None))
        self.cam_preview_on_btn.setText(_translate("MainWindow", "on", None))
        self.cam_preview_off_btn.setText(_translate("MainWindow", "off", None))
        self.label_4.setText(_translate("MainWindow", "Preview", None))
        self.radioButton_7.setText(_translate("MainWindow", "on", None))
        self.radioButton_8.setText(_translate("MainWindow", "off", None))
        self.label_6.setText(_translate("MainWindow", "Preview", None))
        self.radioButton_11.setText(_translate("MainWindow", "on", None))
        self.radioButton_12.setText(_translate("MainWindow", "off", None))
