'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:43:51
FilePath: \python\py.1�����\6.PyQt5��\1.���\�Ի���-Dialog\�ı��Ի���QInputDialog.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QInputDialog


class TextDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Text Dialog Example')

        # ������ť
        btn = QPushButton('��ʾ�ı��Ի���', self)
        btn.clicked.connect(self.showTextDialog)

        # ��������
        layout = QVBoxLayout()
        layout.addWidget(btn)

        # ���������ڲ���
        self.setLayout(layout)

    def showTextDialog(self):
        # ��ʾ�ı��Ի���
        text, okPressed = QInputDialog.getText(self, '�����ı�', '�������ı�:')

        # �����û�������
        if okPressed:
            print('������ı���:', text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TextDialogExample()
    example.show()
    sys.exit(app.exec_())
