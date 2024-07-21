'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:48:39
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\自定义布局.py
Description: 

				*		写字楼里写字间，写字间里程序员；
				*		程序人员写程序，又拿程序换酒钱。
				*		酒醒只在网上坐，酒醉还来网下眠；
				*		酒醉酒醒日复日，网上网下年复年。
				*		但愿老死电脑间，不愿鞠躬老板前；
				*		奔驰宝马贵者趣，公交自行程序员。
				*		别人笑我忒疯癫，我笑自己命太贱；
				*		不见满街漂亮妹，哪个归得程序员？    
Copyright (c) 2024 by HDJ, All Rights Reserved. 
'''
import time
import glob
import os
import random
import re
import threading
import json
import sys
# 需要cmd安装
import pyglet
import pynput.keyboard
import keyboard
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QMenu,
    QVBoxLayout, QHBoxLayout, QSizePolicy, QDesktopWidget, QWidget
    )
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("自定义布局示例")

        # 添加控件到窗口，并手动设置位置
        label1 = QLabel("控件1", self)
        label1.setGeometry(100, 100, 100, 30)

        label2 = QLabel("控件2", self)
        label2.setGeometry(200, 200, 100, 30)

        label3 = QLabel("控件3", self)
        label3.setGeometry(300, 300, 100, 30)

        label4 = QLabel("控件4", self)
        label4.setGeometry(400, 400, 100, 30)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
