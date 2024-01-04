#update可以将集合合并
a = {1, 2, 3}
b = {'H', 'E'}
a.update(b)
print(a)                 # {'H', 1, 2, 3, 'E'}
print(b)                 # {'E', 'H'} #将b并入a后 b集合并没有被改变
