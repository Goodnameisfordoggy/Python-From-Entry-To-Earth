'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:42
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\列表框QListWidget.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton


class ListWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建列表视图
        self.list_widget = QListWidget(self)

        # 添加一些项目到列表视图
        items = ['项目 1', '项目 2', '项目 3']
        self.list_widget.addItems(items)

        # 创建按钮，用于添加新项目
        add_button = QPushButton('添加项目', self)
        add_button.clicked.connect(self.addItemToList)

        # 将列表视图和按钮添加到垂直布局中
        vbox.addWidget(self.list_widget)
        vbox.addWidget(add_button)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QListWidget 示例')
        self.setGeometry(300, 300, 300, 200)

    def addItemToList(self):
        # 添加新项目到列表视图
        new_item_text = f'新项目 {self.list_widget.count() + 1}'
        self.list_widget.addItem(new_item_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ListWidgetExample()
    window.show()
    sys.exit(app.exec_())
