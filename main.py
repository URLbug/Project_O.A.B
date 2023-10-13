import pyautogui
import time
import os

import tensorflow as tf

from pynput.keyboard import Controller

from src.resnet import resnet_ark, evalute, Residual
from __init__ import dirs, keys


def press_key(index):
    keyboard = Controller()

    if keys[index] != None:
        keyboard.press(keys[index])
        keyboard.release(keys[index])

def main():
    model = tf.keras.models.load_model('./model/beta_resnet.h5', custom_objects={'Residual': Residual})
    
    inp = int(input('Сколько раз вы хотите пройти уровень? - '))

    lv = 0

    while True:
        time.sleep(5)
        pyautogui.screenshot('./screen.png')

        index = resnet_ark('./screen.png', model)
        
        press_key(index)

        if index == 'main':
            lv += 1

            if lv == inp:
                break

if __name__ == '__main__':
    main()
