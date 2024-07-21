'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2024-03-10 16:47:12
FilePath: \python\py.1求道境\6.PyQt5库\1.组件\工具栏QToolBar.py
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

class ToolbarExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Toolbar Example')

        # 创建工具栏
        toolbar = self.addToolBar('工具栏')

        # 创建工具动作
        action_open = QAction(QIcon('open.png'), '打开', self)
        action_open.triggered.connect(self.openFile)

        action_save = QAction(QIcon('save.png'), '保存', self)
        action_save.triggered.connect(self.saveFile)

        action_exit = QAction(QIcon('exit.png'), '退出', self)
        action_exit.triggered.connect(self.close)

        # 向工具栏添加动作
        toolbar.addAction(action_open)
        toolbar.addAction(action_save)
        toolbar.addSeparator()  # 添加分隔符
        toolbar.addAction(action_exit)

        # 设置主窗口布局
        self.setGeometry(100, 100, 600, 400)

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # 使用Qt的文件对话框，而不是本地对话框
        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)

        file_path, _ = file_dialog.getOpenFileName(self, '打开文件', '', 'All Files (*);;Text Files (*.txt)')

        if file_path:
            QMessageBox.information(self, '文件打开', f'已成功打开文件:\n{file_path}')

    def saveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # 使用Qt的文件对话框，而不是本地对话框
        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)

        file_path, _ = file_dialog.getSaveFileName(self, '保存文件', '', 'All Files (*);;Text Files (*.txt)')

        if file_path:
            QMessageBox.information(self, '文件保存', f'已成功保存文件:\n{file_path}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ToolbarExample()
    example.show()
    sys.exit(app.exec_())
