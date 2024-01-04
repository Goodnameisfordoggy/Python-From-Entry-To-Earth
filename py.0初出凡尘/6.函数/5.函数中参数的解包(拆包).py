"""
函数中参数的解包(拆包):
    参数数据类型是:字符串/列表/元组/集合/字典的时候可以解包
    传递实参时,可以在序列类型的参数前添加'*',这样它会将序列中的元素依次作为参数传递,且序列内元素个数必须与实参个数相同.
"""
#(对照)使用位置参数


def abc(a, b, c):
    print(a)    # 100
    print(b)    # 200
    print(c)    # 300


abc(100, 200, 300)
print("===========================================================")

#运用解包(所谓的解包在这里就是将字符串"123"中的元素分别传给形参a, b, c)
 #字符串/列表/元组/集合 规则相同 使用(*函数名)
s = "123"


def abc(a, b, c):
    print(a)    # 1
    print(b)    # 2
    print(c)    # 3


abc(*s)
print("===========================================================")

 #字典 使用(**函数名)
  #(对照) 使用(*函数名)仅将字典的键传给实参
d1 = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18,
    "技能": "python"
}

abc(*d1)    # 名字/年龄/技能
print("===========================================================")

  #使用(**函数名)仅将字典的值传给实参
   #注意错误1.
#abc(**d)    # TypeError: abc() got an unexpected keyword argument '名字'#在解包时字典的键等同于函数的参数名(在此键名与形参不同会报错)

  #注意错误2.
d2 = {
    0: "Goodnameisfordoggy",
    1: 18,
    (1, 2, 3): "python"
}

#abc(**d2)   # TypeError: abc() keywords must be strings#在解包时字典的键等同于函数的参数名(在此仅支持字符串格式)

  #注意错误3.
d3 = {
    "name": "Goodnameisfordoggy",
    "age": 18,
    "skill": "python"
}

#abc(**d3)   # TypeError: abc() got an unexpected keyword argument 'name' -> 得到一个意外的关键字参数(并不是不支持键名为中文)

  #正确方式(在使用(**参数名)的格式中,字典的 键 必须与函数的 形参 相同)
d4 = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18,
    "技能": "python"
}


def abc(名字, 年龄, 技能):
    print(名字, '/',  年龄, '/', 技能)


abc(**d4)   # Goodnameisfordoggy / 18 / python