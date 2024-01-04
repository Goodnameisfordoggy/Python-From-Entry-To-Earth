# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用

# 对列表按照升序排序
lst1 = [3, 1, 4, 2, 5]
res1 = sorted(lst1)
print(res1) # [1, 2, 3, 4, 5]

# 对列表按照降序排序
lst2 = [3, 1, 4, 2, 5]
res2 = sorted(lst2, reverse=True)
print(res2) # [5, 4, 3, 2, 1]

# 对列表按照长度降序排序
lst3 = ['apple', 'banana', 'pear', 'orange']
res3 = sorted(lst3, reverse=True, key=len)#reverse与key不存在一定的顺序
print(res3) # ['banana', 'orange', 'apple', 'pear']