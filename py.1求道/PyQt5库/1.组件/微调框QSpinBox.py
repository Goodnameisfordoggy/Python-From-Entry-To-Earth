'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:48:25
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\微调框QSpinBox.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox


class SpinBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建标签和微调框
        label = QLabel('选择一个整数:', self)
        spin_box = QSpinBox(self)

        # 设置微调框的范围
        spin_box.setRange(1, 100)

        # 绑定槽函数，处理微调框值变化事件
        spin_box.valueChanged.connect(self.spinBoxValueChanged)

        # 将标签和微调框添加到垂直布局中
        vbox.addWidget(label)
        vbox.addWidget(spin_box)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QSpinBox 示例')
        self.setGeometry(300, 300, 300, 200)

    def spinBoxValueChanged(self, value):
        # 处理微调框值变化事件
        spin_box = self.sender()  # 获取发射信号的对象
        print(f'选择了：{value}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpinBoxExample()
    window.show()
    sys.exit(app.exec_())
