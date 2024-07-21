'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:48:17
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\图形类.py
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
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsEllipseItem
from PyQt5.QtCore import Qt, QRectF

class CustomGraphicsItem(QGraphicsItem):
    def __init__(self):
        super().__init__()

        # 设置图形项的边界矩形
        self.rect = QRectF(0, 0, 100, 100)

    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget):
        # 在图形项内部绘制椭圆
        painter.setBrush(Qt.red)
        painter.drawEllipse(self.rect)

def main():
    app = QApplication(sys.argv)

    # 创建场景和视图
    scene = QGraphicsScene()
    view = QGraphicsView(scene)

    # 创建自定义图形项并添加到场景
    custom_item = CustomGraphicsItem()
    scene.addItem(custom_item)

    # 设置视图的属性
    view.setWindowTitle('QGraphicsItem Example')
    view.setGeometry(100, 100, 300, 200)

    # 显示视图
    view.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
