'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:49:38
FilePath: \python\py.1求道境\6.PyQt5库\2.布局\主窗口的布局.py
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
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建按钮
        button = QPushButton("Click me!")

        # 创建垂直布局并添加按钮
        layout = QVBoxLayout()
        layout.addWidget(button)

        # 创建主窗口中央的部件
        central_widget = QWidget(self)
        central_widget.setLayout(layout)

        # 设置主窗口的中央部件
        self.setCentralWidget(central_widget)

        # 设置主窗口的标题和大小
        self.setWindowTitle("Main Window with Button")
        self.setGeometry(100, 100, 400, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
