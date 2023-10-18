import json
import win32gui
import pyautogui

from __init__ import keys


def seting():
    print('Key setting')
    print(f"Start level - {keys['main']}\nStart level 2 (team) - {keys['team']}\nEnd level - {keys['end']}\nWasting sanity - {keys['sanity'] }\nThe default window name is {keys['name']}\nUsing Auto mode - {keys['auto']}")
    print(f"Keyboard control  - {keys['press']}")
    print()
    print('Warning: if you enable auto mode it may affect your performance')
    print('If you enable auto mode, restart the application')

    inp = input('Edit? (y/n) ')

    if inp not in ['n', 'y']:
        inp = input('Edit? (y/n) ')
    
    if inp == 'y':
        keys['press'] = False if input('Do you want to disable keyboard control? (y/n) ') == 'y' else True

        if keys['press']:
            keys['main'] = input('specify a new key for Start level ')
            keys['team'] = input('specify a new key for Start Level 2 (command) ') 
            keys['end'] = input('specify a new key for End Level')
            keys['sanity'] = input('specify a new key for Spend sanity ')

        keys['name'] = input(f'specify the window name. Default{keys["name"]} ') 

        keys['auto'] = True if input(f'Do you want it on? auto mode? (y/n) ') == 'y' else False
    
        inp = input('Change settings? (y/n) ')

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
            print('There is no window with that name')
    else:
        im = pyautogui.screenshot()
        return im
    