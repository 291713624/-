# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '注册.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
import requests
import optparse
import json

def register():
    url = "https://api.shisanshui.rtxux.xyz/auth/register"
    payload = "="
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


class apply(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(814, 417)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 771, 381))
        self.label.setStyleSheet("image: url(:/f/photo/注册.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(390, 130, 131, 31))
        self.lineEdit.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 170, 131, 31))
        self.lineEdit_2.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 220, 131, 31))
        self.lineEdit_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 30, 61, 31))
        self.pushButton_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 280, 131, 51))
        self.pushButton.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.display)
        self.pushButton_3.clicked.connect(self.pushButton_3.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
    def display(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        url = "https://api.shisanshui.rtxux.xyz/auth/register"
        text = {"username": username, "password": password}
        payload = json.dumps(text)
        headers = {'content-type': 'application/json'}
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)


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
