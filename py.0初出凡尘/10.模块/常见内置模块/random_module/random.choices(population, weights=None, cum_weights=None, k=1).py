# choices() 是 random 模块下的一个方法，用于从指定序列中随机选择指定数量的元素，并可以允许出现重复的元素。
import random
"""
其中，
population 表示待处理的序列（不能为空），
k 表示要选择的元素个数。
weights 表示每个元素被选中的概率，cum_weights 表示权重的累计值（这两个参数二选一，如果都提供则使用 weights）。
如果未提供 weights 或 cum_weights，则所有元素被选择的概率是相等的。
"""

# 从指定的 序列 中随机选择 5个元素，同时指定每个元素被选择的概率
my_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
weights = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
result = random.choices(my_list, weights=weights, k=5)
print(result)