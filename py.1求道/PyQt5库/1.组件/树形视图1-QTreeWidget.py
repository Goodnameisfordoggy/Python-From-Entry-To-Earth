'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:56
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\树形视图1-QTreeWidget.py
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(['Search Results', '123'])
        self.tree_widget.itemClicked.connect(self.on_item_clicked)

        self.setCentralWidget(self.tree_widget)

        self.add_tree_item("Item 1")
        self.add_tree_item("Item 2")
        self.add_tree_item("Item 3")

    def add_tree_item(self, text):
        item = QTreeWidgetItem(self.tree_widget)
        item.setText(0, text)

    def on_item_clicked(self, item, column):
        print(f"Item clicked: {item.text(column)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
