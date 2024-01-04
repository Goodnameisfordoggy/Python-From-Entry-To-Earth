#get(用于字典获取指定键的值.在get函数中可以设置默认值,当get函数没有获取到对应键是,get函数会将默认值返回
d = {
    "名字": "Goodnameisfordoggy",
    "年龄": 18
}
print(d.get("名字"))               # Goodnameisfordoggy
print(d.get("技能"))               # None  #若键无默认值则返回空值
  #给键添加默认值(次操作不会改变原字典)
print(d.get("技能", "Python"))     # Python
print(d)                          # {'名字': 'Goodnameisfordoggy', '年龄': 18}#