#字典的操作方法2 items & values
 #items(以列表的形式返回字典中的所有键值对)
d = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
print(d.items())                         # dict_items([('名字', 'Goodnameisfordoggy'), ('年龄', 18)])
 #values(以列表的形式返回字典中的所有值)
d = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
print(d.values())                        # dict_values(['Goodnameisfordoggy', 18])
