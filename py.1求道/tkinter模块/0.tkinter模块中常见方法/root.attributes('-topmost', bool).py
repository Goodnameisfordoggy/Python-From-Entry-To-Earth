from tkinter import Tk, Button, Toplevel, messagebox


def open_window():
    top = Toplevel(root)
    top.title("Second UI")

    # 将top置顶
    top.attributes('-topmost', True)

    # 处理错误
    try:
        # 弹出错误窗口
        messagebox.showerror("Error", "Something went wrong!")
    finally:
        # 将二级UI窗口的置顶属性设置为False（还原默认设置）
        top.attributes('-topmost', False)


root = Tk()
root.title("Root Window")

open_button = Button(root, text="Open Window", command=open_window)
open_button.pack()

root.mainloop()