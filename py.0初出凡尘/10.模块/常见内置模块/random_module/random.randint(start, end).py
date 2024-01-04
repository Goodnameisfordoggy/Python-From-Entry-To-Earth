# randint() 是 random 模块下的一个方法，用于随机生成指定范围内的整数
import random
"""
其中，start 和 end 都是整数，表示随机数的范围（包括 start 和 end）这两个参数必填
"""

# 生成 0-9 之间的随机整数
num = random.randint(0, 9)
print(num)

# 生成 10-20 之间的随机整数
num = random.randint(10, 20)
print(num)