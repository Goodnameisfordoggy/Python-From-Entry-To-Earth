"""
人类肉眼可以感知到相对较低的帧率(刷新率)，但同时也与我们所观察的内容有关。
根据一些研究，大多数人类视觉系统需要每秒至少25帧的刷新率才能感到连续的动画效果。这就是电影所使用的帧率，被称为标准帧率。
然而，这只是建立在表现最佳 case 下的最小帧率。

实际上，帧率越高越好，因为最高帧率将带来最佳的覆盖率，让肉眼看不到画面由许多静态图片组成的情况。
例如，对于视频游戏动画和虚拟现实应用程序，通常需要更高的帧率(大约60到120帧)才能确保流畅的运动和操作。
此外，对于高速运动的场景，例如赛车比赛或快速运动的体育场景，可能需要更高的帧率才能有效地捕捉到每个细节。

在实践中，选择恰当的帧率还需要考虑设备限制，例如显示器的刷新率，以及其他应用程序可能与本应用程序争夺CPU资源等方面。
因此，需要根据具体情况选择适当的帧率和实现方式。
"""
import pygame


def main():

    pygame.init()
    top_window = pygame.display.set_mode((1250, 700))
    pygame.display.set_caption('动画效果')

    #定义小球的初始位置
    x, y = 50, 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #重新绘制背景
        top_window.fill((255, 255, 255))
        #重新绘制小球
        pygame.draw.circle(top_window, (255, 0, 0), (x, y), 31.4, 0)
        pygame.display.flip()
        #等待一段时间(毫秒)
        pygame.time.delay(8) #120Hz高刷 为8.333333~毫秒
        #计算小球下一帧的位置
        x += 2.2
        y += 2.2


if __name__ == "__main__":
    main()