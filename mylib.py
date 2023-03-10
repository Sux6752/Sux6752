import random
pole = [["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","#","#","#","#","#"],
        ["*","*","*","#","#","#","#","#","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["#","#","#","#","*","*","*","*","*","#","#","#"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"]]
vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"]]
pov=0
k=0
i=0
j=0
while pov != 3:
    mx=random.randint(1,11)
    my=random.randint(1,11)
    pole[mx][my]="!"
    pov=pov+1
    def minaproverka(vidimost_polya,i,j,k):
        if pole[i][j] == "*" and pole[i+1][j] == "*" and pole[i-1][j] == "*" and pole[i][j+1] == "*" and pole[i][j-1] == "*" and pole[i1][j+1] == "*" and pole[i-1][j-1] == "*" and pole[i-1][j+1] == "*" and pole[i+1][j-1] == "*":
            return "*"
        else:
            if i == 0:
                for l in range(1,11):
                    if vidimost_polya[i+l][j] == "!":
                        k=k+1
                        vidimost_polya[i+l][j]==k
                        return
                    else:
                        return "*"
            elif i == 0 and j >= 0:
                for l in range(1,11):
                    if vidimost_polya[i+l][j] == "!":
                        k=k+1
                        vidimost_polya[i+l][j]==k
                        return k
                    if vidimost_polya[i+l][j-1] == "!":
                        k=k+1
                        vidimost_polya[i+l][j-1]==k
                        return k
                    else:
                        return "*"
                    if vidimost_polya[i][j-1] == "!":
                        k=k+1
                        vidimost_polya[i][j-1]==k
                        return k
                    else:
                        return "*"
            elif i >= 0 and j >= 0:
                for l in range(1,11):
                    if vidimost_polya[i+l][j] == "!":
                        k=k+1
                        vidimost_polya[i+l][j]==k
                        return k
                    if vidimost_polya[i+l][j-1] == "!":
                        k=k+1
                        vidimost_polya[i+l][j-1]==k
                        return k
                    else:
                        return "*"
                    if vidimost_polya[i][j-1] == "!":
                        k=k+1
                        vidimost_polya[i][j-1]==k
                        return k
                    else:
                        return "*"
                    if vidimost_polya[i+1][j+1] == "!":
                        k=k+1
                        vidimost_polya[i+1][j+1]==k
                        return k
                    else:
                        return "*"
                    if vidimost_polya[i-1][j+1] == "!":
                        k=k+1
                        vidimost_polya[i-1][j+1]==k
                        return k
                    else:
                        return "*"
                    if vidimost_polya[i-1][j-1] == "!":
                        k=k+1
                        vidimost_polya[i-1][j-1]==k
                        return k
                    else:
                        return "*"
        minaproverka(vidimost_polya,i,j,k)
# проверка поля на то, что внутри него
# если поле пустое, проверяются все клетки вокруг него
# если стена — не проверяются
# если поле уже было открыто — оно не проверяется

def check(stroka,stolb):
    # если клетка ещё не открыта
    if vidimost_polya[stroka][stolb] == "•":
        # открываем
        vidimost_polya[stroka][stolb] = pole[stroka][stolb]
        # если оно оказалось пустым
        if pole[stroka][stolb] == "*":
            # проверяем все соседние, только если они существуют
            # а то выйдем за пределы поля, Python ругать будет
            if stroka-1 >= 0:
                check(stroka-1,stolb)
                if stolb-1 >= 0:
                    check(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka-1,stolb+1)
                    
            if stroka+1 < len(pole):
                check(stroka+1,stolb)
                if stolb-1 >= 0:
                    check(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka+1,stolb+1)
                    
            if stolb-1 >= 0:
                    check(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                check(stroka,stolb+1)
def isOpen():
    # считаем, что поле открыто всё
    opened = True
    #для каждой строки в видимости поля
    for stroka in vidimost_polya:
        # если хотя бы в одной нашлось закрытое поле
        if "•" in stroka:
            # значит неправда, поле ещё не всё открыто
            opened = False
    return opened

def vyvodPolya(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end='')
        print()