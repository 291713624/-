# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '模式选择.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import 登录
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
import requests
import optparse
import json
class moshi(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(821, 429)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 771, 381))
        self.label.setStyleSheet("image: url(:/f/photo/模式选择.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 40, 61, 31))
        self.pushButton_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 121, 151))
        self.pushButton.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 150, 121, 151))
        self.pushButton_2.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 150, 121, 151))
        self.pushButton_4.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 150, 121, 151))
        self.pushButton_5.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.pushButton.show)
        self.pushButton_2.clicked.connect(self.pushButton_2.show)
        self.pushButton_4.clicked.connect(self.pushButton_4.show)
        self.pushButton_5.clicked.connect(self.pushButton_5.show)
        self.pushButton_3.clicked.connect(self.pushButton_3.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import file
if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QIcon

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon('web.png'))  # 增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())
