'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:33
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\树形图与文件系统.py
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
from PyQt5.QtWidgets import QApplication, QTreeView, QFileSystemModel
from PyQt5.QtCore import Qt
import sys

class TreeViewWithHeader(QTreeView):
    def __init__(self, parent=None):
        super(TreeViewWithHeader, self).__init__(parent)

        # 创建文件系统模型
        model = QFileSystemModel()
        model.setRootPath('')
        self.setModel(model)
        self.setRootIndex(model.index(''))  # 设置根目录

        # 设置表头文本内容
        header_labels = ['名称', '大小', '类型', '修改日期']
        for i, label in enumerate(header_labels):
            self.model().setHeaderData(i, Qt.Horizontal, label)

        # 设置表头样式
        self.setStyleSheet("""
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                border: 1px solid #2980b9;
            }
        """)
        self.setStyleSheet("""
            QTreeView {
                alternate-background-color: #f0f0f0;
                background-color: green;
                color: black;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    tree_view = TreeViewWithHeader()
    tree_view.show()

    sys.exit(app.exec_())
