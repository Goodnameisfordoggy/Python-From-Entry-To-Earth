#在左端用零补齐位数
st = "123"
st2 = "-1"
st3 = "G656"
print(st.zfill(5))    # '00123'
print(st2.zfill(5))   # '-0001'
print(st3.zfill(5))   # '0G656'