'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:49:38
FilePath: \python\py.1�����\6.PyQt5��\2.����\�����ڵĲ���.py
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
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ������ť
        button = QPushButton("Click me!")

        # ������ֱ���ֲ���Ӱ�ť
        layout = QVBoxLayout()
        layout.addWidget(button)

        # ��������������Ĳ���
        central_widget = QWidget(self)
        central_widget.setLayout(layout)

        # ���������ڵ����벿��
        self.setCentralWidget(central_widget)

        # ���������ڵı���ʹ�С
        self.setWindowTitle("Main Window with Button")
        self.setGeometry(100, 100, 400, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
