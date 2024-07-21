'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:12
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\控件跟随鼠标移动.py
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
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QPoint

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        # 记录鼠标按下时的位置
        self.drag_start_position = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'drag_start_position'):
            # 计算鼠标移动的距离
            delta = event.globalPos() - self.drag_start_position

            # 更新窗口位置
            new_position = self.pos() + delta
            self.move(new_position)

            # 更新起始位置，以便下一次移动计算
            self.drag_start_position = event.globalPos()

    def mouseReleaseEvent(self, event):
        # 鼠标释放时清空起始位置
        if hasattr(self, 'drag_start_position'):
            delattr(self, 'drag_start_position')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
