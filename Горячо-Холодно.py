import random
a=random.randint(1,9)
b=random.randint(1,9)
c=random.randint(1,9)
if a == b:
    a=random.randint(1,9)
if a == c:
    a=random.randint(1,9)
if b==a:
    b=random.randint(1,9)
if b==c:
    b=random.randint(1,9)
if c==a:
    c=random.randint(1,9)
if c == b:
    c=random.randint(1,9)
def kapibara(a,b,c,otva,otvb,otvc):
    if a != otva and b != otvb and c != otvc:
        print("Холодно")
    if a == otvb or a == otvc or b == otva or b == otvc or c == otva or c == otvb:
        print("Тепло")
    if a == otva and b == otvb and c == otvc:
        print("Вы Выиграли")
while a != otva and b != otvb and c != otvc:
    kapibara(a,b,c,otva,otvb,otvc)
    otva=int(input("Первое число -- "))
    otvb=int(input("Второе число -- "))
    otvc=int(input("Третье число -- "))

                