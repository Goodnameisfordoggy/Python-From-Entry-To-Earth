#用于分割字符串(不添加参数默认以空格分割)
r = "I have an apple"

print(r.split())    # ['I', 'have', 'an', 'apple']

#使用参数
r = "I have an apple"
print(r.split('a'))    # ['I h', 've ', 'n ', 'pple']
