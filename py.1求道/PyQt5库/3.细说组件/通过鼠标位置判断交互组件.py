'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:38
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\通过鼠标位置判断交互组件.py
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
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('标签样式切换示例')

        # 使用垂直布局
        layout = QVBoxLayout()

        # 创建标签
        self.labels = []
        for i in range(1, 6):
            label = QLabel(f"标签 {i}")
            label.setAlignment(Qt.AlignCenter)
            label.setCursor(Qt.PointingHandCursor)
            layout.addWidget(label)
            self.labels.append(label)

            # 为标签绑定点击事件处理函数
            label.mousePressEvent = lambda event, label=label: self.on_label_click(label)

        self.setLayout(layout)

        # 初始化，将所有标签样式复原为初始状态
        self.reset_all_labels()

    def on_label_click(self, clicked_label):
        # 将上一次被选中的标签样式复原
        self.reset_all_labels()

        # 设置当前点击的标签样式为选中状态
        clicked_label.setStyleSheet("font-weight: bold; color: blue;")

    def reset_all_labels(self):
        # 将所有标签样式复原为初始状态
        for label in self.labels:
            label.setStyleSheet("font-weight: normal; color: black;")

    def mousePressEvent(self, event):
        # 获取鼠标事件的位置
        pos = event.pos()

        # 找到该位置的子部件
        child_widget = self.childAt(pos)

        # 当点击父组件的非标签部分时，也将标签样式还原
        if child_widget not in self.labels:
            self.reset_all_labels()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
