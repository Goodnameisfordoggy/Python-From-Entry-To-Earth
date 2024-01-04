"""
动态绑定属性和方法
    一个Student类可以创建很多个Student类的实例对象,且每个实例对象的属性可以不同
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃饭")


stu1 = Student("Goodnameisfordoggy", 18)
stu2 = Student("李四", 19)
print(id(stu1))
print(id(stu2))

#动态绑定的属性只能为当前绑定对象所用
print("=======为stu1动态绑定属性")
stu1.gender = "男"#绑定操作
print(stu1.name, stu1.age, stu1.gender)    # Goodnameisfordoggy 18 男
#print(stu2.gender)    # AttributeError: 'Student' object has no attribute 'gender'

#动态绑定的方法只能为当前绑定对象所用
print("=======为stu1动态绑定方法")


def show():#show目前仅为为类外函数
    print("此方法动态绑定对象为stu1")


stu1.show = show#绑定操作
stu1.show()    # 此方法动态绑定对象为stu1