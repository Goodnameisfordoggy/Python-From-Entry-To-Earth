'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:51:03
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\文本框的右键菜单.py
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
from PyQt5.QtWidgets import QApplication, QLabel, QMenu, QAction, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, pyqtSignal

class CustomLabel(QLabel):
    leftClicked = pyqtSignal()

    def contextMenuEvent(self, event):
        self.leftClicked.emit()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = CustomLabel("Right-click me!", self)
        self.label.setAlignment(Qt.AlignCenter)

        # 添加操作
        action1 = QAction("Action 1", self)
        action1.triggered.connect(self.action1_triggered)

        action2 = QAction("Action 2", self)
        action2.triggered.connect(self.action2_triggered)

        # 创建菜单并将操作添加到菜单中
        context_menu = QMenu(self)
        context_menu.addAction(action1)
        context_menu.addAction(action2)

        # 连接自定义标签的 leftClicked 信号到槽函数
        self.label.leftClicked.connect(
            lambda: context_menu.exec_(self.label.mapToGlobal(self.label.rect().center()))
        )

        # 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

    def action1_triggered(self):
        print("Action 1 triggered!")

    def action2_triggered(self):
        print("Action 2 triggered!")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
