'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:44:57
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\对话框-Dialog\字体对话框QFontDialog.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFontDialog
from PyQt5.QtGui import QFont

class FontDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建按钮和标签
        self.button = QPushButton('打开字体对话框', self)
        self.label = QLabel('选择的字体样式', self)

        # 创建布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.button)
        vbox.addWidget(self.label)

        # 设置布局给主窗口
        self.setLayout(vbox)

        # 连接按钮的点击事件到函数
        self.button.clicked.connect(self.showFontDialog)

        self.setWindowTitle('QFontDialog Example')
        self.setGeometry(100, 100, 300, 200)

    def showFontDialog(self):
        # 打开字体对话框，返回选中的字体
        font, ok = QFontDialog.getFont()

        # 如果用户点击了确定按钮，更新标签的字体样式
        if ok:
            self.label.setFont(font)
            self.label.setText('选择的字体样式: {}'.format(font.toString()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = FontDialogExample()
    example.show()
    sys.exit(app.exec_())
