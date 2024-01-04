"""
re.search()
    用于在整个字符串中搜索第一个匹配的值,如果匹配成功结果为match对象,否则结果为None
    re.search(pattern,string,flags=0)
"""
import re
pattern = r"\d\.\d+"
s = "I studay python 3.6 every day python 3.10 I love you"
s2 = "4.10python I studay every day"
s3 = "I studay python every day"

match = re.search(pattern, s)
match2 = re.search(pattern, s2)
match3 = re.search(pattern, s3)

print(match)    # <_sre.SRE_Match object; span=(16, 19), match='3.6'>
print(match.group())    # 3.6
print(match2)    # <_sre.SRE_Match object; span=(0, 4), match='4.10'>
print(match2.group())   # 4.10
print(match3)    # None
