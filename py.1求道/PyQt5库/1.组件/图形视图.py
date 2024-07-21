'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:48:21
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\图形视图.py
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
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtGui import QPainter  # Import the QPainter module
from PyQt5.QtCore import Qt


class GraphicsViewExample(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建图形场景
        scene = QGraphicsScene(self)
        self.setScene(scene)

        # 在场景中添加椭圆项
        ellipse_item = QGraphicsEllipseItem(0, 0, 100, 50)
        ellipse_item.setBrush(Qt.red)
        scene.addItem(ellipse_item)

        # 设置视图属性
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setSceneRect(0, 0, 300, 200)  # 设置场景大小

        self.setWindowTitle('QGraphicsView 示例')
        self.setGeometry(300, 300, 400, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphicsViewExample()
    window.show()
    sys.exit(app.exec_())
