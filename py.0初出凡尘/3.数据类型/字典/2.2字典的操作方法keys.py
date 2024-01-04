 #keys(将以列表的形式返回字典中的所有键)
f = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18,
    "技能": {
        "技能1": "Python",
        "技能2": "C++"
    }
}
print(f.keys())                 # dict_keys(['名字', '年龄', '技能']) #keys函数只能返回第一层字典的键