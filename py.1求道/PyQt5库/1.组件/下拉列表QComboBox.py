'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:48:30
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\下拉列表QComboBox.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox


class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建标签和下拉框
        label = QLabel('选择一个选项:', self)
        combo_box = QComboBox(self)

        # 添加选项到下拉框
        combo_box.addItem('选项 1')
        combo_box.addItem('选项 2')
        combo_box.addItem('选项 3')
        combo_box.addItem('选项 4')
        combo_box.addItem('选项 5')
        combo_box.addItem('选项 6')

        # 绑定槽函数，处理下拉框选择变化事件
        combo_box.currentIndexChanged.connect(self.comboBoxIndexChanged)

        # 将标签和下拉框添加到垂直布局中
        vbox.addWidget(label)
        vbox.addWidget(combo_box)

        # 将布局设置为窗口的主布局
        self.setLayout(vbox)

        self.setWindowTitle('QComboBox 示例')
        self.setGeometry(300, 300, 300, 200)

    def comboBoxIndexChanged(self, index):
        # 处理下拉框选择变化事件
        combo_box = self.sender()  # 获取发射信号的对象
        selected_item = combo_box.currentText()
        print(f'选择了：{selected_item}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ComboBoxExample()
    window.show()
    sys.exit(app.exec_())
