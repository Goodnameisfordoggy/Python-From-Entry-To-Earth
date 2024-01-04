#检测数据类型的方法type()
a = 123
b = "123"
c = [1, 2, 3]
d = (1, 2, 3)
e = {1, 2, 3}
f = {"1": 1,
     "2": 2}
g = True
h = 3.14
print(type(a))          # <class 'int'>    #整型
print(type(b))          # <class 'str'>    #字符串
print(type(c))          # <class 'list'>   #列表
print(type(d))          # <class 'tuple'>  #元组
print(type(e))          # <class 'set'>    #集合
print(type(f))          # <class 'dict'>   #字典
print(type(g))          # <class 'bool'>   #布尔值
print(type(h))          # <class 'float'>  #浮点型
#type()中也可以直接放数据
print("=========================================")
print(type("HDJ"))      # <class 'str'>
