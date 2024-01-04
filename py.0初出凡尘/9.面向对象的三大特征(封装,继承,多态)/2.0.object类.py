"""
object类
    *object类是所有类的父类,因此所有类都有object类的属性和方法.
    *内置函数dir()可以查看指定对象所有属性(示例,方法)
    *Object有一个__str()__方法,用于返回一个对于"对象的描述",对应内置函数str()经常用于print()方法,
     帮我们查看对象的信息,所以我们经常会对__str()__进行重写
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("Goodnameisfordoggy", 18)

print(dir(Student))    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
print(dir(stu))        # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name']
                       # 显然,对象stu会比类Student多两个实例属性 name, age
print("=============================================================================")
print(stu)#在没有重写__str()__方法之前,直接输出对象会默认用object类中自带的__str()__方法输出 对象stu 的内存地址  # <__main__.Student object at 0x01259530>


#重写__str()__方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "名字:{}, 年龄:{}".format(self.name, self.age)


per = Person("Goodnameisfordoggy", 18)
print(per)    # 名字:Goodnameisfordoggy, 年龄:18  QwQ:现在__str()__方法不能再输出对象的内存地址了