'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:21
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\事件过滤器.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel

class ShortcutEditer(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QWidget { background-color: white; font-size: 30px; }")
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        self.label = QLabel('Press a shortcut key...')
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setWindowTitle('Shortcut Detection')
        self.setGeometry(300, 300, 300, 200)

    def eventFilter(self, obj, event):
        if event.type() == event.MouseButtonPress:
            print("Mouse button pressed in ShortcutEditer")
        return super().eventFilter(obj, event)

class ParentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        shortcut_editor = ShortcutEditer()
        self.installEventFilter(shortcut_editor)  # 安装事件过滤器

        layout.addWidget(shortcut_editor)
        self.setLayout(layout)
        self.setWindowTitle('Parent Widget')
        self.setGeometry(100, 100, 500, 300)

if __name__ == "__main__":
    app = QApplication([])
    parent_widget = ParentWidget()
    parent_widget.show()
    app.exec_()
