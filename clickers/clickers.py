import time
import pyautogui

from src.resnet import resnet_ark

from controllers.keyboards import press_key, press_mouse


from __init__ import keys


def clickers(inp, sanity, model):
    lv = 0

    while True:
        time.sleep(1.5)
        
        screen = pyautogui.screenshot()

        screen.save('./screen.png')

        index = resnet_ark('./screen.png', model)

        if index == 'end':
            if lv == inp:
                break 
            lv += 1
        
        if index == 'sanity':
            if sanity != 'y':
                break

        if keys['press']:
            press_key(index)
        else:
            press_mouse(index)