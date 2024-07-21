import tkinter
import tkinter.messagebox


def main():

    flag_label_text = True

    #修改标签上的文字
    def change_label_text():
        """使用了bool,该操作只能在两种设定好的文本格式之间切换"""
        nonlocal flag_label_text
        flag_label_text = not flag_label_text
        text, color = ('Hello world!', 'red') if flag_label_text else ('Goodbey world!', 'blue')
        label.config(text=text, fg=color)

    #确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top_window.quit()

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
    # 创建一个按钮容器
                               #QwQ:窗口
    button_container = tkinter.Frame(top_window)
                    #QwQ:位于窗口的位置
    button_container.pack(side='bottom')
    # 创建按钮对象 选择添加到哪个窗口中 再通过command参数绑定事件回调函数
    button1 = tkinter.Button(button_container, text='切换', command=change_label_text)
    button1.pack(side='left')

    button2 = tkinter.Button(button_container, text='退出', command=confirm_to_quit)
    button2.pack(side='right')

    #QwQ:创建完对象后一定要"布局",否则对象不会在窗口上显示

    # 开启主事件循环(运行窗口)
    tkinter.mainloop()


if __name__ == '__main__':
    main()

