"""
try-except-else-finally
    finally下的代码无论是否出错都会执行
"""
try:
    a = int(input("请输入第一个整数"))
    b = int(input("请输入第二个整数"))
    result = a / b
    print(result)

except BaseException as error:# 若不清楚其他的错误类型可以在最后增加BaseException
    print("出错了", error)
else:
    print("计算结果为:", result)
finally:
    print("谢谢您的使用^_^")