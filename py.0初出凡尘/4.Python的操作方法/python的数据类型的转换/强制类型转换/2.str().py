#str()可以把其他数据类型转换成字符串类型(注意:所有类型都可以转换为字符串类型)
a = "123"
b = 123
 #写法一
res_b = str(b)
print(res_b, type(res_b))        # 123 <class 'str'>
c = [1, 2, 3]
d = (1, 2, 3)
e = {1, 2, 3}
f = {"1": 1,
     "2": 2
     }

 #写法二
print(str(f), type(str(f)))       # {'1': 1, '2': 2} <class 'str'>
g = True
h = 3.14