'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:26
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\进度条QProgressBar.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt5.QtCore import QTimer


class ProgressBarExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建水平进度条
        self.progress_horizontal = QProgressBar(self)
        self.progress_horizontal.setOrientation(0)  # 设置为水平方向
        self.progress_horizontal.setValue(0)  # 初始值为0

        # 创建垂直进度条
        self.progress_vertical = QProgressBar(self)
        self.progress_vertical.setOrientation(1)  # 设置为垂直方向
        self.progress_vertical.setValue(0)  # 初始值为0

        # 创建按钮，用于开始、停止和归零进度条演示
        start_button = QPushButton('开始', self)
        stop_button = QPushButton('停止', self)
        reset_button = QPushButton('归零', self)

        # 绑定槽函数，处理按钮点击事件
        start_button.clicked.connect(self.startProgress)
        stop_button.clicked.connect(self.stopProgress)
        reset_button.clicked.connect(self.resetProgress)

        # 将进度条和按钮添加到垂直布局中
        vbox.addWidget(self.progress_horizontal)
        vbox.addWidget(self.progress_vertical)
        vbox.addWidget(start_button)
        vbox.addWidget(stop_button)
        vbox.addWidget(reset_button)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QProgressBar 示例')
        self.setGeometry(300, 300, 300, 200)

        # 创建定时器，用于定时更新进度条
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)

        # 设置定时器间隔（毫秒）
        self.timer_interval = 100

    def startProgress(self):
        # 开始进度条演示
        self.timer.start(self.timer_interval)

    def stopProgress(self):
        # 停止进度条演示
        self.timer.stop()

    def resetProgress(self):
        # 归零进度条演示
        self.progress_horizontal.setValue(0)
        self.progress_vertical.setValue(0)

    def updateProgress(self):
        # 定时更新进度条
        value_horizontal = self.progress_horizontal.value()
        value_vertical = self.progress_vertical.value()

        # 增加进度值，但仅当值小于100时
        if value_horizontal < 100:
            value_horizontal += 1

        if value_vertical < 100:
            value_vertical += 1

        # 更新进度条的值
        self.progress_horizontal.setValue(value_horizontal)
        self.progress_vertical.setValue(value_vertical)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressBarExample()
    window.show()
    sys.exit(app.exec_())
