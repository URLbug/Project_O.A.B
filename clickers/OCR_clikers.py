import time

from src.OCR import OCR_sanity
from src.resnet import resnet_ark

from controllers.keyboards import press_key, press_mouse
from controllers.setings import screenshot

from __init__ import keys


def ocr_inp():
    try:
        screen = screenshot(keys['name'])
    except:
        print('У вас неверное имя окна')
        break

    screen.save('./screen.png')

    san, rep = OCR_sanity('./screen.png')

    inp = san // (rep*-1)

    print(f"Уровень автоматически пройдется {inp}")

    return inp


def auto_lv(sanity, model):
    ocr = True
    lv = 0

    inp = ocr_inp()

    while True:
        time.sleep(1)
        
        try:
            screen = screenshot(keys['name'])
        except:
            print('У вас неверное имя окна')
            break

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