# 背景知识

## 浏览器发送请求原理
浏览器会向服务器发送请求行,包括请求方法,url,http协议.
1. 构建请求
2. 查找缓存
3. 准备ip地址和端口
4. 等待tcp队列
5. 建立tcp队列
6. 发送http请求

## 请求方法
1. GET
   - 直接向服务器发送请求,获取响应内容.
   - 安全性较低: 关键字直接在地址栏上显示,
   - 效率高
```py
import requests

requests.get(url)
```
2. POST
   - 先给服务器数据,再获取响应内容
   - 安全性较高: 一般用于有登录注册 需求时,
   - 效率低
```py
import requests

requests.post(url, date)
```

## 请求结果的常用属性
- response.url 有的时候响应的url和请求的url不一致
- response.status_code 响应状态码
- response.request.headers 响应对应的请求头
- response.headers 响应头
- response.request._cookies 响应对应的请求的cookie;返回cookiejar类型
- response.cookie 响应的cookie(经过set-cookie动作,返回cookiejar类型)
- response.encoding 响应的编码格式

## Url的转换码
Url 转换为 str 时会被编码
```py
from urllib.parse import quote, unquote
s = '参数'
print(quote(s)) # %E5%8F%82%E6%95%B0
print(unquote(quote(s))) # 参数
```

## 代理(ip)
ip地址: 精确的定位

#### 正向与反向
- 正向代理: 给客户端做代理,让服务器不知道客户端的真实身份;保护自己的ip地址不会被封;
- 反向代理: 给服务器做代理,让浏览器不知道服务器的真实地址;保护服务器不被攻击;

#### 实际理论
- 透明代理: 服务器能够检测到用户使用了代理,并且知道用户的真实ip地址.
- 匿名代理: 服务器能够检测到用户使用了代理,但不知道用户的真实ip地址.
- 高匿代理: 服务器既不能检测到用户使用了代理,也不知道用户的真实ip地址.

# requests模块

## get()

#### url

#### headers

##### User-Agent
用户代理 
1. User-Agent的使用: \
爬取到的内容不全,与直接浏览网页时的信息不符,要进行简单的伪装

```py
import requests

# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 模拟浏览器发送请求
response = requests.get('https://www.baidu.com/' , headers=headers)
# print(response.content.decode())
print(len(response.content.decode()))
print(response.request.headers)
```

2. User-Agent池的使用
单一的User-Agent很可能被服务器检测出来 \
(1).自己手搓池子:
```py
import requests
import random

UA_list = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
]
response = requests.get(
    'https://www.baidu.com/' , 
    headers={'User-Agent': f'{random.choice(UA_list)}'}
)
# print(response.content.decode())
print(len(response.content.decode()))
print(response.request.headers)
```

(2).使用fake_useragent库
```py
from fake_useragent import UserAgent
import requests

response = requests.get(
    'https://www.baidu.com/' , 
    headers={'User-Agent': f'{UserAgent().random}'}
)
# print(response.content.decode())
print(len(response.content.decode()))
print(response.request.headers)
```

##### cookie
用于获取登录后的页面数据,实现模拟登录 \
cookie的数据放在用户的浏览器上,容易从本地数据中获取,安全性较低;从安全性考虑,建议用session. 
1. 简单示例
```py

import requests
from fake_useragent import UserAgent

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie': '登录后获取到的cookie'
}
response = requests.get(url, headers=headers)
```
2. cookie池
类似于User-Agent池.\
一个账号进行大量的请求会被服务器认定为爬虫;cookie池中,每一个cookie就是一个账号.


#### params 
url参数传递

1. 直接在url上格式化字符串
```py
import requests

key_world = input('请输入查找关键字:')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
response = requests.get(f'https://www.baidu.com/s?wd={key_world}', headers=headers)
print(response.content.decode())
```

2. 通过get的params参数
```py
import requests

key_world = input('请输入查找关键字:')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# params的参数字典
kw = {'wd': key_world}
response = requests.get('https://www.baidu.com/s?', headers=headers, params=kw)
print(response.content.decode())
```

#### proxies(代理参数)

##### proxies数据格式
```py
import requests

url = 'https://www.baidu.com/'
proxies = {
    # 写法1:
    'http': '12.34.56.78:9527', # (非加密)
    'https': '12.34.56.78:9527', # (加密)
    # 写法2:
    'http': 'http://12.34.56.78:9527', # (非加密)
    'https': 'https://12.34.56.78:9527', # (加密)
}
response = requests.get(url, proxies=proxies)
```

##### 检测代理ip是否可用
使用ip138平台: https://2023.ip138.com/
如果ip可用会显示ip地址,不可用会返回异常.
```py
import requests
from fake_useragent import UserAgent

url = 'https://2023.ip138.com/'
headers = {
    'User-Agent': f'{UserAgent().random}'
}
proxies = {
    'your_key': 'your_value'
}
response = requests.get(url, headers=headers, proxies=proxies)
print(response.content.decode())
```

#### timeout
用于设置超时时间,发送请求后,规定时间内未响应,抛出异常requests.exceptions.ReadTimeout
```py
import requests
from fake_useragent import UserAgent
from retrying import retry

url = 'https://www.baiduss.com/'
headers = {'User-Agent': f'{UserAgent().random}'}
response = requests.get(url, headers=headers, timeout=3) # 设置超时时间为两秒 
print(response.content.decode())


```

## post()
需要先传入数据form_data
```py
import requests
from fake_useragent import UserAgent

url = 'https://www.iciba.com/translate'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
form_data = {
    'from': 'zh',
    'to': 'en',
    'q': '你好'
}
response = requests.post(url, headers=headers, data=form_data)
print(response.text)
```

## session
用于获取登录后的页面数据,实现模拟登录 \
session的数据会保存在服务器上一段时间;从减轻服务器压力考虑,建议用cookie.
```py
# 创建session实例
session = requests.session()
response = session.post(url, data=data)
# 模拟登录,请求数据
session.get(url.text)
```

# response
响应结果的输出有两种形式:文本,二进制.

## response.text
```py
import requests

# 找到目标url
url = 'https://news.baidu.com/'
# 发送请求
response = requests.get(url)
print(response)
# 打印响应内容
print(response.text) # 可能会有乱码,request自动推测解码方式,可自行设置编码  response.encoding = 'utf-8'
```

## response.content
二进制文件的保存
图片,音频,视频等
```py
import requests

url = 'https://p8.itc.cn/q_70/images01/20230614/c605f48d3df64450bdbe65d0c4c7d03f.jpeg'
response = requests.get(url)
# 图片二进制文件
print(response.content)
# 二进制文件写入用'wb'
with open('2.jpeg', 'wb') as file:
    file.write(response.content)
```

#### decode()
文件解码保存;通常用于网页结构信息的文件,html,css,json等
```py
import requests

# 找到目标url
'https://www.baidu.com/'# 发送请求
response = requests.get(url)
with open('baidu首页.html', 'w', encoding='utf-8') as file:
    file.write(response.content.decode())
```

# retrying模块

## 简介
```py
from retrying import retry

@retry(stop_max_attempt_number=3, wait_fixed=1000)
def do_something():
    # 在这个函数里执行可能会失败的操作
    # 如果出现指定的异常，retry装饰器会根据设置自动重试
    # 在这个例子中，最多重试3次，每次重试之间间隔1秒
    # 如果连续重试3次后仍然失败，则会抛出原始的异常
    pass
```

## 简单示例
```py
import requests
from fake_useragent import UserAgent
from retrying import retry

url = 'https://www.baidu.com/'
headers = {'User-Agent': f'{UserAgent().random}'}

@retry(stop_max_attempt_number=3, wait_fixed=1000)
def do_something():
    print(1)
    response = requests.get(url, headers=headers) # reraise=True 即使在 do_something() 中的重试失败  ，异常也会传播
    print(response.content.decode())

if __name__ == '__main__':
    try:    
        do_something()
    except:
        print("finish")
```