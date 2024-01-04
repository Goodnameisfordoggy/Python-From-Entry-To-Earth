"""
类属性的使用方式
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


#类属性的使用方式
print(Student.native_pace)    # 河北
stu1 = Student("张三", 18)
stu2 = Student("李四", 20)
print(stu1)    # <__main__.Student object at 0x0118F3B0>
print(stu1.native_pace)    # 河北
print("========================================================")
 #改变Student中类属性native_pace的值
  #(对照)不加Student.无法使用类属性
#print(native_pace)     # NameError: name 'native_pace' is not defined
native_pace = "天津"# 此时的native_pace仅为一个普通的字符串
print(native_pace)    # 天津
print(Student.native_pace)    # 河北
print("========================================================")
  #改变Student中的类属性
Student.native_pace = "北京"
print(native_pace)    # 天津
print(Student.native_pace)    # 北京
