"""
#判断两个对象是否相同 is & is not
  is(是)判断对象是否相同
  not is(不是)判断对象是否不相同
"""

a = "Goodnameisfordoggy"
b = 18
print(a is b)       # False
print(a is not b)   # True

 #数字/字符串/元组 数据类型与元素完全相同才算相同(不可变数据)
c = "111"
d = 111
print(c is d)       # False
c = "111"
d = "111"
print(c is d)       # True

 #列表/字典/集合 表面一样 其实不是同一个对象(可变数据)
f = [1, 2]
g = [1, 2]
print(f is g)        # False

aa = {"name": "HDJ"}
bb = {"name": "HDJ"}
print(aa is bb)      # False