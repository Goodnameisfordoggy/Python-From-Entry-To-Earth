"""
可以在事件循环中对鼠标事件进行处理，通过事件对象的type属性可以判定事件类型，再通过pos属性就可以获得鼠标点击的位置。
如果要处理键盘事件也是在这个地方，做法与处理鼠标事件类似。
"""

from enum import Enum, unique
from math import sqrt
from random import randint
import pygame


@unique
class Color(Enum):
    """颜色-枚举类"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色(并创建小球对象)"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b) #返回颜色元组


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx #横向移动速度
        self.sy = sy #纵向移动速度
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        #触边检测,并回弹
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        #触顶(底)检测,并回弹
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            #两个圆之间的碰撞检测
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)#圆心距
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                #大球吞噬小球
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


def main():
    #放球的容器
    balls = []
    #Pygame初始三部曲
    pygame.init()
    top_window = pygame.display.set_mode((1250, 700))
    pygame.display.set_caption('大球吃小球')
    #游戏主事件循环
    running = True
    while running:
        for event in pygame.event.get():
            #处理结束事件
            if event.type == pygame.QUIT:
                running = False
            #处理鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #event.button 获取按下的具体按键 左键1, 右键3
                color = Color.random_color() #随机颜色
                x, y = event.pos #获取鼠标点击的位置坐标
                radius = randint(10, 100) #随机半径
                sx, sy = randint(-10, 10), randint(-10, 10) #随机速度
                sx = sx if sx != 0 else 1
                sy = sy if sy != 0 else 1
                ball = Ball(x, y, radius, sx, sy, color) #在鼠标点击处创建小球
                balls.append(ball) #将小球添加到存储容器
        #重新渲染屏幕
        top_window.fill((240, 240, 240))
        #检测容器内小球的存活状态
        for ball in balls:
            if ball.alive:
                ball.draw(top_window)
            else:
                balls.remove(ball)
        pygame.display.flip()
        pygame.time.delay(8) #屏幕刷新间隔
        #小球的移动
        for ball in balls:
            ball.move(top_window)
            #判断当前小球是否吞噬了其他球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()






