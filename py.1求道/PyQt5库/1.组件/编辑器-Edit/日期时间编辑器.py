'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:43:33
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\编辑器-Edit\日期时间编辑器.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit, QLabel
from PyQt5.QtCore import QDateTime


class DateTimeEditExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDateTimeEdit Example')

        # 创建 QDateTimeEdit
        datetime_edit = QDateTimeEdit(self)
        datetime_edit.setDateTime(QDateTime.currentDateTime())  # 设置初始日期时间

        # 创建标签用于显示选择的日期时间
        label = QLabel(self)
        label.setText("选择的日期时间：")

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(datetime_edit)
        layout.addWidget(label)

        # 连接信号槽，以在日期时间更改时更新标签内容
        datetime_edit.dateTimeChanged.connect(lambda dateTime: label.setText(
            f"选择的日期时间： {dateTime.toString('yyyy-MM-dd hh:mm:ss')}"))

        # 设置主窗口布局
        self.setLayout(layout)
        self.setGeometry(100, 100, 400, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = DateTimeEditExample()
    example.show()
    sys.exit(app.exec_())
