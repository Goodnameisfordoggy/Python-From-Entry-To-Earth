# break & continue在for&while循环中运用
 # break 可以跳出for 和while 的循环体
for i in "python":
    print(i)
    if i == 'h':
        break  # p/y/t/h

print("===================================================")
 # continue 跳过当前循环块中剩余的语句,然后继续进行下一轮循环
for i in "python":
    # 跳过 i==t 这一轮的输出操作
    if i == 't':
        continue
    print("当前的字母是:", i)
    # 当前的字母是: p
    # 当前的字母是: y
    # 当前的字母是: h
    # 当前的字母是: o
    # 当前的字母是: n

# break & continue在while循环中运用
 #与在for循环中的规则相同(注意: 两者都需考虑 条件语句,输出语句,break/continue 的先后顺序与逻辑关系)
a = 0
while a < 6:
    print("当前a的值:", a)
    a += 1
    if a == 3:
        continue
print("=============================================")
a = 0
while a < 6:
    a += 1
    if a == 3:
        continue
    print("当前a的值:", a)