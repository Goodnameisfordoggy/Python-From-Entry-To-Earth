#sort函数给列表对象发出排序消息直接在列表对象上进行排序
# (常见ASCII码大小规则: 0~9 < A~Z < a~z)
  #升序
a = ["hello", "HDJ", "world", "python", "hello", "1"]
b = [1, 3, 2, 4, 5]
a.sort()
print(a)    # ['1', 'HDJ', 'hello', 'hello', 'python', 'world']

b.sort()    # [1, 2, 3, 4, 5]
print(b)
# 降序
a.sort(reverse=True)
print(a)    # ['world', 'python', 'hello', 'hello', 'HDJ', '1']

b.sort(reverse=True)
print(b)    # [5, 4, 3, 2, 1]
 #sort函数只能比较相同类型的数据
#a = [1, 2, 3, 'HDJ']
#a.sort()
#print(a)   #TypeError: '<' not supported between instances of 'str' and 'int'


#key: 排序的关键字。key 参数可以接受一个函数作为参数，该函数用于计算出每个元素排序时需要比较的值。
# 例如，对于一些包含学生信息的列表进行按年龄排序，可以通过传递一个自定义函数作为 key 参数来排序。
# 该自定义函数通过规定计算出每个学生的年龄，然后使用年龄作为排序的依据。

students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Jane', 'age': 21},
    {'name': 'John', 'age': 19},
    {'name': 'Bob', 'age': 18}
]

# 对学生列表按照年龄从小到大排序
students.sort(key=lambda x: x['age'])

# 输出排序后的学生列表
for s in students:
    print(s)
    #{'name': 'Bob', 'age': 18}
    #{'name': 'John', 'age': 19}
    #{'name': 'Tom', 'age': 20}
    #{'name': 'Jane', 'age': 21}