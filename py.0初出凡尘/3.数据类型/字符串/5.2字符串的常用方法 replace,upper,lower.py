#字符串的常用方法 replace,upper,lower
s1 = "python HDJ python"

 #replse 参数1:要替换的字符串 参数2:替换后的字符串 参数3:替换的次数(从前往后依次替换)
res = s1.replace("o", "QwQ")
print(res)                         # pythQwQn HDJ pythQwQn
res = s1.replace("o", "QwQ", 2)
print(res)                         # pythQwQn HDJ pythQwQn
res = s1.replace("o", "QwQ", 1)
print(res)                         # pythQwQn HDJ python

 #upper大写转换(整个字符串全部转换)
res2 = s1.upper()
print(res2)         # PYTHON HDJ PYTHON

 #lower小写转换
res3 = s1.lower()
print(res3)         # python hdj python
