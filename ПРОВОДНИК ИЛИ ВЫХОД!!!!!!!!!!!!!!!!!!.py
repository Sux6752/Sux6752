import pyautogui
import time
atvet=input("проводник или выход поиск")
if atvet=="Выход":
    exit
elif atvet=="Проводник":
    pyautogui.moveTo(165,767)
    pyautogui.click()
else:
    print("Неизвестная команда")