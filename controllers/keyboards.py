from pynput.keyboard import Controller

from __init__ import keys


def press_key(index):
    keyboard = Controller()

    if keys[index] != None:
        keyboard.press(keys[index])
        keyboard.release(keys[index])
