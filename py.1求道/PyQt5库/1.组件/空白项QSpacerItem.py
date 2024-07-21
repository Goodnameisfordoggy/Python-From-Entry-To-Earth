'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:37
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\空白项QSpacerItem.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建垂直布局
        vbox = QVBoxLayout(self)

        # 创建组件
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        button = QPushButton('按钮')

        # 创建一个可伸缩的空白项
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # 将组件和空白项添加到布局
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addSpacerItem(spacer_item)
        vbox.addWidget(button)

        # 设置布局的上下边距
        vbox.setContentsMargins(10, 10, 10, 10)

        self.setLayout(vbox)

        # 设置窗口属性
        self.setWindowTitle('窗口布局示例')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
