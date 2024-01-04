"""
继承:
    提高代码的复用性.
    语法格式:
        class 子类名称(父类1, 父类2 ...):
            pass
    *如果一个类没有继承任何类,则默认继承object
    *Python 支持多继承
    *定义子类时,必须在其构造函数中调用父类的构造函数
"""


#一般 单继承 示例
class Person(object): #Person继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name_age(self):
        print("姓名:{}, 年龄:{}".format(self.name, self.age), end=' ')


#定义子类Student
class Student(Person):
    def __init__(self, name, age, stu_no):#在子类的定义过程中,初始化函数要将所有(含父类,子类中新定义)的变量声明
        super().__init__(name, age)#在初始化函数第二部,需要用super()来继承父类的实例
        self.stu_no = stu_no

    def show_stu_no(self):
        print("学号:{}".format(self.stu_no))


#定义子类Teacher
class Teacher(Person):
    def __init__(self, name, age, teach_of_year):
        super().__init__(name, age)
        self.teach_of_year = teach_of_year

    def show_teach_of_year(self):
        print("教龄:{}".format(self.teach_of_year))


stu1 = Student("张三", 18, 228211111)
teacher1 = Teacher("李四", 34, 10)
stu1.show_name_age()
stu1.show_stu_no()
                 # 姓名:张三, 年龄:18 学号:228211111
teacher1.show_name_age()
teacher1.show_teach_of_year()
                            # 姓名:李四, 年龄:34 教龄:10