"""
re.spilt()
    功能与字符串操作中的spilt相同
    re.split(pattern, string, maxsplit, flags=0)
"""
import re
s = "https://www.baidu/s?wd=hdj&ie=utf-8&tn=baidu"
pattern = "[?|&]"
lst = re.split(pattern, s)
print(lst)    # ['https://www.baidu/s', 'wd=hdj', 'ie=utf-8', 'tn=baidu']