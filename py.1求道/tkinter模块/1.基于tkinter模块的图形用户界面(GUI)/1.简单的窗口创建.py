import tkinter


def main():
    # 创建顶层窗口
    top_window = tkinter.Tk()
    # 设置窗口大小
    top_window.geometry('240x160')  # QwQ注意几何说明符: 小写x
    # 设置窗口标题
    top_window.title('hello world小游戏')

    # 开启主事件循环(运行窗口)
    tkinter.mainloop()


if __name__ == '__main__':
    main()