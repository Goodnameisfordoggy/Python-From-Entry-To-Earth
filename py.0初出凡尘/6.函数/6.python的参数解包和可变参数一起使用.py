#python的参数解包和可变参数一起使用(注意:(**参数名)只收集未匹配的关键字参数
 #(*参数名)
  #(对照)正常传参
def abc(a, *args):
    print(a)    # 100
    print(args)    # ((1, 2, 3),)


abc(100, (1, 2, 3))

  #


def abc(a, *args):
    print(a)    # 100
    print(args)    # (1, 2, 3)


abc(100, *[1, 2, 3])# 在序列类型前加'*'将其拆包后的元素填入元组

 #(**参数名)
  #(对照)正常传参


def abc(a, **kwargs):
    print(a)    # 100
    print(kwargs)   # {'x': 10, 'y': 20, 'z': 30}


abc(100, x=10, y=20, z=30)

  #
d = {
      "名字": "Goodnameisfordoggy",
      "年龄": 18
  }


def abc(a, **kwargs):
    print(a)    # 100
    print(kwargs)   # {'名字': 'Goodnameisfordoggy', '年龄': 18}


abc(100, **d)