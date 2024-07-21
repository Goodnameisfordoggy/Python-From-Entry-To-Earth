'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:49:05
FilePath: \python\py.1求道境\6.PyQt5库\2.布局\表单布局.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton


class FormLayoutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        main_layout = QVBoxLayout(self)

        # 创建 QFormLayout
        form_layout = QFormLayout()

        # 添加标签和输入字段
        form_layout.addRow('Label 1:', QLineEdit())
        form_layout.addRow('Label 2:', QLineEdit())
        form_layout.addRow('Label 3:', QLineEdit())

        # 添加一个按钮
        submit_button = QPushButton('Submit')
        form_layout.addWidget(submit_button)

        # 将 QFormLayout 添加到主布局
        main_layout.addLayout(form_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = FormLayoutExample()
    window.show()
    app.exec_()
