"""
封装:
    提高程序的安全性.
    *将数据(属性)和行为(方法)包装到类对象中.在方法内部对属性进行操作,在类对象的外部调用方法.
    这样,无需关心方法内部的具体实现细节,从而隔离了复杂度.
    *在Python中没有专门的修饰符用于属性的私有,如果该属性不希望在类对象外部被访问,前面使用两个'_'.
"""


#一般的class示例
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start_car(self):
        print("汽车已启动...")


car = Car("宝马X5")
car.start_car()    # 汽车已启动...
print(car.brand)    # 宝马X5
print("===================================================================")


#实例属性不希望(但可以用特殊方法)在类对象外部被访问,前面使用两个'_'.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print("姓名:{}, 年龄:{}".format(self.name, self.__age))


stu1 = Student("Goodnameisfordoggy", 18)
 #调用方法来使用实例
stu1.show()    # 姓名:Goodnameisfordoggy, 年龄:18
 #在类外直接使用实例
print(stu1.name)
#print(stu1.__age)    # AttributeError: 'Student' object has no attribute '__age'
 #用特殊方法 在类外 访问前面带有带有"__"的实例
print("===============用dir()来查找想要访问的对象====================")
print(dir(stu1))    # ['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'show']
print("===========================================================")
print(stu1._Student__age)#waring:访问类的 protected 成员 _Student__age  # 18  QwQ:会有警告但程序可以正常运行!