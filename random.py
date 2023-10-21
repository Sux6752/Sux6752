import random
import time
 
a=random.randint(3)
b=random.randint(0,5)
print("Через"+a+"времени появится число от 0 до 5")
time.wait(a)
print(b)