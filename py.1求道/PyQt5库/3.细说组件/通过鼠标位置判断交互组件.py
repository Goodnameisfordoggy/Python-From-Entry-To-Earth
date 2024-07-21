'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:38
FilePath: \python\py.1�����\6.PyQt5��\3.ϸ˵���\ͨ�����λ���жϽ������.py
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
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('��ǩ��ʽ�л�ʾ��')

        # ʹ�ô�ֱ����
        layout = QVBoxLayout()

        # ������ǩ
        self.labels = []
        for i in range(1, 6):
            label = QLabel(f"��ǩ {i}")
            label.setAlignment(Qt.AlignCenter)
            label.setCursor(Qt.PointingHandCursor)
            layout.addWidget(label)
            self.labels.append(label)

            # Ϊ��ǩ�󶨵���¼�������
            label.mousePressEvent = lambda event, label=label: self.on_label_click(label)

        self.setLayout(layout)

        # ��ʼ���������б�ǩ��ʽ��ԭΪ��ʼ״̬
        self.reset_all_labels()

    def on_label_click(self, clicked_label):
        # ����һ�α�ѡ�еı�ǩ��ʽ��ԭ
        self.reset_all_labels()

        # ���õ�ǰ����ı�ǩ��ʽΪѡ��״̬
        clicked_label.setStyleSheet("font-weight: bold; color: blue;")

    def reset_all_labels(self):
        # �����б�ǩ��ʽ��ԭΪ��ʼ״̬
        for label in self.labels:
            label.setStyleSheet("font-weight: normal; color: black;")

    def mousePressEvent(self, event):
        # ��ȡ����¼���λ��
        pos = event.pos()

        # �ҵ���λ�õ��Ӳ���
        child_widget = self.childAt(pos)

        # �����������ķǱ�ǩ����ʱ��Ҳ����ǩ��ʽ��ԭ
        if child_widget not in self.labels:
            self.reset_all_labels()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
