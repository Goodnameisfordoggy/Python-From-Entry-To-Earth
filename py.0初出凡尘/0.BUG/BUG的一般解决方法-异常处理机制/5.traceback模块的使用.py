"""
Python 中常见的异常类型
        异常类型                   描述
    ZeroDivisionError        除(或取模)零 (所有数据类型)
    indexError               序列中没有次索引(index)
    KeyError                 映射中没有这个键
    NameError                未声明/初始化对象(没有属性)
    SyntaxError              python语法错误
    ValueError               传入无效参数
"""
"""
traceback模块的使用
    用于打印异常信息
"""
import traceback
try:
    print("==============注意此处================")
    print(10/0)
except:
    traceback.print_exc()
