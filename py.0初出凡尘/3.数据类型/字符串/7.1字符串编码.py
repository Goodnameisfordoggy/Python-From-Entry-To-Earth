"""
字符串编码
    最早字符串编码是美国的标准信息交换码,ASCLL,最多可以表示256个符号,一个字符占一个字节
    中文编码:
    GBK:我国定制的编码标准,英文占一个字节,中文占两个字节.
    GB2312:我国定制的编码标准,英文占一个字节,中文占两个字节.
    UTF-8:国际通用的编码,英文占一个字节,中文占三个字节.
"""
#字符串的编码(将str类型转成bytes类型)
 #str.encode(encoding="utf-8", errors="strict/ignore/replace")
s = "我爱你中国"
scode_gbk = s.encode("gbk")
print(scode_gbk)     # b'\xce\xd2\xb0\xae\xc4\xe3\xd6\xd0\xb9\xfa'

scode_utf8 = s.encode("utf-8")
print(scode_utf8)    # b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0\xe4\xb8\xad\xe5\x9b\xbd'
print("===============================================================================================================")
#编码中的error处理
s2 = "特殊₯"
 #替换
scode1 = s2.encode("gbk", errors="replace")
print(scode1)    # b'\xcc\xd8\xca\xe2?'#遇到编码表未收录的字符会用'?'代替
 #忽略
scode2 = s2.encode("gbk", errors="ignore")
print(scode2)    # b'\xcc\xd8\xca\xe2'
 #严格处理
#scode3 = s2.encode("gbk", errors='strict')    #UnicodeEncodeError: 'gbk' codec can't encode character '\u20af' in position 2: illegal multibyte sequence
#print(scode3)