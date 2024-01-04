#字符串的格式化 与.format与{}配合使用
print("大家好,我的名字叫Goodnameisfordoggy,今年18岁,性别男")
s2 = "大家好,我的名字叫{},今年{}岁,性别{}".format("Goodnameisfordoggy", "18", "男")
print(s2)                                                        # 大家好,我的名字叫Goodnameisfordoggy,今年18岁,性别男
s3 = "大家好,我的名字叫{},今年{}岁,性别{}"
print(s3.format("Goodnameisfordoggy", "18", "男"))                              # 大家好,我的名字叫Goodnameisfordoggy,今年18岁,性别男
 #.format中的字符串可使用下标
s3 = "大家好,我的名字叫{1},今年{2}岁,性别{0}"
print(s3.format("Goodnameisfordoggy", "18", "男"))                              # 大家好,我的名字叫18,今年男岁,性别Goodnameisfordoggy