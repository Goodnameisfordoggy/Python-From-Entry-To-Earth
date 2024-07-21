import tkinter


def main():
    # 创建顶层窗口
    top_window = tkinter.Tk()
    # 设置窗口大小
    top_window.geometry('240x160')  # QwQ注意几何说明符: 小写x
    # 设置窗口标题
    top_window.title('hello world小游戏')
    # 创建一个文本标签并添加到顶层窗口
                   # QwQ: 标签所在窗口  文本内容              字体与大小         文字颜色
    label = tkinter.Label(top_window, text='Hello world!', font='Arial -32', fg='red')
    label.pack(expand=1)  # QwQ:pack是Tkinter库中设置布局参数的命令，通过该命令可以将组件进行自动布局。
                          # expand 只能等于0或1
                          # 具体而言，label.pack(expand=1)命令指定该标签组件(label)在父容器中自动布局时可以扩展(expand)，也就是说可以根据父容器的大小进行自适应伸缩。
                          # 如果没有设置expand参数的值为1，标签组件将无法进行伸缩，最多只能占据固定大小的空间，不能适应各种尺寸的父容器。
    # 开启主事件循环(运行窗口)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
