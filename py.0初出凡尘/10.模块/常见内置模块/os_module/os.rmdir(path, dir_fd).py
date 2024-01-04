#rmdir(path)    删除目录
import os
os.rmdir('使用mkdir()创建的目录')
# QwQ:若对象为多级目录会报错  OSError: [WinError 145] 目录不是空的。: '使用makedirs()创建的多级目录'
