'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:46:48
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\带有选项卡的窗口QTabWidget.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel

app = QApplication([])

# 创建主窗口
main_window = QWidget()
main_layout = QVBoxLayout()

# 创建 QTabWidget
tab_widget = QTabWidget()

# 创建第一个页面的内容
page1_content = QLabel("This is the content of Page 1.")
# 添加第一个页面到 QTabWidget
tab_widget.addTab(page1_content, "Page 1")

# 创建第二个页面的内容
page2_content = QLabel("This is the content of Page 2.")
# 添加第二个页面到 QTabWidget
tab_widget.addTab(page2_content, "Page 2")

# 将 QTabWidget 添加到主窗口的布局中
main_layout.addWidget(tab_widget)

# 设置主窗口的布局
main_window.setLayout(main_layout)

# 显示主窗口
main_window.show()

app.exec_()
