#random.shuffle() shuffle 函数用于将可变序列中的元素随机排序，它可以接受一个可变序列作为参数。
# 注意: random.shuffle 函数会在原序列中随机交换元素，因此它会直接修改原序列，无需返回任何值。
# 在 Python 中，可变序列包括列表（List）和字节数组（bytearray），在 Python 3.9 及以上版本中还包括可变集合（MutableSet）等。
import random
from typing import MutableSet
#列表（List）
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list1)
print(list1)    # [7, 5, 6, 1, 3, 8, 4, 9, 2]

#字节数组（bytearray）
a = bytearray(b'hello')
random.shuffle(a)
print(a)    # bytearray(b'lhoel')


#一般集合
Set1: MutableSet[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#random.shuffle(Set1)  #QwQ:一般集合不支持索引访问  # TypeError: 'set' object does not support indexing
#print(Set1)

#元组
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#random.shuffle(tuple1)    # TypeError: 'tuple' object does not support item assignment
#print(tuple1)
#QwQ:所以元组可以先转换为列表排序后再转换回原类型
list2 = list(tuple1)
random.shuffle(list2)
print(tuple(list2))     # (2, 1, 8, 7, 5, 4, 6, 9, 3)
