#用于空格补齐位数(若原字符串位数与参数规定的位数一致,不做变动)
st = "123"
print(st.rjust(5))  # '  123'
print(st.ljust(5))  # '123  '
st2 = "12_3_"
print(st2.rjust(5)) # '12_3_'
#just 并不存在
#print(st.just(5))  AttributeError: 'str' object has no attribute 'just'