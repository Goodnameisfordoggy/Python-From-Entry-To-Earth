"""
#2.默认参数
    默认参数是指带有默认值的参数,在对该函数进行调用的时候,可以不必显示传递给该函数.当不传递值的时候,函数将使用默认值
    注意:默认值只能执行一次这条规则在默认值为可变对象(列表,字典以及大多数类的实例)时非常重要
        官方建议默认参数尽量使用不可变对象!
        因为可变对象会储存在后续调用中传递传递给它的参数
"""
#abc() 省略传入所有参数,函数会使用默认参数的默认值


def abc(a=100, b=200):
    print(a+b)


abc()   #300
 #传参时只有一个值,则为第一个默认参数传入值,另一个继续使用默认值
abc(800)    # 1000
 #指定一个默认参数传值
abc(b=1000)    # 1000

#可变对象会储存在后续调用中传递传递给它的参数


def abc(a, b=[]):
    b.append(a)
    print(b)

 #第一次调用


abc("666")    # ['666']
 #第二次调用
abc("HDJ")    # ['666', 'HDJ']
 #第三次调用
abc("PYTHON")    # ['666', 'HDJ', 'PYTHON']

 #若需求为:将每次传递的参数单独输出
  #方法1.


def abc(a, b=None):
    if b is None:
        b = []
    b.append(a)
    print(b)


abc(100)    # [100]
abc(200)    # [200]

  #方法2.


def abc(a, b=[]):
    b.append(a)
    print(b)
    b.clear()


abc(100)    # [100]
abc(200)    # [200]