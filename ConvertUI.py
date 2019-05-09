# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Convert.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(270, 200, 101, 51))
        self.exitButton.setObjectName("exitButton")
        self.calcButton = QtWidgets.QPushButton(self.centralwidget)
        self.calcButton.setGeometry(QtCore.QRect(100, 200, 101, 51))
        self.calcButton.setObjectName("calcButton")
        self.xEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.xEdit.setGeometry(QtCore.QRect(140, 70, 181, 31))
        self.xEdit.setObjectName("xEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 120, 21, 21))
        self.label_2.setObjectName("label_2")
        self.yEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yEdit.setGeometry(QtCore.QRect(140, 110, 181, 31))
        self.yEdit.setObjectName("yEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        self.calcButton.clicked.connect(MainWindow.calc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.calcButton.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "X:"))
        self.label_2.setText(_translate("MainWindow", "Y:"))

