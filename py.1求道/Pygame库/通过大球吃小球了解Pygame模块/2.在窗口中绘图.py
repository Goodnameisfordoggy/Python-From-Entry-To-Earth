"""
可以通过pygame中draw模块的函数在窗口上绘图，可以绘制的图形包括：线条、矩形、多边形、圆、椭圆、圆弧等。
屏幕坐标系是将屏幕 左上角 设置为坐标原点(0, 0)，向右是x轴的正向，向下是y轴的正向，在表示位置或者设置尺寸的时候，我们默认的单位都是像素。
pygame中表示颜色用的是色光三原色表示法，即通过一个元组或列表来指定颜色的RGB值，每个值都在0~255之间，
因为是每种原色都用一个8位（bit）的值来表示，三种颜色相当于一共由24位构成，这也就是常说的“24位颜色表示法”。
"""
import pygame


def main():
    # 初始化 pygame库(必要的,初始化 Pygame 库时，会返回一个表示初始化操作成功或失败的元组,若成功该元组的第一个元素的值为 0,失败是一堆乱码)
    pygame.init()
    # 创建用于显示的窗口并设置窗口大小
    top_window = pygame.display.set_mode((800, 600)) #QwQ:窗口大小是一个由两个数组成的元组
    # 设置该窗口的标题
    pygame.display.set_caption('大球吃小球')
    #设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    top_window.fill((100, 100, 100))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(top_window, (255, 0, 0), (400, 400), 100, 0)
    #刷新窗口(在此处,将屏幕背景的颜色以及画的圆显示出来)
    pygame.display.flip()

    running = True
    # 游戏主循环
    while running:
        for event in pygame.event.get():
            #处理 QUIT事件 QwQ:此处判断的是 获取的事件的类型 是否为 QUIT 事件
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
