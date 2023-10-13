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

def seting():
    print('Настройка клавишь')
    print(f"Начать уровень - {keys['main']}\nНачать уровень 2 (команда) - {keys['team']}\nЗакончить уровень - {keys['end']}")

    inp = input('Редактироваь? (y/n) ')

    if inp not in ['n', 'y']:
        inp = input('Редактироваь? (y/n) ')
    
    if inp == 'y':
        keys['main'] = input('укажите новую клавишу для Начать уровень ')
        keys['team'] = input('укажите новую клавишу для Начать уровень 2 (команда) ') 
        keys['end'] = input('укажите новую клавишу для Закончить уровень ') 



def main():
    model = tf.keras.models.load_model('./model/beta_resnet.h5', custom_objects={'Residual': Residual})
    
    while True:
        print('Настройка - 1\nСтарт - 2\nВыйти - 3')
        
        inp = input('-> ')

        if inp not in ['1', '2', '3']:
            inp = input('-> ')
        elif inp == '1':
            seting()
        elif inp == '2':
            inp = int(input('Сколько раз вы хотите пройти уровень? '))

            lv = 0

            while True:
                time.sleep(5)
                pyautogui.screenshot('./screen.png')

                index = resnet_ark('./screen.png', model)
                
                press_key(index)

                if index == 'main':
                    if lv == inp:
                        break
                    
                    lv += 1
        else:
            exit()

if __name__ == '__main__':
    main()
