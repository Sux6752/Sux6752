import mylib
import random
mylib.vyvodPolya(mylib.vidimost_polya)
game = True
while game:
    stroka = int(input("Введите номер строки"))
    if stroka > 12 or stroka < 1:
        break;
    stolb = int(input("Введите номер столбца"))
    if stolb > 12 or stroka < 1:
        break;
    if vidimost_polya[stroka][stolb] == "!":
        break
    # передадим не номера строки и столбца, а индексы
    mylib.check(stroka-1,stolb-1)
    mylib.vyvodPolya(mylib.vidimost_polya)
    if mylib.isOpen():
        game = False

print("Мина! Беги беги беги! ")
#print("Всё поле открыто!")
