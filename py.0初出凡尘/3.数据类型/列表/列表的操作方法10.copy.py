#copy函数用于创建列表的副本
  #使用copy函数后 对a列表的处理对b列表无影响
a = ["hello", "world", "python", "hello"]
b = a.copy()
print(b)                                 # ['hello', 'world', 'python', 'hello']
del a[0]
print("删除a[0]元素后,输出b列表", b)        # ['hello', 'world', 'python', 'hello']
  #使用赋值操作后 对a列表的处理对b列表有影响
a = ["hello", "world", "python", "hello"]
b = a
print(b)                                 # ['hello', 'world', 'python', 'hello']
del a[0]
print("删除a[0]元素后,输出b列表", b)        # ['world', 'python', 'hello']