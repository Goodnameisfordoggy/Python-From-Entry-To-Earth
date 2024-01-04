# 集合的交集、并集、差集、对称差运算
set1 = {1, 2, 3, 5}
set2 = {1, 2, 7, 6}
set3 = {1, 2, 3, 4, 5, 6, 7}

#交集 使用 '&' 连接多个集合,得到相同的元素
print(set1 & set2)    # {1, 2}
# print(set1.intersection(set2))

#并集 使用 '|' 连接多个集合,得到全部元素
print(set1 | set2)    # {1, 2, 3, 5, 6, 7}
# print(set1.union(set2))

#差集
print(set1 - set2)    # {3, 5}
# print(set1.difference(set2))

#对称差
print(set1 ^ set2)    # {3, 5, 6, 7}
# print(set1.symmetric_difference(set2))


# 判断子集和超集
print(set1 <= set2)    # False
# print(set1.issubset(set2))
print(set1 <= set3)    # True
# print(set1.issubset(set3))
print(set1 >= set2)    # False
# print(set1.issuperset(set2))
print(set1 >= set3)    # False
# print(set1.issuperset(set3))