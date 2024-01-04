 #pop(用于从字典中移除指定键,并返回该键所对应的值)
d = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
r = d.pop("名字")
print(d)                       # {'年龄': 18}
print(r)                       # Goodnameisfordoggy