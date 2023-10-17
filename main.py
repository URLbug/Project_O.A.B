import time
import os
import pyautogui

import tensorflow as tf


from __init__ import keys

from src.layers import Residual

from controllers.setings import seting, screenshot

if keys['auto']:
    from clickers.OCR_clikers import auto_lv 

from clickers.clickers import clickers
from src.OCR import OCR_sanity


def main():
    model = tf.keras.models.load_model('./model/beta_resnet.h5', custom_objects={'Residual': Residual})

    while True:
        os.system('cls')

        print('Настройка - 1\nСтарт - 2\nВыйти - 3')
        
        inp = input('-> ')

        if inp not in ['1', '2', '3']:
            inp = input('-> ')
        elif inp == '1':
            os.system('cls')

            seting()
        elif inp == '2':
            os.system('cls')

            if keys['auto']:
                print('Напишите англискую "a" если хотите пройти уровень автоматически')

            inp = input('Сколько раз вы хотите пройти уровень? Либо автоматически пройти уровень? ')

            sanity = input('Тратить sanity? (y/n) ')

            if inp == "a" and keys['auto']:
                auto_lv(sanity, model)
            else:
                try:
                    inp = int(inp)
                except:
                    print('Вы указали не число. Поэтому цикл всего будет 1')

                    inp = 1
            
            clickers(inp, sanity, model)
        else:
            exit()

if __name__ == '__main__':
    main()