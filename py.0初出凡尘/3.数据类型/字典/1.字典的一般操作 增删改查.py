#增加
d1 = {"名字": "Goodnameisfordoggy", "年龄": 18}
d1["技能"] = "Python"
print(d1)                         # {'名字': 'Goodnameisfordoggy', '年龄': 18, '技能': 'Python'}
 #删除(用del)
d2 = {"名字": "Goodnameisfordoggy", "年龄": 18}
del d2["年龄"]
print(d2)                         # {'名字': 'Goodnameisfordoggy'}
 #修改
d3 = {"名字": "HDJ", "年龄": 18}
print(d3)                         # {'名字': 'HDJ', '年龄': 18}
 #查找并获取
print(d3["年龄"])                  #18