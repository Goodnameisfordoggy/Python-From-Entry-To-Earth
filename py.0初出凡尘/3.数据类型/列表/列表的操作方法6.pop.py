#pop(用于移除列表中指定位置的元素,并返回要移除的元素.在默认情况下,移除列表中最后一个元素)
a = ["hello", "world", "python", "hello"]
a.pop(3)
print(a)                                  # ['hello', 'world', 'python']

a = ["hello", "world", "python", "hello"]
print("要移除的数据", a.pop(3))              # 要移除的数据 hello
print("更改后的数据", a)                    # 更改后的数据 ['hello', 'world', 'python']