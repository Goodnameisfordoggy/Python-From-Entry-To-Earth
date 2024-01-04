"""
字符串的去重
    not in
"""
s = "helloworldhelloworldhdjincmlcsza"

#not in
new_s = ''
for item in s:
    if item not in new_s:
        new_s += item
print(new_s)    # helowrdjincmsza

#索引 + not in
new_s2 = ''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2 += s[i]
print(new_s2)    # helowrdjincmsza

#通过集合去重
new_s3 = list(set(s))
new_s3.sort(key=s.index)# 排序关键字
print(''.join(new_s3))    # helowrdjincmsza