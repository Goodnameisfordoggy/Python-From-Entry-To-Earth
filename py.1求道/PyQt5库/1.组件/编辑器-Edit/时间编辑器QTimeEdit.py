'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:43:37
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\编辑器-Edit\时间编辑器QTimeEdit.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTimeEdit
from PyQt5.QtCore import QTime


class TimeEditExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建时间编辑小部件
        self.time_edit = QTimeEdit(self)

        # 设置时间范围和步长
        self.time_edit.setTimeRange(QTime(0, 0), QTime(23, 59))

        # 绑定槽函数，处理时间变化事件
        self.time_edit.timeChanged.connect(self.showSelectedTime)

        # 创建标签，用于显示选中的时间
        self.selected_time_label = QLabel('选中的时间：', self)

        # 将时间编辑小部件和标签添加到垂直布局中
        vbox.addWidget(self.time_edit)
        vbox.addWidget(self.selected_time_label)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QTimeEdit 示例')
        self.setGeometry(300, 300, 300, 200)

    def showSelectedTime(self):
        # 显示选中的时间
        selected_time = self.time_edit.time()
        self.selected_time_label.setText(
            f'选中的时间：{selected_time.toString("hh:mm:ss")}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimeEditExample()
    window.show()
    sys.exit(app.exec_())
