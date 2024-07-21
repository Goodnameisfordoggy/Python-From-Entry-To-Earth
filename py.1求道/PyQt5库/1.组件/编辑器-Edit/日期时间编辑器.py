'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:43:33
FilePath: \python\py.1�����\6.PyQt5��\1.���\�༭��-Edit\����ʱ��༭��.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit, QLabel
from PyQt5.QtCore import QDateTime


class DateTimeEditExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDateTimeEdit Example')

        # ���� QDateTimeEdit
        datetime_edit = QDateTimeEdit(self)
        datetime_edit.setDateTime(QDateTime.currentDateTime())  # ���ó�ʼ����ʱ��

        # ������ǩ������ʾѡ�������ʱ��
        label = QLabel(self)
        label.setText("ѡ�������ʱ�䣺")

        # ��������
        layout = QVBoxLayout()
        layout.addWidget(datetime_edit)
        layout.addWidget(label)

        # �����źŲۣ���������ʱ�����ʱ���±�ǩ����
        datetime_edit.dateTimeChanged.connect(lambda dateTime: label.setText(
            f"ѡ�������ʱ�䣺 {dateTime.toString('yyyy-MM-dd hh:mm:ss')}"))

        # ���������ڲ���
        self.setLayout(layout)
        self.setGeometry(100, 100, 400, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = DateTimeEditExample()
    example.show()
    sys.exit(app.exec_())
