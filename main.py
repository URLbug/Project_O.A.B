import os
import keyboard

import tensorflow as tf


from __init__ import keys

from src.layers import Residual

from controllers.setings import seting

if keys['auto']:
    from clickers.OCR_clikers import auto_lv

from clickers.clickers import clickers


def main():
    model = tf.keras.models.load_model('./model/beta_resnet.h5', custom_objects={'Residual': Residual})

    while True:
        os.system('cls')

        print('Settings - 1\nStart - 2\nExit - 3')
        
        inp = input('-> ')

        if inp not in ['1', '2', '3']:
            inp = input('-> ')
        elif inp == '1':
            os.system('cls')

            seting()
        elif inp == '2':
            os.system('cls')

            if keys['auto']:
                print('Write English "a" if you want to pass the level automatically')

            inp = input('How many times do you want to complete the level? Or automatically complete the level? ')

            sanity = input('Spending sanity? (y/n) ')

            if inp == "a" and keys['auto']:
                auto_lv(sanity, model)
            else:
                try:
                    inp = int(inp)
                except:
                    print("You didn't specify a number. Therefore the cycle will be 1")

                    inp = 1
            
            clickers(inp, sanity, model)
        else:
            exit()

if __name__ == '__main__':
    main()
