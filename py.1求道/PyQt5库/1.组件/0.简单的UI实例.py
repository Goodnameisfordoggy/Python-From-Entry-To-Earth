'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:45:30
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\0.简单的UI实例.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QProgressBar

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle('My PyQt Window')
        self.setGeometry(100, 100, 400, 300)

        # 创建按钮
        self.button1 = QPushButton('按钮1', self)
        self.button2 = QPushButton('按钮2', self)

        # 创建文本框
        self.textbox = QLineEdit(self)

        # 创建进度条
        self.progressbar = QProgressBar(self)

        # 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.textbox)
        layout.addWidget(self.progressbar)

        # 信号连接到槽
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)

    def on_button1_clicked(self):
        self.textbox.setText("按钮1被点击了")

    def on_button2_clicked(self):
        # 模拟进度条更新
        value = self.progressbar.value() + 10
        self.progressbar.setValue(value)

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)

    # 创建窗口对象
    window = MyWindow()

    # 显示窗口
    window.show()

    # 应用程序事件循环
    sys.exit(app.exec_())