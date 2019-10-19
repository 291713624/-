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
import optparse
import json
import os
import re
global card
global id
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
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 130, 361, 41))
        self.lineEdit_2.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 290, 371, 51))
        self.lineEdit_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 190, 361, 41))
        self.lineEdit_4.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 250, 361, 41))
        self.lineEdit_5.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Form)
        self.pushButton_8.clicked.connect(self.display)
        self.pushButton_9.clicked.connect(self.play)
        self.pushButton_7.clicked.connect(self.pushButton_7.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def display(self):
        global id
        global card
        global token
        token=登录.token
        print(token)
        url = "https://api.shisanshui.rtxux.xyz/game/open"
        headers = {'x-auth-token': token }
        response = requests.request("POST", url, headers=headers)
        res = response.text
        a = res.find('card')
        card = res[a + 7:len(res) - 3]
        b = res.find('id')
        res = res[b:a]
        res=re.search(r'[0-9]+',res)
        id=res.group()
        print(card)
        print(id)
        self.lineEdit.setText(card)
        print(response.text)
    def play(self):
        global card
        global id
        print(id)
        card = card.replace("&", "x")
        card = card.replace("#", "k")
        card = card.replace("$", "t")
        card = card.replace("*", "h")
        print(card)
        ss = "D:\shisanshui.exe %s" % (card)
        f = os.popen(ss, "r", 1)
        res = f.read()
        print(res)
        s = res.split("\n")
        self.lineEdit_2.setText(s[0])
        self.lineEdit_4.setText(s[1])
        self.lineEdit_5.setText(s[2])
        text = {
            "id": id,
            "card": [
                s[0],
                s[1],
                s[2]
            ]
        }
        payload = json.dumps(text)
        url = "https://api.shisanshui.rtxux.xyz/game/submit"
        headers = {
            'content-type': "application/json",
            'x-auth-token': token
        }
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
