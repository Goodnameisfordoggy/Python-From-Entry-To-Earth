'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:16
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\列表框与按钮.py
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
from PyQt5.QtWidgets import QApplication, QListWidget, QPushButton, QVBoxLayout, QWidget


class ButtonListWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个 QListWidget
        self.listWidget = QListWidget(self)

        # 向列表中添加按钮
        for i in range(5):
            button = QPushButton(f"Button {i + 1}")
            self.listWidget.addItem("")
            self.listWidget.setItemWidget(self.listWidget.item(i), button)

        # 创建一个垂直布局，并将 QListWidget 添加到布局中
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.listWidget)

        # 设置主窗口的基本属性
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Button List Widget Example')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ButtonListWidget()
    window.show()
    sys.exit(app.exec_())
