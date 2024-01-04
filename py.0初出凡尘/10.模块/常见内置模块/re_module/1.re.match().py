"""
常用的正则处理方法
    re.match()
        用于从字符串的开始位置进行匹配,如果起始位置匹配成功,结果为Match对象,否则结果为None
        re.match(pattern,string,flags=0)
                (模式, 待匹配字符串, 可选参数:标志位)
"""
import re
pattern = r"\d\.\d+"
s = "I study Python3.6 every day"
match = re.match(pattern, s, re.I)# re.I忽略大小写
print(match)    # None

s2 = "3.6python I studay every day"
match2 = re.match(pattern, s2, )
print(match2)    # <_sre.SRE_Match object; span=(0, 3), match='3.6'>
print("匹配值的起始位置", match2.start())    # 匹配值的起始位置 0
print("匹配值的结束位置", match2.end())    # 匹配值的结束位置 3
print("匹配区间的位置元祖", match2.span())    # 匹配区间的位置元祖 (0, 3)
print("带匹配的字符串", match2.string)    # 带匹配的字符串 3.6python I studay every day
print("匹配的数据", match2.group())    # 匹配的数据 3.6
