"""
#isinstance()用来判断一个对象是否是一个已知的类型
    isinstance()函数的返回值为布尔值,
    若对象的类型是已知类型,那么返回True, 否则返回False
语法:isinstance(对象,对象类型)
"""
a = 123
b = 3.14
print(isinstance(a, int))    # True
print(isinstance(a, float))  # False
print(isinstance(b, (int, float, str)))     # True #此方式只要对象类型符合元组中任意类型则返回True
