'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:03
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\按钮的凹陷凸起.py
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

""" pyqt5的按钮凹陷不好看,不推荐使用qwq """
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class RaisedSunkenButtonsExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Raised and Sunken Buttons')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        raised_button = QPushButton('凸起按钮')
        raised_button.clicked.connect(self.set_raised)
        layout.addWidget(raised_button)

        sunken_button = QPushButton('凹陷按钮')
        sunken_button.clicked.connect(self.set_sunken)
        layout.addWidget(sunken_button)

        self.setLayout(layout)

    def set_raised(self):
        # 设置按钮为凸起状态
        self.sender().setFlat(False)

    def set_sunken(self):
        # 设置按钮为凹陷状态
        self.sender().setFlat(True)

if __name__ == '__main__':
    app = QApplication([])

    window = RaisedSunkenButtonsExample()
    window.show()

    app.exec_()
