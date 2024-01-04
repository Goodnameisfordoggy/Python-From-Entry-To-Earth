"""
try-多个except
    捕获异常的顺序按照先子类后父类的顺序,为了避免遗漏可能出现的异常,可以在最后增加BaseException
"""
try:
    a = int(input("请输入第一个整数"))
    b = int(input("请输入第二个整数"))
    result = a / b
    print(result)

except ZeroDivisionError:
    print("除数不能为0!")
except ValueError:
    print("只能输入数字串!")
except BaseException as error:# 若不清楚其他的错误类型可以在最后增加BaseException
    print("出错了", error)
print("程序结束")