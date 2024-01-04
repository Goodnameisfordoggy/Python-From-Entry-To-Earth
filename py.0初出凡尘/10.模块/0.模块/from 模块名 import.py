#from 模块名称 import 函数名/变量名/类名
from math import pi
print(pi)    # 3.141592653589793
print(pow(2, 3))    # 8  QwQ:此时使用的pow函数并不是math模块中的

from math import pow
print(pow(2, 3))    # 8.0  QwQ:现在使用的是math模块中的pow,得到的结果为float类型