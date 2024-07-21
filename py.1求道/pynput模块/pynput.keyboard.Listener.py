import pynput.keyboard
import time


def main():
    while (1):
        print(1)
        time.sleep(0.5)


def key_press(key):

    if str(key) == 'Key.right':
        print("right has been pressed")
    elif str(key) == 'Key.left':
        print("left has been pressed")
    elif str(key) == 'Key.space':
        print("space has been pressed")


L = pynput.keyboard.Listener(on_press=key_press)
L.start()


if __name__ == "__main__":
    main()
