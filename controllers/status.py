import pyautogui

import numpy as np


def click_end_status():
    myScreenshot = np.array(pyautogui.screenshot())

    pyautogui.moveTo(2102/2560*myScreenshot.shape[1], 652/1440*myScreenshot.shape[0])
    pyautogui.click()

def click_main_status():
    myScreenshot = np.array(pyautogui.screenshot())

    pyautogui.moveTo(2110/2560*myScreenshot.shape[1], 1250/1440*myScreenshot.shape[0])
    pyautogui.click()

def click_team_status():
    myScreenshot = np.array(pyautogui.screenshot())

    pyautogui.moveTo(2110/2560*myScreenshot.shape[1], 1218/1440*myScreenshot.shape[0])
    pyautogui.click()

def click_sanity_status():
    myScreenshot = np.array(pyautogui.screenshot())

    pyautogui.moveTo(2050/2560*myScreenshot.shape[1], 1100/1440*myScreenshot.shape[0])
    pyautogui.click()