"""
with语句(上下文管理器)
    with语句可以自动管理上下文资源,不论什么原因(包括但不限于语法出错)跳出with都能确保文件正确的关闭,以此来达到释放资源的目的
"""


#MyContentMgr实现了特殊方法__enter__(), __exit__(),故该类对象遵守了上下文管理器协议,该类对象的实例对象称为上下文管理器
class MyContentMgr (object):
    def __enter__(self):
        print("enter方法被调用执行了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被调用执行了")

    def show(self):
        print("show方法被调用执行了")


with MyContentMgr() as file:
    file.show()    # enter方法被调用执行了
                   # show方法被调用执行了
                   # exit方法被调用执行了
