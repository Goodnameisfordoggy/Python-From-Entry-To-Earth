import pynput.keyboard
from pynput.keyboard import Key, Controller
"""
总结一下,大键盘上的数字,字母,符号(识别按照下方小写字符)用key.char,
        其余用str(key),
"""


def key_press(key):

    print(key)
    # print(type(key))
    print(str(key))
    #print(key.char)

    if key == Key.ctrl:
        print("True")

# 写法一
# L = pynput.keyboard.Listener(on_press=key_press)
# L.start()
# L.join()


# 写法二
with pynput.keyboard.Listener(on_press=key_press) as listener:
    listener.join()

#4101
