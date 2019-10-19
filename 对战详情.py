# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '对战详情.ui'
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
class detail(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(826, 418)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 771, 381))
        self.label.setStyleSheet("image: url(:/f/photo/对战详情.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(540, 70, 91, 41))
        self.lineEdit.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(640, 70, 71, 41))
        self.pushButton.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 30, 61, 31))
        self.pushButton_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(80, 110, 621, 221))
        self.listWidget.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.listWidget.setObjectName("listWidget")
        self.pushButton.clicked.connect(self.display)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def display(self):
        global token
        token = 登录.token
        number = self.lineEdit.text()
        url = "https://api.shisanshui.rtxux.xyz/history/%s" % (number)
        headers = {'x-auth-token': token}
        response = requests.request("GET", url, headers=headers)
        res = response.text
        text = json.loads(res)
        t = text['data']
        t=str(t)
        s = "战局id:%s" % (number)
        self.listWidget.addItem(s)
        a=t.find('detail')
        t=t[a+9:len(t)-2]
        s = "详细数据:\n%s" % (t)
        self.listWidget.addItem(s)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
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
