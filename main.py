from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
import sys
import requests
import optparse
import 主界面
import 登录
import 对战记录
import 排行榜
import 模式选择
import 注册
import 游戏界面
from 主界面 import mainmeun
from 登录 import login
from 对战记录 import fight
from 排行榜 import paihang
from 模式选择 import moshi
from 注册 import apply
from 游戏界面 import gamepage


class Mywindow1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow1, self).__init__()
        self.ui = mainmeun()  # 这句话是实例化类
        self.ui.setupUi(self)  # 这句话相当于设置控件

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow2, self).__init__()
        self.ui = login()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()

class Mywindow3(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow3, self).__init__()
        self.ui = apply()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow4(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow4, self).__init__()
        self.ui = moshi()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow5(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow5, self).__init__()
        self.ui = fight()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow6(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow6, self).__init__()
        self.ui = paihang()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow7(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow7, self).__init__()
        self.ui = gamepage()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # 实例化各个类
    w1 = Mywindow1()
    w2 = Mywindow2()
    w3 = Mywindow3()
    w4 = Mywindow4()
    w5 = Mywindow5()
    w6 = Mywindow6()
    w7 = Mywindow7()
    # 将主窗口进行展示调用
    w1.show()
    w1.ui.pushButton.clicked.connect(w2.open)
    w1.ui.pushButton_2.clicked.connect(w4.open)
    w2.ui.pushButton.clicked.connect(w4.open)
    w2.ui.pushButton_2.clicked.connect(w3.open)
    w2.ui.pushButton_3.clicked.connect(w2.close)
    w3.ui.pushButton.clicked.connect(w2.open)
    w3.ui.pushButton_3.clicked.connect(w3.close)
    w4.ui.pushButton.clicked.connect(w7.open)
    w4.ui.pushButton_2.clicked.connect(w7.open)
    w4.ui.pushButton_4.clicked.connect(w6.open)
    w4.ui.pushButton_5.clicked.connect(w5.open)
    w4.ui.pushButton_3.clicked.connect(w4.close)
    w5.ui.pushButton_3.clicked.connect(w5.close)
    w6.ui.pushButton_3.clicked.connect(w6.close)

    sys.exit(app.exec_())


