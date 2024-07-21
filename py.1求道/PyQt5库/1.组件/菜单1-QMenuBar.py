'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:46:29
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\菜单1-QMenuBar.py
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QMessageBox

class MenuBarExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('MenuBar Example')
        self.setGeometry(100, 100, 400, 300)

        # 创建菜单栏对象
        menu_bar = QMenuBar(self)

        # 创建一个菜单
        file_menu = menu_bar.addMenu('文件')

        # 创建一个动作（菜单项）
        open_action = QAction('打开', self)
        file_menu.addAction(open_action)

        # 为动作绑定方法
        open_action.triggered.connect(self.open_file)

        # 设置菜单栏
        self.setMenuBar(menu_bar)

    def open_file(self):
        QMessageBox.information(self, '消息', '执行打开文件的操作')

if __name__ == '__main__':
    app = QApplication([])

    window = MenuBarExample()
    window.show()

    app.exec_()
