'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:22
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\滑动条QSlider.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider


class SliderExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建标签和水平滑动条
        label_horizontal = QLabel('水平滑动条:', self)
        slider_horizontal = QSlider(self)
        slider_horizontal.setOrientation(0)  # 设置为水平方向

        # 创建标签和垂直滑动条
        label_vertical = QLabel('垂直滑动条:', self)
        slider_vertical = QSlider(self)
        slider_vertical.setOrientation(1)  # 设置为垂直方向

        # 绑定槽函数，处理滑动条值变化事件
        slider_horizontal.valueChanged.connect(self.sliderValueChanged)
        slider_vertical.valueChanged.connect(self.sliderValueChanged)

        # 将标签和滑动条添加到垂直布局中
        vbox.addWidget(label_horizontal)
        vbox.addWidget(slider_horizontal)
        vbox.addWidget(label_vertical)
        vbox.addWidget(slider_vertical)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QSlider 示例')
        self.setGeometry(300, 300, 300, 200)

    def sliderValueChanged(self, value):
        # 处理滑动条值变化事件
        slider = self.sender()  # 获取发射信号的对象
        orientation = '水平' if slider.orientation() == 0 else '垂直'
        print(f'{orientation}滑动条值：{value}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SliderExample()
    window.show()
    sys.exit(app.exec_())
