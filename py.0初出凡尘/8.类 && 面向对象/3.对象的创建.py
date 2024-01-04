"""
对象的创建
语法:
    实例名=类名()
有了实例,就可以调用类中的内容
"""


class Student:
    native_pace = "河北"

    def eat(self):
        print("正在吃饭")

    @staticmethod
    def sm():
        print("使用staticmethod修饰,所以这是静态方法")

    @classmethod
    def cm(cls):
        print("使用classmethod修饰,所以这是类方法")

    def __init__(self, name, age):
        self.name = name
        self.age = age


#创建Student类的对象
stu = Student("HDJ", 18)# stu是根据Student创建出来的实例对象
stu.eat()    # 正在吃饭  # 类的对象可以调用类中的方法(对象名.方法名())与属性
print(stu.name, stu.age)    # HDJ 18

#print(id(stu))    # 22410064
#print(type(stu))    # <class '__main__.Student'>
#print(stu)    # <__main__.Student object at 0x0155F350>
#print("=========================================================")
#print(id(Student))    # 17716664
#print(type(Student))    # <class 'type'>
#print(Student)    # <class '__main__.Student'>

#另一种调用类中方法的写法(类名.方法名(类的对象)
Student.eat(stu)    # 正在吃饭