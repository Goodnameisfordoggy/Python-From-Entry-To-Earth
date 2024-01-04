"""
#for
    for循环用来遍历序列
    通过不适用下标的方式来实现对序列中每一个元素的访问
    列表/元组/字符串/字典/集合
    for遍历数字用range()
"""
#列表/元组/集合
for i in [1, 2, 3]:
    print(i)   # 1/2/3
#字符串
for i in "HDJ":
    print(i)   # H/D/J
#字典(单独的for循环只会遍历每个键)
for i in {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}:
    print(i)   # 名字/年龄
 #可用items()获取字典的全部键和值再遍历,以元组的形式返回
d = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
for i in d.items():
    print(i)    # ('名字', 'Goodnameisfordoggy')/('年龄', 18)
#range()(取左不取右)
for i in range(0, 5):
    print(i)   # 1/2/3/4/5
 #步长
for i in range(0, 4, 2):
    print(i)   # 0/2