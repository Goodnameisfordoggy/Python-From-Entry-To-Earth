"""
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，
不同的子类对象会表现出不同的行为，这个就是多态
"""


from abc import ABCMeta, abstractmethod

"""
我们将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。
Python从语法层面并没有像Java或C#那样提供对抽象类的支持，但是我们可以通过 abc模块 的 ABCMeta元类 和 abstractmethod包装器 来达到抽象类的效果，
如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。
下面的代码中，Dog和Cat两个子类分别对Pet类中的make_voice抽象方法进行了重写并给出了不同的实现版本，
当我们在main函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。

abstractmethod 是在抽象类中定义抽象方法的一个装饰器，它用于声明一个方法是抽象方法，即这个方法没有具体的实现，只有定义。
抽象方法可以被子类继承并实现，强制规范了子类的方法实现，提高了程序的健壮性和可读性, 是一种很好的设计模式。
"""


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


class Xingxing(Pet):
    """猩猩"""
    def make_voice(self):#子类中继承抽象类中的抽象方法可以继续抽象着,但必须写出来!
        pass


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄'), Xingxing('狒狒')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()