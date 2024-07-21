'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:49:24
FilePath: \python\py.1求道境\6.PyQt5库\2.布局\网格布局.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 创建按钮
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button3 = QPushButton('Button 3')
        button4 = QPushButton('Button 4')

        # 创建网格布局
        grid_layout = QGridLayout()

        # 向网格布局添加按钮
        grid_layout.addWidget(button1, 0, 0)  # 第一行，第一列
        grid_layout.addWidget(button2, 0, 1)  # 第一行，第二列
        grid_layout.addWidget(button3, 1, 0)  # 第二行，第一列
        grid_layout.addWidget(button4, 1, 1)  # 第二行，第二列

        # 将网格布局设置为窗口的布局
        self.setLayout(grid_layout)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Grid Layout Example')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
