'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:44:10
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\对话框-Dialog\文件对话框QFileDialog.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog


class FileDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 File Dialog Example')

        # 创建按钮
        btn = QPushButton('打开文件对话框', self)
        btn.clicked.connect(self.showFileDialog)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(btn)

        # 设置主窗口布局
        self.setLayout(layout)

    def showFileDialog(self):
        # 打开文件对话框
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # 使用Qt的文件对话框，而不是本地对话框
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        # 获取用户选择的文件路径
        file_path, _ = file_dialog.getOpenFileName(
            self, '打开文件', '', 'All Files (*);;Text Files (*.txt)')

        # 处理用户的选择
        if file_path:
            print('选择的文件路径是:', file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = FileDialogExample()
    example.show()
    sys.exit(app.exec_())
