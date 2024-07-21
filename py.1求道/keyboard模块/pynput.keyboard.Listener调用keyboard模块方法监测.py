
import keyboard
import pynput


def listening(key):
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('6'):
        print("'Ctrl+6' has been pressed")
    elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('4'):
        print("'Ctrl+4' has been pressed")
    elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('5'):
        print("'Ctrl+5' has been pressed")
    elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('1'):
        print("'Ctrl+1' has been pressed")
    elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('0'):
        print("'Ctrl+0' has been pressed")

listener = pynput.keyboard.Listener(on_press=listening)
listener.start()
listener.join()