"""
try-expect
    解决被动掉坑的问题
"""
#原代码
#a = int(input("请输入第一个整数"))
#b = int(input("请输入第二个整数"))
#result = a/b
#print(result)    # input q  # ValueError: invalid literal for int() with base 10: 'q'
                  # input 8 0  # ZeroDivisionError: division by zero

#应用异常捕获
try:
    a = int(input("请输入第一个整数"))
    b = int(input("请输入第二个整数"))
    result = a / b
    print(result)

except ZeroDivisionError:
    print("除数不能为0")
print("程序结束")