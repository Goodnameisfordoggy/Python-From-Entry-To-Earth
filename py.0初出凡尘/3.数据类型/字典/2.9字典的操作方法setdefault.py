#setdefault(用于设置键的默认值) 若字典中该键已存在,则忽略设置;若不存在,则添加该键和值)
d = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
d.setdefault("名字", "HDJ")
print(d)             # {'名字': 'Goodnameisfordoggy', '年龄': 18}

d = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
d.setdefault("技能", "Python")
print(d)             # {'名字': 'Goodnameisfordoggy', '年龄': 18, '技能': 'Python'}