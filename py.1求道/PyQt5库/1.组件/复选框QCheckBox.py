'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:07
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\复选框QCheckBox.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox


class CheckBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建两个复选框
        checkbox1 = QCheckBox('复选框 1', self)
        checkbox2 = QCheckBox('复选框 2', self)

        # 将复选框添加到垂直布局中
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        # 绑定槽函数，处理复选框状态变化事件
        checkbox1.stateChanged.connect(self.checkboxStateChanged)
        checkbox2.stateChanged.connect(self.checkboxStateChanged)

        self.setWindowTitle('QCheckBox 示例')
        self.setGeometry(300, 300, 300, 200)

    def checkboxStateChanged(self, state):
        # 处理复选框状态变化事件
        sender = self.sender()  # 获取发射信号的对象
        if state == 2:  # 2 表示复选框被选中
            print(f'复选框 {sender.text()} 被选中')
        else:
            print(f'复选框 {sender.text()} 被取消选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxExample()
    window.show()
    sys.exit(app.exec_())
