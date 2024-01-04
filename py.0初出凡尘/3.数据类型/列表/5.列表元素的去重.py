lst = ['金星', '木星', '水星', '火星', '土星', '金星', '木星', '水星', '火星', '土星', '金星', '木星', '水星', '火星', '土星']

#遍历 + not in
new_lst = []
for item in lst:
    if item not in new_lst:
        new_lst.append(item)
print(new_lst)    # ['金星', '木星', '水星', '火星', '土星']

#索引 + not in
new_lst2 = []
for i in range(len(lst)):
    if lst[i] not in new_lst2:
        new_lst2.append(lst[i])
print(new_lst2)    # ['金星', '木星', '水星', '火星', '土星']

#集合去重
new_lst3 = list(set(lst))
new_lst3.sort(key=lst.index)
print(new_lst3)    # ['金星', '木星', '水星', '火星', '土星']

