'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:44:22
FilePath: \python\py.1�����\6.PyQt5��\1.���\�Ի���-Dialog\�ļ��жԻ���QFileDialog.getExistingDirectory.py
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
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout, QPushButton


class FolderDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Folder Dialog Example')

        # ������ť
        btn = QPushButton('���ļ��жԻ���', self)
        btn.clicked.connect(self.showFolderDialog)

        # ��������
        layout = QVBoxLayout()
        layout.addWidget(btn)

        # ���������ڲ���
        self.setLayout(layout)

    def showFolderDialog(self):
        # ���ļ��жԻ���
        folder_path = QFileDialog.getExistingDirectory(self, 'ѡ���ļ���')

        # �����û���ѡ��
        if folder_path:
            print('ѡ����ļ���·����:', folder_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = FolderDialogExample()
    example.show()
    sys.exit(app.exec_())
