"""
字符串的拼接
    使用'+'
    使用str.join()
    直接拼接
    使用格式化字符串进行拼接
"""
#字符串的拼接 +
a = '我'+"爱你"+"中国"
print(a)               # 我爱你中国
b = '100'+'50'
print(b)               # 10050

m = "abc"
n = "def"
o = "ghi"
p = m+n+o
print(p)               # abcdefghi
#使用str.join()
q = ','.join((m, n, o))
print(q)               # abc,def,ghi
#直接拼接
print("hello""world")    # helloworld
#使用格式化字符串进行拼接
print("%s%s" % (m, n))    # abcdef
print(f"{m}{n}")    # abcdef
print("{0}{1}".format(m, n))    # abcdef