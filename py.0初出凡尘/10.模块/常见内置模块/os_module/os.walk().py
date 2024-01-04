#os.walk() 获取所有的文件路径 目录名 文件名
import os
os.chdir('/py入门/10.模块/常见内置模块/os_module')
files = os.walk(os.getcwd())

for dirpath, dirnames, filenames in files:
    print(dirpath)
    print(dirnames)
    print(filenames)
    print(1000 * '*')
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
    for filename in filenames:
        print(os.path.join(dirpath, filename))
    print(1000*'=')