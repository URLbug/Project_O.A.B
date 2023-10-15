import pyautogui
import time
import os
import json
import win32gui

import tensorflow as tf

from pynput.keyboard import Controller

from src.resnet import resnet_ark
from src.layers import Residual
from __init__ import dirs, keys

if keys['auto']:
    from src.OCR import OCR_sanity


def press_key(index):
    keyboard = Controller()

    if keys[index] != None:
        keyboard.press(keys[index])
        keyboard.release(keys[index])

def screenshot(window_title=None):
    if window_title:
        title_exists = win32gui.FindWindow(None, window_title)
        
        if title_exists:
            win32gui.SetForegroundWindow(title_exists)
            
            x, y, x1, y1 = win32gui.GetClientRect(title_exists)
            
            x, y = win32gui.ClientToScreen(title_exists, (x, y))
            
            x1, y1 = win32gui.ClientToScreen(title_exists, (x1 - x, y1 - y))
            
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            
            return im
        else:
            print('Не существует окна с таким именем')
    else:
        im = pyautogui.screenshot()
        return im

def seting():
    print('Настройка клавишь')
    print(f"Начать уровень - {keys['main']}\nНачать уровень 2 (команда) - {keys['team']}\nЗакончить уровень - {keys['end']}\nТрата sanity - {keys['sanity']}\nНазвание окна по умолчанию - BlueStacks App Player 1\nИспользование Auto режима - {keys['auto']}")
    print('Предупреждение если вы вкл. auto режим то это может повлиять на вашу производительность')
    print('Если вы вкл. auto режим то перезагрузите приложение')

    inp = input('Редактироваь? (y/n) ')

    if inp not in ['n', 'y']:
        inp = input('Редактироваь? (y/n) ')
    
    if inp == 'y':
        keys['main'] = input('укажите новую клавишу для Начать уровень ')
        keys['team'] = input('укажите новую клавишу для Начать уровень 2 (команда) ') 
        keys['end'] = input('укажите новую клавишу для Закончить уровень ')
        keys['sanity'] = input('укажите новую клавишу для Трата sanity ')

        keys['name'] = input(f'укажите имя окна. По умолчанию {keys["name"]} ') 

        keys['auto'] = True if input(f'Хотите вкл. auto режим? (y/n) ') == 'y' else False
    
        inp = input('Изменить настройки? (y/n) ')

        if inp == 'y':
            with open('./keyboards.json', 'w') as jsons:
                json.dump(keys, jsons)

def auto_lv(sanity, model):
    ocr = True
    lv = 0

    while True:
        time.sleep(5)
        
        try:
            screen = screenshot(keys['name'])
        except:
            print('У вас неверное имя окна')
            break

        screen.save('./screen.png')

        if ocr:
            san, rep = OCR_sanity('./screen.png')

            inp = san // (rep*-1)

            ocr = False

            print(f"Уровень автоматически пройдется {inp}")
            print(f"Подождите 60 сек. до запуска уровня")

            time.sleep(60)

        index = resnet_ark('./screen.png', model)

        if index == 'main':
            if lv == inp:
                break    
            lv += 1
        
        if index == 'sanity' and sanity != 'y':
            break
        
        if index == 'sanity':
            ocr = True
        
        press_key(index)

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

            lv = 0

            while True:
                time.sleep(5)
                
                try:
                    screen = screenshot(keys['name'])
                except:
                    print('У вас неверное имя окна')
                    break

                screen.save('./screen.png')

                index = resnet_ark('./screen.png', model)

                if index == 'main':
                    if lv == inp:
                        break    
                    lv += 1
                
                if index == 'sanity' and sanity != 'y':
                    break
                
                press_key(index)
        else:
            exit()

if __name__ == '__main__':
    main()
