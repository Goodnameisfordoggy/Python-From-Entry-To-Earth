#update(用于将字典2的值更新到字典1.) 若字典2的键在字典1中已存在,则对字典1进行修改; 若不存在,则对字典1进行添加
d1 = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
d2 = {
    "名字": "HDJ",
}
d1.update(d2)
print(d1)            # {'名字': 'HDJ', '年龄': 18}

d1 = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
d2 = {
    "技能": "Python",
}
d1.update(d2)
print(d1)            # {'名字': 'Goodnameisfordoggy', '年龄': 18, '技能': 'Python'}