import json
import win32gui
import pyautogui
import ctypes

from __init__ import keys


def seting():
    print('Настройка клавишь')
    print(f"Начать уровень - {keys['main']}\nНачать уровень 2 (команда) - {keys['team']}\nЗакончить уровень - {keys['end']}\nТрата sanity - {keys['sanity']}\nНазвание окна по умолчанию - BlueStacks App Player 1\nИспользование Auto режима - {keys['auto']}")
    print(f"Управление клавиатурой  - {keys['press']}")
    print()
    print('Предупреждение если вы вкл. auto режим то это может повлиять на вашу производительность')
    print('Если вы вкл. auto режим то перезагрузите приложение')

    inp = input('Редактироваь? (y/n) ')

    if inp not in ['n', 'y']:
        inp = input('Редактироваь? (y/n) ')
    
    if inp == 'y':
        keys['press'] = False if input('Вы хотите отключить управление клавиатурой? (y/n) ') == 'y' else True

        if keys['press']:
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
    

def windows():
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    titles = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)
