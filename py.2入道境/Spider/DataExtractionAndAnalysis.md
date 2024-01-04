# 数据类型

## 文本数据类型
xml: 可扩展标记语言,更专注于数据的传输和储存,侧重点事数据内容.
html: 超文本标记语言,更专注于显示数据,侧重点是显示.

结构化响应内容:
json字符串: 可以使用re/json模块来获取特定数据.
xml字符串: 可以使用re/lxml来提取特定的数据.

非结构化相应内容:
html字符串: 可以使用re/lxml来提取特定的数据.

# json模块

## dumps()
将python数据转化为json字符串
```py
import json

dic = {'name': '张三丰'}
print(type(dic)) # <class 'dict'>
dic1 = json.dumps(dic)
print(type(dic1)) # <class 'str'> # 数据转化为json字符串
print(dic1) # {"name": "\u5f20\u4e09\u4e30"} # json字符串必须是用双引号引起来的
dic2 = json.dumps(dic, ensure_ascii=False) # 数据有中文,不使用ascll编码解析
print(dic2) # {"name": "张三丰"}
```

## loads()
将json字符串转化为python数据
```py
import json

dic = {"name": "张三丰"}
dic1 = json.dumps(dic)
print(type(dic1)) # <class 'str'>
dic2 = json.loads(dic1)
print(type(dic2)) # <class 'dict'>
print(dic2) # {'name': '张三丰'}
```

# jsonpath模块