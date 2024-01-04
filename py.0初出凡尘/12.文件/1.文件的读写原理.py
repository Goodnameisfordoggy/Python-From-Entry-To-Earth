"""
文件的读写操作
    语法规则:
        file = open(filename [,mode,encoding])
    被创建的文件对象 = 创建文件对象的函数( 要创建或打开的文件名 [,打开模式(默认只读),编码格式(默认文本文件中编码格式为GBK)] )
"""
file = open('txt1', 'r')
print(file.readline())
file.close()    # HDJ