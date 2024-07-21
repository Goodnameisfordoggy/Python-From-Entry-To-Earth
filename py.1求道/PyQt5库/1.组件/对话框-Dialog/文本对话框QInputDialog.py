'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:43:51
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\对话框-Dialog\文本对话框QInputDialog.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QInputDialog


class TextDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Text Dialog Example')

        # 创建按钮
        btn = QPushButton('显示文本对话框', self)
        btn.clicked.connect(self.showTextDialog)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(btn)

        # 设置主窗口布局
        self.setLayout(layout)

    def showTextDialog(self):
        # 显示文本对话框
        text, okPressed = QInputDialog.getText(self, '输入文本', '请输入文本:')

        # 处理用户的输入
        if okPressed:
            print('输入的文本是:', text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TextDialogExample()
    example.show()
    sys.exit(app.exec_())
