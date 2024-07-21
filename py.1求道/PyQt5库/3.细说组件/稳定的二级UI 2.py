'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:51:24
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\稳定的二级UI 2.py
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

"""
QMainWindow和QDialog是Qt框架中的两个不同的窗口类，它们在设计和用途上有一些区别。

应用场景:

QMainWindow通常用于创建应用程序的主窗口，包含菜单栏、工具栏、状态栏等，适用于整个应用程序的主界面。
QDialog通常用于创建对话框，比如弹出式窗口，用于在应用程序的主界面上执行特定的任务或获取用户输入。
界面元素:

QMainWindow提供了一个主窗口，可以包含各种子窗口、工具栏、菜单栏等。它通常充当应用程序的主要容器。
QDialog则是一个对话框窗口，通常包含用于特定任务的一组控件，比如文本框、按钮等。
关系:

QMainWindow可以包含多个QDialog或其他窗口部件，是整个应用程序的主要容器。
QDialog通常是作为QMainWindow的子窗口，用于执行一些特定的任务，然后返回结果给主窗口。
模态对话框:

QMainWindow不具备模态对话框的特性，通常用于应用程序的主界面。
QDialog可以是模态对话框，意味着它会阻止用户与其他窗口进行交互，直到对话框被关闭。
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QDialog

class SearchUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Search UI')
        self.setGeometry(200, 200, 400, 300)

        label = QLabel('This is the Search UI', self)
        button = QPushButton('Close', self)
        button.clicked.connect(self.close)

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(button)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)

        # 创建按钮，点击按钮弹出Search UI
        open_search_ui_button = QPushButton('Open Search UI', self)
        open_search_ui_button.clicked.connect(self.open_search_ui)

        layout = QVBoxLayout(self)
        layout.addWidget(open_search_ui_button)

        # 初始化Search UI实例
        self.search_ui = SearchUI(self)

    def open_search_ui(self):
        # 显示Search UI实例为模态对话框
        self.search_ui.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
