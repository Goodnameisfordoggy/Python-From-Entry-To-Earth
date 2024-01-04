"""
Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，
它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），
通过这个参数我们可以获取和类相关的信息并且 可以创建出类的对象 可以创建出类的对象 可以创建出类的对象!!!
"""


from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        # 使用调用构造方法返回类的实例的方式
        ctime = localtime(time())# 获取当前时间,将时间戳转换为本地时间，并以元组的形式返回年、月、日、时、分、秒、一周中的第几天、一年中的第几天、是否为夏令时等值(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()