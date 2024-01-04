"""
类的创建
"""


class Student:  # 类的名称由一个或多个单词组成,每个单词的首字母大写,其余小写
    pass


#Student是对象吗? 内存有开辟空间吗?
print(id(Student))    # 24925624  #开辟的内存空间
print(type(Student))    # <class 'type'>
print(Student)    # <class '__main__.Student'>