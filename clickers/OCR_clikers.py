import time
import pyautogui

from src.OCR import OCR_sanity
from src.resnet import resnet_ark

from controllers.keyboards import press_key, press_mouse
from controllers.setings import screenshot

from __init__ import keys


def ocr_inp():
    try:
        screen = screenshot(keys['name'])
    except:
        print('Your window name is incorrect')
        return 1

    screen.save('./screen.png')

    san, rep = OCR_sanity('./screen.png')

    inp = san // (rep*-1)

    print(f"The level will be completed automatically {inp}")

    return inp


def auto_lv(sanity, model):
    ocr = False
    lv = 0

    inp = ocr_inp()

    while True:
        time.sleep(1)
        
        screen = pyautogui.screenshot()

        screen.save('./screen.png')

        if ocr:
            inp = ocr_inp()

            ocr = False

        index = resnet_ark('./screen.png', model)

        if index == 'main':
            if lv == inp:
                break    
            lv += 1
        
        if index == 'sanity' and sanity != 'y':
            break
        
        if index == 'sanity' and sanity == 'y':
            ocr = True
        
        if keys['press']:
            press_key(index)
        else:
            press_mouse(index)