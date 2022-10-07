'''
Этот проект на pyautogui должен запускать блокнот
Но почему-то код выдаёт ошибку
'''
import pyautogui
import time
pyautogui.press('win')
time.sleep(1)
pyautogui.write('notepad')
time.sleep(1)
pyautogui.press('enter')