from pynput.keyboard import Controller

from __init__ import keys

from controllers.status import click_main_status, click_team_status, click_end_status, click_sanity_status


def press_key(index):
    keyboard = Controller()

    if keys[index] != None:
        keyboard.press(keys[index])
        keyboard.release(keys[index])

def press_mouse(index):
    if index == 'main':
        click_main_status() 
    elif index == 'team':
        click_team_status()
    elif index == 'sanity':
        click_sanity_status()
    else:
        click_end_status()
