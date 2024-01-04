#用于清除字符(无参数 默认添加空格为参数)
st = "   123   "
st2 = "***123****"
print(st.strip())    # '123'
print(st.rstrip())   # '   123'
print(st2.lstrip('*'))   # '123****'

#去除时与顺序无关 (可以认为与参数互为镜像的字符串也将被去除)
st3 = "lpb-python-bpl"
print(st3.strip("bpl"))    # -python-