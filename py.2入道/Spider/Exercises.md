# 练手


## 获取一张图片
https://music.163.com/
```py
import requests
from fake_useragent import UserAgent

# 找到目标url
url = 'https://s7.music.126.net/static_public/6542061442ceed1ffe5c6ede_6542061442ceed1ffe5c6ee0/static/media/pc.5d0dab1a.jpg'
# 发送请求
response = requests.get(url,headers={'User-Agent': f'{UserAgent().random}'})
with open('网易云.jpg', 'wb') as file:
    file.write(response.content)
```


## 获取一首歌曲音频
https://music.163.com/
```py
import requests
from fake_useragent import UserAgent

# 找到目标url
url = 'https://m801.music.126.net/20231221180308/7a79b2a731c7ac40abe16a15066f2aac/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/32150295234/d3e3/ba8c/f2b4/279330cf738c4ebd96b2a0744db0379d.m4a'
# 发送请求
response = requests.get(url,headers={'User-Agent': f'{UserAgent().random}'})
with open('我们终将在音乐里相遇.mp3', 'wb') as file:
    file.write(response.content)
```
经实践,在media类型中找到


## 获取一个MV(视频)
https://music.163.com/
```py
import requests
from fake_useragent import UserAgent

# 找到目标url
url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/ICAwICQ4IGQgZTBjISUwJA==/mv/5902263/876008e6d30db52d965ddf9f8e16e624.mp4?wsSecret=f41ffbace2738f732efa6f0c6ee0da8b&wsTime=1703152185'
# 发送请求
response = requests.get(url,headers={'User-Agent': f'{UserAgent().random}'})
with open('在你的身边.mp4', 'wb') as file:
    file.write(response.content)
```
经实践,在fetch类型中找到


## 获取一个贴吧的单页网页内容
https://tieba.baidu.com/
```py
import requests
from fake_useragent import UserAgent

# 找到目标url
url = 'https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D'
# 发送请求
response = requests.get(url,headers={'User-Agent': f'{UserAgent().random}'})
with open('孙笑川.html', 'w', encoding='utf-8') as file:
    file.write(response.content.decode())
```
页面内容一般在第一个包;经实践,在document类型中找到


## 获取一个贴吧的多页网页内容
孙笑川吧: https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D

先观察不同页url的规律:
- 第1页: https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D&ie=utf-8&pn=0
- 第2页: https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D&ie=utf-8&pn=50
- 第3页: https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D&ie=utf-8&pn=100
- 第4页: https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D&ie=utf-8&pn=150
- 第5页: https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D&ie=utf-8&pn=200
```py
import requests
from fake_useragent import UserAgent

num = int(input('请输入要获取的页数:'))
url = 'https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D'
for i in range(num):
    headers={'User-Agent': f'{UserAgent().random}'}
    params = {
        'ie': 'utf-8', # 无关参数,若不知道其作用照抄即可
        'pn': i*50
    }
    response = requests.get(url, headers=headers, params=params)
    # 分页保存数据
    with open(f'孙笑川{i+1}.html', 'w', encoding='utf-8') as file:
        file.write(response.content.decode())
```