'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:47
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\图片缩放与标签.py
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
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap

class ImageLabelDemo(QWidget):
    def __init__(self):
        super().__init__()

        # 创建 QLabel
        label = QLabel(self)

        # 创建 QPixmap 并加载图片
        original_pixmap = QPixmap("path/to/your/image.jpg")

        # 缩放图片按照原始比例
        scaled_pixmap = original_pixmap.scaledToWidth(200)  # 指定缩放后的宽度

        # 设置 QPixmap 到 QLabel
        label.setPixmap(scaled_pixmap)

        # 创建主布局
        layout = QVBoxLayout(self)

        # 将 QLabel 添加到布局
        layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication([])
    window = ImageLabelDemo()
    window.show()
    app.exec_()

