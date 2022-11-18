import random
import time
import pyautogui
import keyboard              
a = 0
b = 0
c = 0
ochki = 0
print("Это игра однорукий бандит! Старт через-")
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("Игра началась!")
while ochki != 10:
    a = random.randint(1,5)
    b = random.randint(1,5)
    c = random.randint(1,5)
    time.sleep(1)
    print(a,b,c)
    if (keyboard.is_pressed(" ")):
        if a == b and a==c:
            ochki = ochki + 1
        elif (a!=b or a!=c or b!=c) and ochki > 0:
            ochki = ochki - 1
        print(ochki)
        
        
        
        
