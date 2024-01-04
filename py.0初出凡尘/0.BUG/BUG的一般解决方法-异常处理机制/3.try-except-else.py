"""
try-except-else
    若没有出错else可继续执行其后代码
"""
try:
    a = int(input("请输入第一个整数"))
    b = int(input("请输入第二个整数"))
    result = a / b
    print(result)

except BaseException as error:# 若不清楚其他的错误类型可以在最后增加BaseException
    print("出错了", error)
else:
    print("计算结果为:", result)    # input 8 2    # 4.0
