'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:49:10
FilePath: \python\py.1求道境\6.PyQt5库\2.布局\布局的拉伸与占比.py
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QStackedLayout, QListWidgetItem


class YourMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        # 创建并设置主窗口中央的部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 创建并设置中央组件的布局
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        left_layout = QVBoxLayout()
        right_layout = QStackedLayout()
        main_layout.addLayout(left_layout, 1)  # 设置左侧布局占比为1
        main_layout.addLayout(right_layout, 3)  # 设置右侧布局占比为3

        # 左侧列表框
        self.list_Widget = QListWidget(self)
        left_layout.addWidget(self.list_Widget)

        # 按钮选项
        self.button1 = QPushButton("选项1", self)
        item1 = QListWidgetItem()
        self.list_Widget.addItem(item1)
        self.list_Widget.setItemWidget(item1, self.button1)

        self.button2 = QPushButton("选项2", self)
        item2 = QListWidgetItem()
        self.list_Widget.addItem(item2)
        self.list_Widget.setItemWidget(item2, self.button2)

        self.button3 = QPushButton("选项3", self)
        item3 = QListWidgetItem()
        self.list_Widget.addItem(item3)
        self.list_Widget.setItemWidget(item3, self.button3)

        # 其他布局和窗口初始化的代码...


if __name__ == '__main__':
    app = QApplication([])
    window = YourMainWindow()
    window.show()
    app.exec_()
