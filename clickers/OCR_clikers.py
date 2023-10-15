import time

from src.OCR import OCR_sanity
from src.resnet import resnet_ark

from controllers.keyboards import press_key
from controllers.setings import screenshot

from __init__ import keys


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

            inp = san // rep

            ocr = False

            print(f"Уровень автоматически пройдется {inp}")

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