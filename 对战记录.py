# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '对战记录.ui'
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
global token
class fight(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(829, 454)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 771, 381))
        self.label.setStyleSheet("image: url(:/f/photo/对战记录.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 50, 61, 31))
        self.pushButton_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 360, 71, 41))
        self.pushButton_4.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(100, 130, 621, 221))
        self.listWidget.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 90, 71, 41))
        self.pushButton.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(550, 90, 91, 41))
        self.lineEdit.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(self.pushButton_3.show)
        self.pushButton_4.clicked.connect(self.display)
        self.pushButton.clicked.connect(self.pushButton.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def display(self):
        global token
        token = 登录.token
        user_id=登录.user_id
        url = "https://api.shisanshui.rtxux.xyz/history"
        querystring = {"page": "0", "limit": "100", "player_id": user_id}
        headers = {'x-auth-token': token}
        response = requests.request("GET", url, headers=headers, params=querystring)
        res = response.text
        flag = json.loads(res)
        global id
        global card
        global score
        global data
        for i in flag['data']:
            s1 = i['id']
            s2 = i['card']
            s3 = i['score']
            s = "战局id:%s\n手牌:%s\n分数:%s" % (s1, s2, s3)
            self.listWidget.addItem(s)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.listWidget.setFont(font)
        print(response.text)
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
