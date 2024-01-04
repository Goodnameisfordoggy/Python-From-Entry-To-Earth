"""
re.findall()
    用于在字符串中搜索所用符合正则表达式的值,结果为列表
    re.findall(pattern,string,flags=0)
"""
import re
pattern = r"\d\.\d+"
s = "I studay python 3.6 every day python 3.10 I love you"
s2 = "4.10python I studay every day"
s3 = "I studay python every day"

lst = re.findall(pattern, s)
lst2 = re.findall(pattern, s2)
lst3 = re.findall(pattern, s3)

print(lst)      # ['3.6', '3.10']
print(lst2)     # ['4.10']
print(lst3)     # []