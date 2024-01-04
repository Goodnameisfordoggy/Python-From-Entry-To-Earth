#字符串的常用方法 find & count
s1 = "python HDJ python"

 #find查找字符位置
print(s1.find("o"))                # 4 #find会返回第一个所查找字符的下标
print(s1.find("o", 6, 16))         # 15 #在6~16中查找字符
print(s1.find("a"))                # -1  #若当前字符串中没有要查找的字符 find的返回值为-1

 #count会统计字符在字符串中出现的次数
print(s1.count("o"))            # 2
print(s1.count("o", 6, 16))     # 1
print(s1.count("a"))            # 0