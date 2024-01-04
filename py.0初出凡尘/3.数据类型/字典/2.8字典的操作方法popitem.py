 #popitem(用于删除字典最后一项,并以元组的形式返回该项对应的键和值)
d = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
r = d.popitem()
print(d)             # {'名字': 'Goodnameisfordoggy'}
print(r)             # ('年龄', 18)