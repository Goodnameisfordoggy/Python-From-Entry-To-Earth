#传统的格式化输出 & F表达式

 #%S为(任意类型)字符站位
s1 = "我%s你"
print(s1 % "爱")                          # 我爱你

 #%d为数值(整数)类型站位
s2 = "我的成绩是%d" % 100
print(s2)                                 # 我的成绩是100
s2 = "我的成绩是%d" % 99.99
print(s2)                                 # 我的成绩是99

 #%f为浮点数类型站位
s3 = "我的成绩是%f" % 99.99
print(s3)                                 # 我的成绩是99.990000
s3 = "我的成绩是%.2f" % 99.99
print(s3)                                 # 我的成绩是99.99

 #F表达式(python3.6以上支持)
name = "Goodnameisfordoggy"
age = "18"
s4 = "我的名字叫{},我的年龄是{}"
print(s4.format(name, age))               # 我的名字叫Goodnameisfordoggy,我的年龄是18
s5 = F"我的名字叫{name},我的年龄是{age}"
print(s5)                                 # 我的名字叫Goodnameisfordoggy,我的年龄是18
