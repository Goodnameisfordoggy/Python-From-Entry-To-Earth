#remove 删除集合中的元素 如果有直接删除 如果没有会报错
a = {"python", "Goodnameisfordoggy", "学"}
a.remove("学")
print(a)                       # {'python', 'Goodnameisfordoggy'}

#a.remove("666")                # KeyError: '666'

 #pop随机删除集合中的元素 若集合中没有元素会报错
a = {"python", "Goodnameisfordoggy", "学"}
a.pop()
print(a)                        # 第一次运行{'python', 'Goodnameisfordoggy'}#第二次运行{'学', 'Goodnameisfordoggy'}

 #discard 如果元素存在直接删除 若不存在不做任何操作(返回原集合)
a = {"python", "Goodnameisfordoggy", "学"}
a.discard("学")
print(a)                        # {'python', 'Goodnameisfordoggy'}

a = {"python", "Goodnameisfordoggy", "学"}
a.discard("666")
print(a)                        # {'学', 'Goodnameisfordoggy', 'python'}