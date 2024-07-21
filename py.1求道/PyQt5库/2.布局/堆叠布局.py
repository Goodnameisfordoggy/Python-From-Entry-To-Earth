'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:49:14
FilePath: \python\py.1求道境\6.PyQt5库\2.布局\堆叠布局.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedLayout

class StackedLayoutExample(QWidget):
    def __init__(self):
        super().__init__()

        # 创建堆叠布局
        stacked_layout = QStackedLayout()

        # 页面1
        page1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel('Welcome to Page 1')
        button1 = QPushButton('Next Page')
        button1.clicked.connect(lambda: stacked_layout.setCurrentIndex(1))
        layout1.addWidget(label1)
        layout1.addWidget(button1)
        page1.setLayout(layout1)

        # 页面2
        page2 = QWidget()
        layout2 = QVBoxLayout()
        label2 = QLabel('You are now on Page 2')
        button2 = QPushButton('Next Page')
        button2.clicked.connect(lambda: stacked_layout.setCurrentIndex(2))
        layout2.addWidget(label2)
        layout2.addWidget(button2)
        page2.setLayout(layout2)

        # 页面3
        page3 = QWidget()
        layout3 = QVBoxLayout()
        label3 = QLabel('This is the final Page')
        button3 = QPushButton('Restart')
        button3.clicked.connect(lambda: stacked_layout.setCurrentIndex(0))
        layout3.addWidget(label3)
        layout3.addWidget(button3)
        page3.setLayout(layout3)

        # 向堆叠布局添加页面
        stacked_layout.addWidget(page1)
        stacked_layout.addWidget(page2)
        stacked_layout.addWidget(page3)

        # 创建垂直布局，用于放置按钮和堆叠布局
        main_layout = QVBoxLayout()
        main_layout.addLayout(stacked_layout)

        self.setLayout(main_layout)

        self.setWindowTitle('Stacked Layout Example')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = StackedLayoutExample()
    example.show()
    sys.exit(app.exec_())
