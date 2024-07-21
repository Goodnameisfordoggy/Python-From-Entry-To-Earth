from tkinter import Tk, Button, Toplevel, messagebox


def open_window():
    # 禁用一级UI窗口
    root.attributes('-disabled', True)

    top = Toplevel(root)
    top.title("Second UI")

    # 处理错误
    try:
        # 弹出错误窗口
        messagebox.showerror("Error", "Something went wrong!")
    finally:
        # 恢复一级UI窗口为可用状态
        root.attributes('-disabled', False)


root = Tk()
root.title("Root Window")

open_button = Button(root, text="Open Window", command=open_window)
open_button.pack()

root.mainloop()