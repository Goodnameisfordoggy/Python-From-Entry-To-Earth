"""
函数中各种参数排列位置时的注意事项
    1.可变参数{(*参数名)(**参数名)},必须定义在普通参数以及默认值参数的后面
    2.函数定义时,(*参数名)(**参数名)同时存在,一定要将*args放在**kwargs之前
    综上 格式为
        def 函数名(普通参数,默认值参数name="Goodnameisfordoggy",*参数名,**参数名)
            pass
"""


def abc(a, name="Goodnameisfordoggy", *args, **kwargs):
    print(a)    # 100
    print(name)    # 张三
    print(args)    # (0.1, 0.01, 0.001)
    for i in args:# 遍历元组中的每个元素 用于单独提取使用
        print(i)    # 0.1/0.01/0.001
    print(kwargs)   # {'x': 10, 'y': 20, 'z': 30}
    for key, value in kwargs.items():
        print(key, value)   # x 10/y 20/z 30


abc(100, "张三", 0.1, 0.01, 0.001, x=10, y=20, z=30)
