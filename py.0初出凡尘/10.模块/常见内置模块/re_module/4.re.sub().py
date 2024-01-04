"""
re.sub()
    用于实现字符串的替换
    re.sub(pattern, repl, string, count, flags=0)
          (模式字符串,替换字符串,原始字符串,最大替换次数(默认替换所有),可选参数)
"""
import re
pattern = "黑客|破解|反爬"
s = "我想学习python,想破解一些VIP视频,python可以实现无底线反爬吗?"
new_s = re.sub(pattern, "**", s)
print(new_s)    # 我想学习python,想**一些VIP视频,python可以实现无底线**吗?