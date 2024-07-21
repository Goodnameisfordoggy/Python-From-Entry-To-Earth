'''
QWQ:不要使用文本编辑器打开二进制文件
'''
import tkinter as tk
from tkinter import filedialog
import os
import platform
import subprocess

def open_config_file():
    file_path = filedialog.askopenfilename()  # 打开文件对话框，用户选择文件
    if os.path.exists(file_path):
        if platform.system() == 'Windows':  # 检查操作系统是否为 Windows
            os.system(f'notepad.exe {file_path}')  # 使用系统默认的文本编辑器打开文件
        if platform.system() == 'Darwin':  # 检查操作系统是否为 macOS
            subprocess.run(['open', '-t', file_path])
    else:
        print("错误", "文件未找到。")

root = tk.Tk()
root.title("打开配置文件")

button = tk.Button(root, text="打开配置文件", command=open_config_file)
button.pack()

root.mainloop()



