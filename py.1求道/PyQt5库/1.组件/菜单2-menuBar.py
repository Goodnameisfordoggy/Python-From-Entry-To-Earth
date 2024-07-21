'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:46:39
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\菜单2-menuBar.py
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主窗口标题
        self.setWindowTitle("PyQt5 Menu Example")

        # 创建菜单栏
        menubar = self.menuBar()

        # 创建文件菜单
        file_menu = menubar.addMenu("File")

        # 添加动作到文件菜单
        new_action = QAction("New", self)
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        file_menu.addAction(open_action)

        # 创建编辑菜单
        edit_menu = menubar.addMenu("Edit")

        # 添加动作到编辑菜单
        cut_action = QAction("Cut", self)
        edit_menu.addAction(cut_action)

        copy_action = QAction("Copy", self)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Paste", self)
        edit_menu.addAction(paste_action)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()