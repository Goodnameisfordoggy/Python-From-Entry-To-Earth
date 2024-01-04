#1.位置参数
def aaa(a, b):
    print(a+b)


aaa(66, 600)    # 666
aaa("i", "你")  # i你

#0.函数中的pass关键字 与在循环中的用法大致相同


def abc():
    pass
#使用位置参数,在调用函数时实参个数必须与形参个数相同


def ccc(a, b):
    print(a+b)
#ccc(6, 60, 600)   # TypeError: ccc() takes 2 positional arguments but 3 were given