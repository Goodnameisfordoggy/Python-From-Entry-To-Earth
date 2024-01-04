# sample() 是 random 模块下的一个方法，用于从指定序列中随机选择指定数量的元素。该方法不会修改原始序列。
import random
"""
其中，sequence 表示待处理的序列，k 表示需要选择的元素个数。
如果指定的 k 大于 sequence 的长度，则会引发 ValueError 异常。
注意:
    返回的结果是一个列表对象。
    sequence 可以是字符串、列表、元组或集合等序列类型。
    在选择元素时，不允许重复选择。如果希望允许重复选择，则可以使用 random.choices() 方法。
    random.sample() 方法不会改变原始序列中元素的排列顺序。
"""

# 从列表中随机选择两个元素
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = random.sample(my_list, 2)
print(result)