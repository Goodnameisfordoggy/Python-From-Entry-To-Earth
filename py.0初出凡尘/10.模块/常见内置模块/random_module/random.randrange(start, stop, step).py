# randrange() 函数是 random 模块下的一个方法，用于随机生成指定范围内的整数。
import random
"""
其中，start、stop 和 step 都是整数。
start 表示随机数的起始值（包括），stop 表示随机数的结束值（不包括），step 表示步长（即每次增加或减少的值，默认为 1）。
如果只提供一个参数，则表示 stop，并以 0 为起始值，默认步长为 1。
"""

# 生成 0-9 之间的整数，包括 0，不包括 10
num = random.randrange(10)
print(num)

# 生成 10-20 之间的整数，不包括 20
num = random.randrange(10, 20)
print(num)

# 生成 0-100 之间以 10 为步长的整数
num = random.randrange(0, 100, 10)
print(num)