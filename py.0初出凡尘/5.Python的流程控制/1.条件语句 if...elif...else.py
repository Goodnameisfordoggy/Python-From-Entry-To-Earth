# python的条件语句:if...elif...else
# if
if 3 < 6:
    print("HELLO")  # 此处必须缩进
if True:
    print("HELLO")  # HELLO #真值会运行输出
if False:
    print("HELLO")  # 假值不输出

# elif
if 2 > 1:
    print(1)
elif 3 > 2:
    print(2)
elif 4 > 3:
    print(3)  # 1 #从if开始(含if项)无论其后跟多少条elif语句,只选择第一条为真的语句执行

# else
if 2 < 1:
    print(1)
elif 3 < 2:
    print(2)
elif 4 < 3:
    print(3)
else:
    print("若以上条件均不满足则执行else下的语句")  # 若以上条件均不满足则执行else下的语句