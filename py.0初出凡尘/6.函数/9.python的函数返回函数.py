"""
python的函数返回函数
    在函数里嵌套函数,用函数返回函数
"""


def abc():
    def xyz():
        return 666
    return xyz# 此时返回的是xyz这个函数


r = abc()# r接受的是一个函数 这里就相当于r变成了一个函数,且功能与abc函数完全相同
print(r)    # <function abc.<locals>.xyz at 0x022C3780>

 #验证r的功能
r2 = r()
print(r2)    #666