#add可以往集合中添加元素   数字/字符串/元组
a = {1, 2, 3}
a.add(6)
print(a)                 # {1, 2, 3, 6}
a.add("HDJ")
print(a)                 # {1, 2, 3, 6, 'HDJ'}
a.add((1, 2, 3))
print(a)                 # {1, 2, 3, 'HDJ', 6, (1, 2, 3)}