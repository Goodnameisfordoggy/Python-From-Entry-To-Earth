"""
可变参数
    **参数:最常见的变量名是kwargs(日常工作时约定俗成的,但并不是不可改变的),看到该变量名,一眼就知道变量kwargs指向一个dict对象;
   自动收集所有未匹配的关键字参数到一个dict对象中,变量名kwargs指向了此dict对象
"""
#(对照)位置参数(调用时必须全部传参否则报错)


def abc(a, b):
    print(a)
    print(b)

#abc(100)    #TypeError: abc() missing 1 required positional argument: 'b'

#可变参数(**参数名)
 #给**kwargs传0个实参


def abc(a, **kwargs):
    print(a)    # 100
    print(kwargs)    #  {}#此时kwargs参数对应的是一个空字典
    print(type(kwargs))   # <class 'dict'>


abc(100)

 #给**kwargs传1个实参


def abc(a, **kwargs):
    print(a)    # 100
    print(kwargs)    # {'x': 200}


abc(100, x=200)
 #给**kwargs传多个实参, 自动收集所有未匹配的默认参数到一个dict对象中


def abc(a, **kwargs):
    print(a)    # 100
    print(kwargs)    # (200, 300, 400, 500)


abc(100, b=200, c=300, d=400, e=500)    # {'b': 200, 'c': 300, 'd': 400, 'e': 500}