#字符串在给定的宽度内居中显示
st = "123"
a = 10
print(st.center(a))    # '   123    '
print(st.center(a, '*'))    # ***123****
print(len(st.center(a)))    # 10