#copy(用于创建字典的副本,修改原字典对象,不会影响其副本)
d2 = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
d3 = d2.copy()# d3为复制出的副本
del d2["名字"]
print(d2)            # {'年龄': 18}
print(d3)            # {'名字': 'Goodnameisfordoggy', '年龄': 18}
  #同理 对副本的修改对原字典也无影响
d2 = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
d4 = d2.copy()
del d4["名字"]
print(d2)            # {'名字': 'Goodnameisfordoggy', '年龄': 18}
print(d4)            # {'年龄': 18}