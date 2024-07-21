'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:51:08
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\稳定的二级UI 1.py
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
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QAction, QMenu

class SecondUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Second UI')
        self.setGeometry(200, 200, 400, 300)

        label = QLabel('This is the Second UI', self)
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

        # 创建菜单栏
        menubar = self.menuBar()

        # 创建一级菜单
        file_menu = menubar.addMenu('File')

        # 在一级菜单中添加打开二级UI的菜单项
        open_second_ui_action = QAction('Open Second UI', self)
        open_second_ui_action.triggered.connect(self.open_second_ui)
        file_menu.addAction(open_second_ui_action)

        # 初始化二级UI实例
        self.second_ui = SecondUI()

    def open_second_ui(self):
        # 显示已经存在的二级UI实例
        self.second_ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
