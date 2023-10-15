import time

from src.resnet import resnet_ark

from controllers.keyboards import press_key
from controllers.setings import screenshot

from __init__ import keys


def clickers(inp, sanity, model):
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