'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:49:28
FilePath: \python\py.1求道境\6.PyQt5库\2.布局\栅格布局.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout

class GridLayoutExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建栅格布局
        grid_layout = QGridLayout()

        # 添加标签和文本框到栅格布局的不同位置
        grid_layout.addWidget(QLabel('Name:'), 0, 0)
        grid_layout.addWidget(QLineEdit(), 0, 1)

        grid_layout.addWidget(QLabel('Age:'), 1, 0)
        grid_layout.addWidget(QLineEdit(), 1, 1)

        grid_layout.addWidget(QLabel('Occupation:'), 2, 0)
        grid_layout.addWidget(QLineEdit(), 2, 1)

        # 将栅格布局设置为窗口的布局
        self.setLayout(grid_layout)

        # 设置窗口的大小和标题
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Grid Layout Example')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = GridLayoutExample()
    example.show()
    sys.exit(app.exec_())
