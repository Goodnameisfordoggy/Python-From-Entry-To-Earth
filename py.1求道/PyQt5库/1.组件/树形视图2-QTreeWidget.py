'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:48:05
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\树形视图2-QTreeWidget.py
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
        self.resize(1000, 800)
        # 创建一个 QTreeWidget 并设置列标签
        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(['名称', '数值'])
        self.tree_widget.setFixedSize(600, 500)

        # 将主窗口的中央部件设置为 QTreeWidget
        self.setCentralWidget(self.tree_widget)

        # 添加根节点
        self.add_tree_item("根节点", "根节点数值")

        # 添加父节点及其子节点
        parent_item1 = self.add_tree_item("父节点1", "父节点1数值")
        self.add_tree_item_to_parent(parent_item1, "子节点1", "子节点1数值")
        self.add_tree_item_to_parent(parent_item1, "子节点2", "子节点2数值")

        parent_item2 = self.add_tree_item("父节点2", "父节点2数值")
        self.add_tree_item_to_parent(parent_item2, "子节点3", "子节点3数值")
        self.add_tree_item_to_parent(parent_item2, "子节点4", "子节点4数值")

    def add_tree_item(self, name, value):
        # 向 QTreeWidget 添加一个节点并设置各列的文本内容
        item = QTreeWidgetItem(self.tree_widget)
        item.setText(0, name)  # 设置第一列的文本
        item.setText(1, value)  # 设置第二列的文本
        return item

    def add_tree_item_to_parent(self, parent, name, value):
        # 向父节点添加一个子节点并设置各列的文本内容
        item = QTreeWidgetItem(parent)
        item.setText(0, name)  # 设置第一列的文本
        item.setText(1, value)  # 设置第二列的文本

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
