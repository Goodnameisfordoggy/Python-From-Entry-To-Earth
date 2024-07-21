'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:56
FilePath: \python\py.1�����\6.PyQt5��\1.���\������ͼ1-QTreeWidget.py
Description: 

				*		д��¥��д�ּ䣬д�ּ������Ա��
				*		������Աд�������ó��򻻾�Ǯ��
				*		����ֻ���������������������ߣ�
				*		��������ո��գ����������긴�ꡣ
				*		��Ը�������Լ䣬��Ը�Ϲ��ϰ�ǰ��
				*		���۱������Ȥ���������г���Ա��
				*		����Ц��߯��񲣬��Ц�Լ���̫����
				*		��������Ư���ã��ĸ���ó���Ա��    
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
