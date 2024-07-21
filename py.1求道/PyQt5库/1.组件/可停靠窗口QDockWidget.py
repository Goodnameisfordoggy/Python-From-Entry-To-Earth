'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:31
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\可停靠窗口QDockWidget.py
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit


class DockWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个 QTextEdit 作为主窗口的中心小部件
        text_edit = QTextEdit(self)
        self.setCentralWidget(text_edit)

        # 创建一个 QDockWidget
        dock_widget = QDockWidget('Dock Widget', self)

        # 在 QDockWidget 内添加一个 QTextEdit
        dock_text_edit = QTextEdit()
        dock_widget.setWidget(dock_text_edit)

        # 设置 QDockWidget 可停靠在主窗口的左侧
        self.addDockWidget(1, dock_widget)

        self.setWindowTitle('QDockWidget 示例')
        self.setGeometry(300, 300, 500, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DockWidgetExample()
    window.show()
    sys.exit(app.exec_())
