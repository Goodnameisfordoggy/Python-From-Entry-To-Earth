"""
类的组成:
    类属性
    实例方案
    静态方案
    类方法
    初始化方法
"""


class Student:
    native_pace = "河北"# 直接写在类里的变量称为 类属性

    #在类里定义的函数称为 实例方法
    def eat(self):# 在类方法中定义函数()内要写self
        print("正在吃饭")

    #静态方法
    @staticmethod
    def sm():# 在静态方法中()什么都不写
        print("使用staticmethod修饰,所以这是静态方法")

    #类方法
    @classmethod
    def cm(cls):# 在类方法中定义函数()内要写cls
        print("使用classmethod修饰,所以这是类方法")

    #初始化方法
    def __init__(self, name, age):
        self.name = name# self.name 称为实例属性  # 将局部变量name的值赋给实例属性
        self.age = age