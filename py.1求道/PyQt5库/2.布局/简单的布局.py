'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:49:19
FilePath: \python\py.1求道境\6.PyQt5库\2.布局\简单的布局.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Nested Layout Example')

        # 创建按钮
        self.button1 = QPushButton('Button 1')
        self.button2 = QPushButton('Button 2')
        self.button3 = QPushButton('Button 3')

        # 创建水平布局
        self.h_layout = QHBoxLayout()

        # 创建垂直布局
        self.v_layout1 = QVBoxLayout()
        self.v_layout2 = QVBoxLayout()

        # 将按钮添加到垂直布局1中
        self.v_layout1.addWidget(self.button1)
        self.v_layout1.addWidget(self.button2)

        # 将按钮添加到垂直布局2中
        self.v_layout2.addWidget(self.button3)

        # 将垂直布局添加到水平布局中
        self.h_layout.addLayout(self.v_layout1)
        self.h_layout.addLayout(self.v_layout2)
        self.setLayout(self.h_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

