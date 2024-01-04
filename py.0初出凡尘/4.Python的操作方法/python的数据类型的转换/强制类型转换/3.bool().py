#bool() 可以把其他类型转为True 或 False
 #数字类型转布尔类型(int类型: 0为False 其余数为True, float类型: 0.0为False 其余数为True)
a1 = 0
a2 = 0.0
a3 = 100
a4 = None
print(bool(a1), type(bool(a1)))    # False <class 'bool'>
print(bool(a2), type(bool(a2)))    # False <class 'bool'>
print(bool(a3), type(bool(a3)))    # True <class 'bool'>
print(bool(a4), type(bool(a4)))    # False <class 'bool'>

 #容器类型转布尔类型(容器类型包括: 字符串, 列表, 元组, 字典, 集合) 容器中为空: false 容器中有元素: True
a = ""
A = " "# 空格也算元素
b = [None]
c = (None,)
d = {}
e = set()
print(bool(a), type(bool(a)))   # False <class 'bool'>
print(bool(A), type(bool(A)))   # True <class 'bool'>
print("===========================================================================================")
 #None放在容器中只能作为元素,不能表示该容器为空
print(bool(b), type(bool(b)))    # True <class 'bool'>
print(bool(c), type(bool(c)))    # True <class 'bool'>
