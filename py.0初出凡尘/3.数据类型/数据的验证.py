"""
数据的验证(返回值均为布尔类型)
    对用户输入数据进行"合法"性验证
    str.isdigit()      #所有字符都是数字(十进制阿拉伯数字)
    str.isnumeric()    #所有字符都是数字(全体数字)
    str.isalpha()      #所有字符都是字母(包括中文字符)
    str.isalnum()      #所有字符都是数字或字母(包括中文字符)
    str.islower()      #所有字符都是小写(仅对于字母进行判断,其余字符无影响)
    str.isupper()      #所有字符都是大写(仅对于字母进行判断,其余字符无影响)
    str.istitle()      #所有字符都是首字母大写(仅对于字母进行判断,其余字符无影响)
    str.isspace()      #所有字符都是空白字符(\n, \t)
"""
#str.isdigit()
print("123".isdigit())    # True
print("一二三".isdigit())    # False
print("1230e".isdigit())    # False
print("===============================================================================================================")
#str.isnumeric()
print("123".isnumeric())    # True
print("一二三".isnumeric())    # True
print("壹贰叁".isnumeric())    # True
print("0b1001".isnumeric())    # False
print("===============================================================================================================")
#str.istitle()
print("Hello world".istitle())    # False
print("Hello World".istitle())    # True
print("你好hello".istitle())    # False
print("你好Hello".istitle())    # True
print("===============================================================================================================")
#str.isspace()
print("\n".isspace())    # True
print("\t".isspace())    # True
print("   ".isspace())    # True