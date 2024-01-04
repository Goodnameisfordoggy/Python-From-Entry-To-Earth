#  a      |  以追加模式打开文件,如果文件不存在则创建,文件的指针会放在文件开头;如果文件存在则在文件的末尾追加内容,文件指针在原文件末尾.
file = open('txt2.2', 'a')
file.write('python\n')#现在text2.2存在 每运行一次该程序 text2.2中的python就会增加一个
file.close()