'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:46:52
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\单选按钮QRadioButton.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton


class RadioButtonExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建三个单选按钮
        radio_btn1 = QRadioButton('选项 1', self)
        radio_btn2 = QRadioButton('选项 2', self)
        radio_btn3 = QRadioButton('选项 3', self)

        # 将单选按钮添加到垂直布局中
        vbox.addWidget(radio_btn1)
        vbox.addWidget(radio_btn2)
        vbox.addWidget(radio_btn3)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        # 绑定槽函数，处理单选按钮状态变化事件
        radio_btn1.toggled.connect(self.radioButtonToggled)
        radio_btn2.toggled.connect(self.radioButtonToggled)
        radio_btn3.toggled.connect(self.radioButtonToggled)

        self.setWindowTitle('QRadioButton 示例')
        self.setGeometry(300, 300, 300, 200)

    def radioButtonToggled(self):
        # 处理单选按钮状态变化事件
        sender = self.sender()  # 获取发射信号的对象
        if sender.isChecked():
            print(f'选中了 {sender.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RadioButtonExample()
    window.show()
    sys.exit(app.exec_())
