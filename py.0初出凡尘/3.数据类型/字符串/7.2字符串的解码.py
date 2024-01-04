#字符串的解码(将bytes类型转成str类型)
 #bytes.decode(encoding="utf-8", errors="strict/ignore/replace")

#来自7.1
scode_gbk = b'\xce\xd2\xb0\xae\xc4\xe3\xd6\xd0\xb9\xfa'
scode_utf8 = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0\xe4\xb8\xad\xe5\x9b\xbd'
scode1 = b'\xcc\xd8\xca\xe2?'
scode2 = b'\xcc\xd8\xca\xe2'

S1 = bytes.decode(scode_gbk, "gbk")
print(S1)    # 我爱你中国

S2 = bytes.decode(scode_utf8, "utf-8")
print(S2)    # 我爱你中国
#编码中的error处理
 #替换
S3 = bytes.decode(scode1, "gbk", errors="replace")
print(S3)    # 特殊?
 #忽略
S4 = bytes.decode(scode2, "gbk", errors="ignore")
print(S4)    # 特殊
 #严格处理在此处无意义
S5 = bytes.decode(scode1, "gbk", errors="strict")
print(S5)    # 特殊?
S6 = bytes.decode(scode2, "gbk", errors="strict")
print(S6)    # 特殊