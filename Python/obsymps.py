# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obsymps.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 365)
        MainWindow.setStyleSheet("color: rgb(170, 0, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 290, 431, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(670, 40, 21, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(670, 80, 21, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(670, 120, 21, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(670, 160, 21, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 641, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 631, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 531, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 601, 21))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 541, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(670, 200, 21, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(530, 0, 161, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 131, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 531, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(670, 240, 21, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Observable Symptoms"))
        self.pushButton.setText(_translate("MainWindow", "Store Observable Symptoms in Data base"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.lineEdit_4.setText(_translate("MainWindow", "0"))
        self.lineEdit_5.setText(_translate("MainWindow", "0"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Does the patient have problem with eye to eye contact?(1:Yes, 0:No)"))
        self.label_4.setText(_translate("MainWindow", "Does the patient not responding properly, when called?(1:Yes, 0:No)"))
        self.label_5.setText(_translate("MainWindow", "Does the patient spending mostly alone?(1:Yes, 0:No)"))
        self.label_6.setText(_translate("MainWindow", "Does the patient engages in imaginative Play?(1:Yes, 0:No)"))
        self.label_2.setText(_translate("MainWindow", "Does the patient have any epilepsy problem?(1:Yes, 0:No)"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.lineEdit_9.setText(_translate("MainWindow", "000001"))
        self.label_7.setText(_translate("MainWindow", "Patient ID:"))
        self.label_8.setText(_translate("MainWindow", "Does the patient suffering from depression?(1:Yes, 0:No)"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))


