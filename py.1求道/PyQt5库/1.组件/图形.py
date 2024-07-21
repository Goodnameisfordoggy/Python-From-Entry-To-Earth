'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:48:08
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\图形.py
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
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsRectItem
from PyQt5.QtCore import Qt

class GraphicsSceneExample(QGraphicsScene):
    def __init__(self):
        super().__init__()

        # 添加椭圆和矩形图形项到场景
        ellipse_item = QGraphicsEllipseItem(0, 0, 100, 100)
        rect_item = QGraphicsRectItem(150, 0, 100, 100)

        # 设置图形项的笔刷和画笔
        ellipse_item.setBrush(Qt.green)
        ellipse_item.setPen(Qt.black)

        rect_item.setBrush(Qt.blue)
        rect_item.setPen(Qt.black)

        # 将图形项添加到场景
        self.addItem(ellipse_item)
        self.addItem(rect_item)

def main():
    app = QApplication(sys.argv)

    # 创建场景和视图
    scene = GraphicsSceneExample()
    view = QGraphicsView(scene)

    # 设置视图的属性
    view.setSceneRect(0, 0, 300, 100)
    view.setWindowTitle('QGraphicsScene Example')
    view.setGeometry(100, 100, 400, 200)

    # 显示视图
    view.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
