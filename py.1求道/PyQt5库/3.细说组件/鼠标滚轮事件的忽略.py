'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:29
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\鼠标滚轮事件的忽略.py
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
from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtCore import QEvent

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        combo_box = QComboBox(self)
        combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        combo_box.installEventFilter(self)  # 安装事件过滤器

        layout.addWidget(combo_box)

    def eventFilter(self, obj, event):
        if isinstance(obj, QComboBox) and event.type() == QEvent.Wheel:
            # 捕获滚轮事件并忽略
            return True

        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication([])

    widget = MyWidget()
    widget.show()

    app.exec_()
