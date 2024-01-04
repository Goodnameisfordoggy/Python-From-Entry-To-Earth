#查找一个子串在字符串中是否存在(若不存在会报错,存在返回找到的首个子串的第一个字符的下标)
st = "123123456789"

print(st.index('34'))    # 5
#print(st.index("10"))    # ValueError: substring not found