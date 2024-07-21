
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
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)