'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:51
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\日历QCalendarWidget.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel


class CalendarWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建日历小部件
        self.calendar_widget = QCalendarWidget(self)

        # 绑定槽函数，处理日期选择变化事件
        self.calendar_widget.selectionChanged.connect(self.showSelectedDate)

        # 创建标签，用于显示选中的日期
        self.selected_date_label = QLabel('选中的日期：', self)

        # 将日历小部件和标签添加到垂直布局中
        vbox.addWidget(self.calendar_widget)
        vbox.addWidget(self.selected_date_label)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget 示例')
        self.setGeometry(300, 300, 400, 300)

    def showSelectedDate(self):
        # 显示选中的日期
        selected_date = self.calendar_widget.selectedDate()
        self.selected_date_label.setText(
            f'选中的日期：{selected_date.toString("yyyy-MM-dd")}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarWidgetExample()
    window.show()
    sys.exit(app.exec_())
