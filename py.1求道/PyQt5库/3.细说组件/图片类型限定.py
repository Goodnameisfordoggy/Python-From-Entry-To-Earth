'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:50:43
FilePath: \python\py.1求道境\6.PyQt5库\3.细说组件\图片类型限定.py
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
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
import sys

class FileDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # 创建 QLabel 用于显示选择的图片
        self.image_label = QLabel("选择的图片将在这里显示")
        layout.addWidget(self.image_label)

        # 创建按钮，连接槽函数以调用文件对话框
        button = QPushButton("选择图片")
        button.clicked.connect(self.showImageDialog)
        layout.addWidget(button)

        self.setLayout(layout)

    def showImageDialog(self):
        # 创建文件对话框
        file_dialog = QFileDialog()

        # 设置文件对话框的模式为选择文件
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        # 明确指定允许的 MIME 类型为图片
        mime_types = ["image/png", "image/jpeg", "image/bmp", "image/gif"]
        file_dialog.setMimeTypeFilters(mime_types)

        # 显示文件对话框
        file_path, _ = file_dialog.getOpenFileName(None, "选择图片文件")

        # 更新 QLabel 显示选择的图片
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = FileDialogExample()
    example.show()
    sys.exit(app.exec_())
