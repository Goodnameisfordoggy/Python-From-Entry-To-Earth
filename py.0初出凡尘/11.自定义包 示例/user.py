import package1.module_A as Ma#将导入内容使用别名代替
import package1.module_B as Mb

#另一种导入写法
#from package1.module_A import a
#from package1.module_A import b

#print(module_A.a)    # NameError: name 'module_A' is not defined  QwQ:使用别名后原名称将不可用
print(Ma.a, Mb.b)    # 666 888