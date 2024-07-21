'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:46:57
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\堆叠组件QStackedWidget.py
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QStackedWidget, QWidget
from PyQt5.QtGui import QColor


class SettingsPage(QWidget):
    def __init__(self, label_text, color):
        super().__init__()

        # 创建 QVBoxLayout 用于包含页面内容
        layout = QVBoxLayout(self)

        # 创建一个 QPushButton 用于显示页面标签
        button = QPushButton(label_text, self)

        # 设置按钮背景颜色
        button.setStyleSheet(f"background-color: {color.name()};")

        # 添加按钮到布局
        layout.addWidget(button)

        # 设置布局
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        # 创建不同的设置页面，并为每个页面设置不同的颜色
        self.page1 = SettingsPage('Setting Page 1', QColor(255, 0, 0))  # 红色
        self.page2 = SettingsPage('Setting Page 2', QColor(0, 255, 0))  # 绿色
        self.page3 = SettingsPage('Setting Page 3', QColor(0, 0, 255))  # 蓝色

        # 将页面添加到 QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        # 设置主窗口布局
        self.setCentralWidget(self.stacked_widget)

        # 创建按钮用于切换页面
        self.button_page1 = QPushButton('Page 1', self)
        self.button_page1.clicked.connect(lambda: self.change_page(0))

        self.button_page2 = QPushButton('Page 2', self)
        self.button_page2.clicked.connect(lambda: self.change_page(1))

        self.button_page3 = QPushButton('Page 3', self)
        self.button_page3.clicked.connect(lambda: self.change_page(2))

        # 创建一个水平布局用于放置切换按钮
        layout = QVBoxLayout()
        layout.addWidget(self.button_page1)
        layout.addWidget(self.button_page2)
        layout.addWidget(self.button_page3)

        # 设置主窗口布局
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setWindowTitle('Settings Window')
        self.setGeometry(300, 300, 400, 300)

    def change_page(self, index):
        if hasattr(self, 'stacked_widget') and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
