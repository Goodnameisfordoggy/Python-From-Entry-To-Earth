# py关键词：
```py
import keyword
print(keyword.kwlist)

#'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
#'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
#'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise','return', 'try',
#'while', 'with', 'yield'
```

## False, True, None
False, True和None是Python中的布尔值和空值。它们用于表示逻辑上的假、真和空对象。
False和True是布尔数据类型的两个值，用于逻辑运算和控制流程。
None用于表示空值或缺少值的情况，通常用作函数的默认返回值或变量的初始值。
```py
# 布尔数据类型
if False:
    print("这段代码不会被执行")
# 作为关键字
False = 1  # 这会导致语法错误，因为 False 是关键字，不能被赋值
# 逻辑运算
result = False and True  # 结果为 False
# 返回值
def check_value(value):
    if value > 10:
        return False
    else:
        return True

print(check_value(5))  # 输出 True
print(check_value(15)) # 输出 False
# 初始化变量
flag = False
if some_condition:
    flag = True

```
## and, or, not
and, or和not是逻辑运算符，用于组合和操作布尔值。
and表示逻辑与操作，当两个条件都为真时返回真。
or表示逻辑或操作，只要有一个条件为真就返回真。
not表示逻辑非操作，对布尔值取反。
```py
# 逻辑与操作符：
x = 5
y = 10
result = (x < 10) and (y > 5)
print(result)  # 输出 True，因为两个条件都成立

# 当用于两个操作数时，and 返回第一个为假的值，如果都为真，则返回最后一个为真的值。
x = 5
y = 3
result = x and y # 输出 3

# 使用在条件语句中：
if condition1 and condition2:
    print("执行当 condition1 和 condition2 都为 True 时的代码")

# 逻辑与的短路特性：
x = 5
y = 0
result = (y != 0) and (x / y > 2)  # 在这里，第二个表达式不会被计算，避免了除以零错误
```        

## if, elif, else:
if, elif（else if的缩写）和else是条件语句的关键字。
if用于条件判断，根据条件的真假执行相应的代码块。
elif用于多个条件判断，如果前面的条件不满足，则检查下一个条件。
else用于在所有条件都不满足时执行的代码块。

## for, while, break, continue
for和while是循环结构的关键字。
for用于遍历迭代器（如列表、元组、字典等）中的元素。
while用于根据条件循环执行代码块。
break用于跳出循环，终止整个循环的执行。
continue用于跳过当前循环的剩余代码，进入下一次循环。
in用于检查元素是否存在于某个容器对象中.

## def, return
def用于定义函数，后面跟着函数名和参数列表。
return用于函数中，表示函数的返回值，并且终止函数的执行并将值传递给调用者。

## class, pass
class用于定义类，创建对象的模板。
pass是占位符，用于表示空操作，通常用作占据语法位置而不执行任何操作。

## in, is
in用于检查元素是否存在于某个容器对象中.
is用于比较两个对象是否相同（身份比较）。

## global, nonlocal
global用于在函数内部声明全局变量，允许在函数内部修改全局变量。
nonlocal用于在嵌套函数中声明变量，指示变量来自于外层函数的作用域。

## as         
## assert     


  
## del        

## except     
     
## finally    
## from
## import     

## lambda     
## raise      
## try
## with       
## yield

