'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:43:42
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\编辑器-Edit\文本编辑器QTextEdit.py
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
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout


class TextEditExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # 创建 QTextEdit
        text_edit = QTextEdit(self)
        text_edit.setPlainText("This is a QTextEdit")

        # 添加 QTextEdit 到布局
        vbox.addWidget(text_edit)

        # 设置布局
        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit 示例')
        self.setGeometry(300, 300, 300, 200)


if __name__ == '__main__':
    app = QApplication([])
    window = TextEditExample()
    window.show()
    app.exec_()
