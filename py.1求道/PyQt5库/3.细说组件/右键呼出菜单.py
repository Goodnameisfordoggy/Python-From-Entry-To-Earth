'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:51:29
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\右键呼出菜单.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QVBoxLayout
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 在组件上添加布局
        layout = QVBoxLayout(self)
        
        # 设置右键菜单
        self.setContextMenuPolicy(3)  # 3 表示 CustomContextMenu，即自定义右键菜单
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, event):
        # 创建右键菜单
        contextMenu = QMenu(self)

        # 添加菜单项
        action1 = contextMenu.addAction('菜单项1')
        action2 = contextMenu.addAction('菜单项2')

        # 显示菜单
        action = contextMenu.exec_(self.mapToGlobal(event))

        # 根据用户选择的菜单项执行相应操作
        if action == action1:
            print('菜单项1 被点击')
        elif action == action2:
            print('菜单项2 被点击')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
