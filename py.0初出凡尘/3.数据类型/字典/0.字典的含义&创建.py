"""
#字典是一种映射类型,它的元素是键值对,字典的键必须为不可变类型,且不能重复.键可以是任意不可变类型(元组/字符串/数字)
 字典的创建:
           1.直接用"{}"
           2.使用dict()
"""
a = {
    "姓名": "Goodnameisfordoggy",
    "年龄": 18
}
print(a)                 # {'姓名': 'Goodnameisfordoggy', '年龄': 18}

b = dict((["年龄",18],["名字","Goodnameisfordoggy"]))
print(b)                 # {'年龄': 18, '名字': 'Goodnameisfordoggy'}
#创建空集合
c = {}
print(c)                 # {}

d = set()
print(d)                 # set() #表达空集用set()

