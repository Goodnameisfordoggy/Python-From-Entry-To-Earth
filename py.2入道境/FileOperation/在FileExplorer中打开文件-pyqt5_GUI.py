import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

def open_file():
    file_path, _ = QFileDialog.getOpenFileName(None, "选择要打开的文件")  # 打开文件对话框，获取文件路径
    if file_path:
        os.startfile(file_path)  # 使用系统默认程序打开文件

class FileOpener(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("文件选择器")
        self.setGeometry(300, 300, 300, 200)

        button = QPushButton('选择文件并打开', self)
        button.clicked.connect(open_file)
        button.setGeometry(50, 50, 200, 100)

def main():
    app = QApplication(sys.argv)
    window = FileOpener()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
