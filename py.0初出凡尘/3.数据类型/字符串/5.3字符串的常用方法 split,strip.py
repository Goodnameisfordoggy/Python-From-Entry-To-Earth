#字符串的常用方法 split,strip

s1 = "111ab222ab333ab444"
 #用split将字符串用规定的字符"a"进行分割,得到一个列表
print(s1.split('a'))                     # ['111', 'b222', 'b333', 'b444']
  #参数1:用于分割的字符 参数2:分割的次数
print(s1.split('a', 2))                  # ['111', 'b222', 'b333ab444']

 #strip
  #去除字符串首尾的空格(此格式仅能去除首尾空格)
s2 = "   HDJ  666   "
print(s2.strip())                        # HDJ  666
s2 = "   HDJ   6 6 6"
print(s2.strip())                        # HDJ   6 6 6
   #去除全部空格
s2 = "   HDJ   6 6 6"
print(s2.replace(' ', ''))               # HDJ666
  #去除首尾的666
s3 = "666HDJ666"
print(s3.strip('6'))                     # HDJ