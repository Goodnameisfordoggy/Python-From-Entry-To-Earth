# choice() 是 random 模块下的一个方法，用于从序列中随机选择一个元素。
import random
"""
其中，sequence 表示要操作的序列。
如果 sequence 序列为空，则 random.choice() 方法将引发 IndexError 异常
"""

# 从列表中随机选择一个元素
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = random.choice(my_list)
print(result)