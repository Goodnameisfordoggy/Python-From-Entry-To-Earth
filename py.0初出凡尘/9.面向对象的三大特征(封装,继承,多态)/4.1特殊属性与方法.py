print(dir(object))    # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


#__dict__  获得类对象或实例对象所绑定的所有属性的字典
class A:
    pass


class B:
    pass


class C(B, A):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return self.name


class D(C):
    pass


class E(C):
    pass


c = C("HDJ", 18)
print(c.__dict__)#输出实例对象的属性字典    # {'name': 'HDJ', 'age': 18}
print(C.__dict__)#输出类对象的属性字典    # {'__module__': '__main__', '__init__': <function C.__init__ at 0x023738A0>, 'show': <function C.show at 0x02373858>, '__doc__': None}
print("=========================================================================")
print(c.__class__)#输出对象所属的类    # <class '__main__.C'>
print(C.__bases__)#输出C类的父类的元组    # (<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)#输出C类继承的第一个父类    # <class '__main__.B'>  QwQ:可见C类的定义 --> class C(B, A):
print(C.__mro__)#输出类的层次结构    # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)  QwQ:从左 --> 到右 继承顺序(若有同辈分,从左到右则表示优先级)
print(C.__subclasses__())#输出子类列表    # [<class '__main__.D'>, <class '__main__.E'>]