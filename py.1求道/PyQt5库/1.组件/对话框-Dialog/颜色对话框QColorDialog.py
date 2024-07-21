'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:44:35
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\对话框-Dialog\颜色对话框QColorDialog.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QColorDialog
from PyQt5.QtGui import QColor

class ColorDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建按钮
        self.button = QPushButton('打开颜色对话框', self)
        self.button.clicked.connect(self.showColorDialog)

        # 创建布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.button)

        # 设置布局给主窗口
        self.setLayout(vbox)

        self.setWindowTitle('QColorDialog Example')
        self.setGeometry(100, 100, 300, 200)

    def showColorDialog(self):
        # 打开颜色对话框，返回选中的颜色
        color = QColorDialog.getColor()

        # 如果用户点击了确定按钮，更新按钮的背景颜色
        if color.isValid():
            self.button.setStyleSheet('background-color: {}'.format(color.name()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ColorDialogExample()
    example.show()
    sys.exit(app.exec_())
