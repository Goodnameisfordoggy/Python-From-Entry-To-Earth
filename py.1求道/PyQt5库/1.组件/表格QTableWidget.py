'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:45:45
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\表格QTableWidget.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton


class TableWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建表格小部件
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(3)  # 设置行数
        self.table_widget.setColumnCount(3)  # 设置列数

        # 设置表头标签
        self.table_widget.setHorizontalHeaderLabels(['列 1', '列 2', '列 3'])

        # 设置表格内容
        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem(f'单元格({i + 1}, {j + 1})')
                self.table_widget.setItem(i, j, item)

        # 创建按钮，用于添加新行
        add_button = QPushButton('添加新行', self)
        add_button.clicked.connect(self.addRowToTable)

        # 将表格小部件和按钮添加到垂直布局中
        vbox.addWidget(self.table_widget)
        vbox.addWidget(add_button)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QTableWidget 示例')
        self.setGeometry(300, 300, 400, 200)

    def addRowToTable(self):
        # 添加新行到表格
        current_row = self.table_widget.rowCount()
        self.table_widget.setRowCount(current_row + 1)

        for j in range(self.table_widget.columnCount()):
            item = QTableWidgetItem(f'新单元格({current_row + 1}, {j + 1})')
            self.table_widget.setItem(current_row, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWidgetExample()
    window.show()
    sys.exit(app.exec_())
