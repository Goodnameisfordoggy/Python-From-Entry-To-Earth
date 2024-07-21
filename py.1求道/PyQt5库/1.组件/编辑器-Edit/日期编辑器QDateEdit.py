'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:43:27
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\编辑器-Edit\日期编辑器QDateEdit.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDateEdit
from PyQt5.QtCore import QDate


class DateEditExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建日期编辑小部件
        self.date_edit = QDateEdit(self)

        # 设置日期范围
        self.date_edit.setDateRange(QDate(2000, 1, 1), QDate(2030, 12, 31))

        # 设置日期步长
        self.date_edit.setDate(QDate.currentDate())  # 设置初始日期为当前日期

        # 绑定槽函数，处理日期变化事件
        self.date_edit.dateChanged.connect(self.showSelectedDate)

        # 创建标签，用于显示选中的日期
        self.selected_date_label = QLabel('选中的日期：', self)

        # 将日期编辑小部件和标签添加到垂直布局中
        vbox.addWidget(self.date_edit)
        vbox.addWidget(self.selected_date_label)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QDateEdit 示例')
        self.setGeometry(300, 300, 300, 200)

    def showSelectedDate(self):
        # 显示选中的日期
        selected_date = self.date_edit.date()
        self.selected_date_label.setText(
            f'选中的日期：{selected_date.toString("yyyy-MM-dd")}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DateEditExample()
    window.show()
    sys.exit(app.exec_())
