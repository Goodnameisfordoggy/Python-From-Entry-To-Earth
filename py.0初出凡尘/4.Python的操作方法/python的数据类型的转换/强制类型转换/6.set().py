#set()将其他数据类型转换为集合类型,可参考其他类型转列表类型的规则(几乎一样)

    #1.数字类型为非容器类型,不能转换为集合
a = 123
#tuple(a)    #TypeError: 'int' object is not iterable

    #2.容器类型(字符串/列表/元组/字典)转集合类型时,得到的结果是无序的,其中字典转集合时只保留键

 #
b = "HDJ666"
print(set(b))    # {'D', 'J', '6', 'H'}

 #
c = [1, 1, 2, 3, "HDJ", '666']
print(set(c))    # {'666', 1, 2, 3, 'HDJ'}

 #
d = (1, 3, 4, 6, "HDJ")
print(set(d))    # {1, 'HDJ', 3, 4, 6}

 #
e = {
    "名字": "Goodnameisfordoggy",
    ("HDJ", 666): None,
}
print(set(e))    # {('HDJ', 666), '名字'}