# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '主界面.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)


class mainmeun(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(806, 415)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 771, 381))
        self.label.setStyleSheet("image: url(:/f/photo/主菜单.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 310, 121, 51))
        self.pushButton.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 310, 121, 51))
        self.pushButton_2.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.pushButton.show)
        self.pushButton_2.clicked.connect(self.pushButton_2.show)
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
