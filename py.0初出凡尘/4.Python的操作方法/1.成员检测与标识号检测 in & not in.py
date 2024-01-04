"""
#成员检测与标识号检测 in & not in
  使用"in" 和"not in"运算符来判断某个对象是否为序列的成员
  in: 判断对象视为在序列(列表/字符串/元组/字典)中,如果是则返回True
  not in: 判断对象是否不在序列中,如果是则返回True
"""

#in
print("4" in "1234")       # True
print(4 in (1, 2, 3, 4))   # True
print(4 in [1, 2, 3, 4])   # True
 #对于字典来说 判断对象仅为键
print("名字" in {"名字": "Goodnameisfordoggy", "年龄": 18})     # True
print("Goodnameisfordoggy" in {"名字": "Goodnameisfordoggy", "年龄": 18})   # False

#not in
print(4 not in (1, 2, 3, 4))   # False
print(4 not in (2, 2, 2, 2))   # True