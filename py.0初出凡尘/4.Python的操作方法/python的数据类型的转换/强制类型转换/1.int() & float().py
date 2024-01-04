#int() & float() (注意:*数字类型之间可以相互转换
                     #*只有字符串可以转换为数字类型,且字符串中的元素必须为数字,否则无法转换)
 #数字类型之间转换
a = 123
r_a = float(a)
print(r_a)     # 123.0

b = 3.14
r_b = int(b)# 不遵循四舍五入直接去除小数部分
print(r_b)     # 3

c = True
r_c = int(c)
print(r_c)     # 1
d = False
r_d = float(d)
print(r_d)     # 0.0
 #非数字类型转换为数字类型
e = "-123"
r_e = int(e)
f_e = float(e)
print(r_e, type(r_e))    # -123 <class 'int'>
print(f_e, type(f_e))    # -123.0 <class 'float'>

f = "123.45"
r_f = float(f)
#i_f = int(f) #字符串中是浮点型则不能转换为整型 根据(精度等级: 布尔 < 整型 < 浮点型  < 复数 )不同类型之间的转换,向高级兼容
#ValueError: invalid literal for int() with base 10: '123.45'
print(r_f, type(r_f))    # 123.45 <class 'float'>