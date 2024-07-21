'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:17
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\滚动区域QScrollArea.py
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
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton, QLineEdit, QHBoxLayout

class ScrollableComponent(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 创建 QScrollArea
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)  # 设置内容大小可调整

        # 在 QScrollArea 中添加一个 QVBoxLayout 作为滚动内容
        scroll_content = QWidget(self)
        content_layout = QVBoxLayout(scroll_content)

        # 添加各种组件到滚动内容中
        label = QLabel('这是一个标签', self)
        button = QPushButton('这是一个按钮', self)
        line_edit = QLineEdit(self)

        content_layout.addWidget(label)
        content_layout.addWidget(button)
        content_layout.addWidget(line_edit)

        # 设置滚动内容为 QScrollArea 的滚动内容
        scroll_area.setWidget(scroll_content)

        layout.addWidget(scroll_area)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    scrollable_component = ScrollableComponent()
    scrollable_component.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
