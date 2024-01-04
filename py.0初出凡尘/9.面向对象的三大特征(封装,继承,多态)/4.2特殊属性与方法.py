class Person:
    def __new__(cls, *args, **kwargs):
        print("__new__被调用了,cls的id值为:{}".format(id(cls)))
        obj = super().__new__(cls)
        print("创建的对象的id为:{}".format(id(obj)))
        return obj

    def __init__(self, name, age):
        print("__init__被调用了,self的id值为:{}".format(id(self)))
        self.name = name
        self.age = age


print("object这个类对象的id为:{}".format(id(object)))
print("Person这个类对象的id为:{}".format(id(Person)))

p1 = Person("Goodnameisfordoggy", 18)
print("p1这个Person类的实例对象的id为:{}".format(id(p1)))
######################################
#object这个类对象的id为:1587920520
#Person这个类对象的id为:31479224
#__new__被调用了,cls的id值为:31479224
#创建的对象的id为:31519312
#__init__被调用了,self的id值为:31519312
#p1这个Person类的实例对象的id为:31519312