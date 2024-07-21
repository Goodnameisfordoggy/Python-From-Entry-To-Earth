'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:47
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\列表视图QListView.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class ListViewExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建模型
        model = QStandardItemModel()

        # 添加数据到模型
        items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', "Item 5"]
        for text in items:
            item = QStandardItem(text)
            model.appendRow(item)

        # 创建列表视图并设置模型
        list_view = QListView()
        list_view.setModel(model)

        # 创建布局并将列表视图添加到布局中
        vbox = QVBoxLayout()
        vbox.addWidget(list_view)

        # 设置布局给主窗口
        self.setLayout(vbox)

        self.setWindowTitle('QListView Example')
        self.setGeometry(100, 100, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ListViewExample()
    example.show()
    sys.exit(app.exec_())
