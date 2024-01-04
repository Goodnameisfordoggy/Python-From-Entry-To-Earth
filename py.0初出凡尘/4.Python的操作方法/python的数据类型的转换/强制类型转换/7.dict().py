#dict()其他类型转字典类型

    #1.数字类型为非容器类型,不能转换为字典
a = 123
#print(dict(a))    # TypeError: 'int' object is not iterable

    #2.字符串不能转换为字典,因为字符串不能生成二级容器
b = "abc我爱你"
#print(dict(b))    # ValueError: dictionary update sequence element #0 has length 1; 2 is required

    #3.列表类型转字符串类型,列表必须为等长二级容器,子容器中的元素个数必须为2
c = [1, 2, 3, 4]# 一级容器
c1 = [1, 2, [3, 4]]# 一级容器与二级容器混合
c2 = [[1, 2], ["名字", "Goodnameisfordoggy"], ["年龄", 18]]# 符合要求: (等长 仅含有二级容器 子容器元素个数为2)
#print(dict(c))    # SyntaxError: unexpected EOF while parsing
#print(dict(c1))   # SyntaxError: unexpected EOF while parsing
print(dict(c2))    # {1: 2, '名字': 'Goodnameisfordoggy', '年龄': 18}

    #4.元组类型转字符串类型,元组必须为等长二级容器,子容器中的元素个数必须为2
    #与列表一样

    #5.集合不能转换为字典类型
e = {{"名字", "Goodnameisfordoggy"}, {"年龄", 18}}
#print(dict(e))    # TypeError: unhashable type: 'set'