"""
函数的返回值
    python中的函数可以使用return返回数值,也可以不用return返回,则默认返回"None"
    return,用在函数执行的时候,返回处理好的结果
"""
#print无返回值


#def abc():
    #print("Hello")


#r = abc()    # Hello
#print(r)    # None

#用return返回单个数据


def abc(a):
    return a+100


r = abc(900)
print(r)    # 1000

#用return返回多个数据


def abc(a, b, c):
    return a+100, b+200, c+300


r = abc(100, 200, 300)
print(r, type(r))   # (200, 400, 600) <class 'tuple'>
 #将元组中元素逐个提取(解包)
x, y, z = r
print(x)    # 200
print(y)    # 400
print(z)    # 600