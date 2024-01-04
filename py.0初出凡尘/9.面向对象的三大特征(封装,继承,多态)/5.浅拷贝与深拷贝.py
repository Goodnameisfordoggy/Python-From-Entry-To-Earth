
class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


#赋值操作 
    #只是形成两个变量,实际上还是指向同一个对象
cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))    # <__main__.CPU object at 0x010694B0> 17208496
print(cpu2, id(cpu2))    # <__main__.CPU object at 0x010694B0> 17208496
print("========================================================================")

#浅拷贝:
    #Python的拷贝一般都是浅拷贝,拷贝时,对象包含的子对象内容不拷贝,
    #因此,源对象与拷贝对象会引用同一个子对象
import copy
disk1 = Disk()
computer = Computer(cpu1, disk1)
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)    #<__main__.Computer object at 0x01B2F310> <__main__.CPU object at 0x01669470> <__main__.Disk object at 0x01B2F250>
print(computer2, computer2.cpu, computer2.disk) #<__main__.Computer object at 0x01B2F310> <__main__.CPU object at 0x01669470> <__main__.Disk object at 0x01B2F250>
print("=============================================================================")

#深拷贝:
    #使用copy模块的deepcopy函数,递归拷贝对象中包含的子对象
    #源对象和拷贝对象以及两者所有的子对象也不相同
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)      # <__main__.Computer object at 0x0152F310> <__main__.CPU object at 0x010694B0> <__main__.Disk object at 0x0152F350>
print(computer3, computer3.cpu, computer3.disk)   # <__main__.Computer object at 0x0152F7B0> <__main__.CPU object at 0x0153AAF0> <__main__.Disk object at 0x015430D0>
