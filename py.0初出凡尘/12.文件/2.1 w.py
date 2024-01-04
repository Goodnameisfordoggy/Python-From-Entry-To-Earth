# w      |  以只写模式打开文件,如果文件不存在则创建,如果文件存在则覆盖原有内容,文件的指针会放在文件开头.
file = open('txt2.1', 'w')
file.write('python')#改变此处字符串 text2.1中的内容会发生相应变化
#print(file.readline())    # io.UnsupportedOperation: not readable  QwQ:该模式下不可读,所以不能输出
file.close()