#元组的拼接&与更新
 #元组拼接
t1 = ("hello", "DHJ", 666)
t2 = ("我爱学习", "python")
t3 = ([1, 2], [10, 1000000000000])
print(t1+t2+t3)                      # ('hello', 'DHJ', 666, '我爱学习', 'python', [1, 2], [10, 1000000000000])

#若元组中的元素有列表 那么我们可以更改列表中的元素
t4 = t1+t2+t3
t4[6][0] = "$$$$$"
print(t4)                            # ('hello', 'DHJ', 666, '我爱学习', 'python', [1, 2], ['$$$$$', 1000000000000])