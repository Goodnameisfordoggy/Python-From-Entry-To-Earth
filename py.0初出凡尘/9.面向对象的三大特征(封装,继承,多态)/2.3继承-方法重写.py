"""
方法重写
    *如果子类对继承自父类的某个属性或方法不满意,可以在子类中对其(方法体)进行修改
    *子类重写后的方法可以通过super().xxx()调用父类中被重写的方法
"""


class Person(object): #Person继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("姓名:{}, 年龄:{}".format(self.name, self.age), end=' ')


class Teacher(Person):
    def __init__(self, name, age, teach_of_year):
        super().__init__(name, age)
        self.teach_of_year = teach_of_year

    def show(self):
        super().show()#用super().调用父类中的同名函数,使子类中的该函数覆盖父类中的同名函数,以达到重写的目的  QwQ:只有函数名相同才会被系统认定为重写
        print("教龄:{}".format(self.teach_of_year))


teacher1 = Teacher("李四", 34, 10)
teacher1.show()    # 姓名:李四, 年龄:34 教龄:10