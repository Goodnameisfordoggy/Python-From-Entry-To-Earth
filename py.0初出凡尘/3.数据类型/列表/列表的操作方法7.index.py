#index(用于返回所匹配的函数索引(下标). 若有重复元素仅匹配第一个. 参数1:待查找对象 参数2:起始范围 参数3:结束范围)
a = ["hello", "world", "python", "hello"]
print(a.index("hello"))                       # 0

a = ["hello", "world", "python", "hello"]
print(a.index("hello", 1, 4))                 # 3
  #index的范围取左不取右
a = ["hello", "world", "python", "hello"]
print(a.index("hello", 0, 4))                 # 0
#a = ["hello", "world", "python", "hello"]
#print(a.index("hello", 1, 3))                 #ValueError: 'hello' is not in list