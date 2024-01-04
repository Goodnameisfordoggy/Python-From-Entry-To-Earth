# chdir(path)    将path设置为当前工作目录
import os
os.chdir('/py入门/10.模块/常见内置模块/os_module\\使用makedirs()创建的多级目录')
print(os.getcwd())    # D:\Users\Goodnameisfordoggy\PycharmProjects\pythonProject\py入门\10.模块\常见内置模块\os\使用makedirs()创建的多级目录

os.chdir('/py.0入门')
print(os.getcwd())    # D:\Users\Goodnameisfordoggy\PycharmProjects\pythonProject\py入门
# QwQ:os.chdir()可以跨级设置当前工作目录
