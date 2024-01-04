#tuple()将其他类型数据转换为元组类型,与其他类型转列表类型的规则相同

 #
a = 123
#tuple(a)    # TypeError: 'int' object is not iterable

 #
b = "HDJ666"
print(tuple(b))   # ('H', 'D', 'J', '6', '6', '6')

 #
c = (1, 2, 3, "HDJ")
print(tuple(c))   # (1, 2, 3, 'HDJ')

 #
d = {
    "名字": "Goodnameisfordoggy",
    ("HDJ", 666): None,
}
print(tuple(d))    # ('名字', ('HDJ', 666))

 #
e = {1, 2, "3", "4", "5", (6, 7, 8)}
print(tuple(e))   # (1, 2, '4', (6, 7, 8), '3', '5')