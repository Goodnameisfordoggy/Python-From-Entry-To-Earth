#元组的注意事项以及乘号的使用
 #元组在定义时无括号也是元组(输出时系统会自动添加括号)
a = (1, 2, 3, 4)
b = 1, 2, 3, 4
print(a)            # (1, 2, 3, 4)
print(b)            # (1, 2, 3, 4)
#元组内仅有一个元素时要在其后加','才能表示其为元组
c = ("HDJ")
print(c)
c = ("HDJ",)        # HDJ
print(c)            # ('HDJ',)
c = "HDJ",
print(c)            # ('HDJ',)

 #'*'的使用
d = (10,)
print(d*10)         # (10, 10, 10, 10, 10, 10, 10, 10, 10, 10)