'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:02
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\分割线QFrame.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame

class LineExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # 水平线
        line1 = QFrame(self)
        line1.setFrameShape(QFrame.HLine)
        layout.addWidget(line1)

        # 垂直线
        line2 = QFrame(self)
        line2.setFrameShape(QFrame.VLine)
        layout.addWidget(line2)

        # 盒子（带边框的矩形框）
        line3 = QFrame(self)
        line3.setFrameShape(QFrame.Box)
        layout.addWidget(line3)

        # 无框架
        line4 = QFrame(self)
        line4.setFrameShape(QFrame.NoFrame)
        layout.addWidget(line4)

        self.setWindowTitle('分割线样式示例')
        self.setGeometry(100, 100, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = LineExample()
    example.show()
    sys.exit(app.exec_())
