# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '排行榜.ui'
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
class paihang(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(828, 458)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 771, 381))
        self.label.setStyleSheet("image: url(:/f/photo/排行榜.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 40, 61, 31))
        self.pushButton_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 350, 91, 31))
        self.pushButton_5.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 350, 91, 31))
        self.pushButton_4.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(110, 120, 611, 221))
        self.listWidget.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(self.pushButton_3.show)
        self.pushButton_5.clicked.connect(self.pushButton_5.show)
        self.pushButton_4.clicked.connect(self.pushButton_4.show)
        QtCore.QMetaObject.connectSlotsByName(Form)
        url = "https://api.shisanshui.rtxux.xyz/rank"
        response = requests.request("GET", url)
        res = response.text
        flag = json.loads(res)
        global player_id
        global name
        global score
        for i in flag:
            s1 = i['player_id']
            s2 = i['name']
            s3 = i['score']
            s = "用户名:%s 玩家id:%s 分数:%s" % (s1, s2, s3)
            self.listWidget.addItem(s)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.listWidget.setFont(font)

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
