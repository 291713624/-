# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '游戏界面.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import 登录
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
import requests
import http.client
import optparse
import json
import os
global token
class gamepage(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(826, 483)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 270, 61, 41))
        self.pushButton_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 270, 61, 31))
        self.pushButton_4.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 771, 381))
        self.label.setStyleSheet("image: url(:/f/photo/游戏界面.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(740, 360, 61, 31))
        self.pushButton_5.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(740, 370, 61, 31))
        self.pushButton_6.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(710, 70, 61, 31))
        self.pushButton_7.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 340, 61, 31))
        self.pushButton_8.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 340, 61, 31))
        self.pushButton_9.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 290, 371, 51))
        self.lineEdit.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        self.pushButton_8.clicked.connect(self.display)
        self.pushButton_9.clicked.connect(self.pushButton_9.show)
        self.pushButton_7.clicked.connect(self.pushButton_7.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def display(self):
        global id
        global card
        token=登录.token
        print(token)
        url = "https://api.shisanshui.rtxux.xyz/game/open"
        headers = {'x-auth-token': token }
        response = requests.request("POST", url, headers=headers)
        res = response.text
        a = res.find('card')
        b = res.find('id')
        id = res[b+4:b+9]
        card = res[a + 7:len(res) - 3]
        print(card)
        print(id)
        self.lineEdit.setText(card)
        print(response.text)
    #def play(self):
        #os.chdir("C:\Users\许煌标\Desktop")
        #path_01 = r"shisanshui.exe %s" % (card)
        #r_v = os.system(path_01)
        #print(r_v)

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

