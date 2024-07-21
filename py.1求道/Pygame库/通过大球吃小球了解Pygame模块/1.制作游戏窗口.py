import pygame


def main():
    # 初始化 pygame库(必要的,初始化 Pygame 库时，会返回一个表示初始化操作成功或失败的元组,若成功该元组的第一个元素的值为 0,失败是一堆乱码)
    pygame.init()
    # 创建用于显示的窗口并设置窗口大小
    top_window = pygame.display.set_mode((800, 600)) #QwQ:窗口大小是一个由两个数组成的元组
    # 设置该窗口的标题
    pygame.display.set_caption('大球吃小球')

    running = True
    # 游戏主循环
    while running:
        for event in pygame.event.get():
            #处理 QUIT事件 QwQ:此处判断的是 获取的事件的类型 是否为 QUIT 事件
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


if __name__ == '__main__':
    main()
