"""
#可变参数
    *参数:最常见的变量名是args(日常工作时约定俗成的,但并不是不可改变的),看到该变量名,一眼就知道变量args指向一个tuple对象;
    自动收集所有未匹配的位置参数到一个tuple对象中,变量名args指向了此tuple对象
"""
#(对照)位置参数(调用时必须全部传参否则报错)


def ab(a, b):
    print(a)
    print(b)

#ab(100)    # TypeError: abc() missing 1 required positional argument: 'b'

#可变参数(*参数名)
 #给*args传0个实参


def abc(a, *args):
    print(a)    # 100
    print(args)    # ()#此时b参数对应的是一个空元组
    print(type(args))   # <class 'tuple'>


abc(100)

 #给*args传1个实参


def abc(a, *args):
    print(a)    # 100
    print(args)    # (200,)


abc(100, 200)

 #给*args传多个实参, 自动收集所有未匹配的位置参数到一个tuple对象中


def abc(a, *args):
    print(a)    # 100
    print(args)    # (200, 300, 400, 500)


abc(100, 200, 300, 400, 500)