'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:42:58
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\编辑器-Edit\单行输入编辑器QLineEdit.py
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
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit

class YourMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel('Song Name:')
        layout.addWidget(label)

        self.song_name_entry = QLineEdit()
        self.song_name_entry.setPlaceholderText('Enter song name')  # 设置占位符文本
        layout.addWidget(self.song_name_entry)

if __name__ == '__main__':
    app = QApplication([])
    window = YourMainWindow()
    window.show()
    app.exec_()
