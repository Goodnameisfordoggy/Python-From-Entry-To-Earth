from tkinter import Tk, Button, Toplevel


def open_secondary_window():
    secondary_window = Toplevel(root)
    secondary_window.title("Secondary UI")

    def close_secondary_window():
        secondary_window.destroy()# 记得一定要写窗口关闭操作
        print("窗口已关闭")

    secondary_window.protocol("WM_DELETE_WINDOW", close_secondary_window) #窗口关闭绑定事件


root = Tk()
root.title("Main UI")

open_button = Button(root, text="Open Secondary Window", command=open_secondary_window)
open_button.pack()

root.mainloop()