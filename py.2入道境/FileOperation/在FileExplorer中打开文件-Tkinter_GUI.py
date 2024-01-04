import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    file_path = filedialog.askopenfilename()  # 打开文件对话框，用户选择文件
    if file_path:
        os.system(f'start "" "{file_path}"')  # 使用系统默认程序打开文件，并将文件路径放在引号中

root = tk.Tk()
root.title("选择要打开的文件")

button = tk.Button(root, text="选择文件", command=open_file)
button.pack()

root.mainloop()