# b      |  以二进制形式打开文件,不能单独使用,需要与其他模式一起使用 如: rb, wb
src_file = open('xp.jpg', 'rb')#在执行程序前存在xp.jpg文件 所以打开该文件

target_file = open('copy_xp.png', 'wb')#在执行程序前无copy_xp.png文件 所以创建copy_xp.png文件  QwQ:这样可以实现简单的文件格式转换

target_file.write(src_file.read())

src_file.close()
target_file.close()