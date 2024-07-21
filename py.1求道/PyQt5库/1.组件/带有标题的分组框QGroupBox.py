'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:46:43
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\带有标题的分组框QGroupBox.py
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QLabel, QCheckBox, QPushButton, QFontDialog

class EffectsGroupBox(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 添加 QGroupBox 作为带边框和标题的区域
        group_box = QGroupBox('这是一个带标题的边框', self)
        group_layout = QVBoxLayout(group_box)

        # 添加 QLabel 用于显示文本
        # 这个 QLabel 将位于 QGroupBox 的标题区域
        title_label = QLabel('这是一些文本', self)
        group_layout.addWidget(title_label)

        # 添加复选框和应用按钮
        boldCheckBox = QCheckBox('粗体', self)
        italicCheckBox = QCheckBox('斜体', self)
        underlineCheckBox = QCheckBox('下划线', self)
        strikeoutCheckBox = QCheckBox('删除线', self)

        applyButton = QPushButton('应用效果', self)
        applyButton.clicked.connect(self.applyEffects)

        group_layout.addWidget(boldCheckBox)
        group_layout.addWidget(italicCheckBox)
        group_layout.addWidget(underlineCheckBox)
        group_layout.addWidget(strikeoutCheckBox)
        group_layout.addWidget(applyButton)

        layout.addWidget(group_box)

        self.setLayout(layout)

    def applyEffects(self):
        font_dialog = QFontDialog(self)
        current_font = font_dialog.currentFont()

        # 应用粗体效果
        current_font.setBold(True)

        # 应用斜体效果
        current_font.setItalic(True)

        # 应用下划线效果
        current_font.setUnderline(True)

        # 应用删除线效果
        current_font.setStrikeOut(True)

        font_dialog.setCurrentFont(current_font)

        # 显示字体对话框
        font_dialog.exec_()

def main():
    app = QApplication(sys.argv)
    effects_group_box = EffectsGroupBox()
    effects_group_box.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
