import random
vsego = 0
while vsego == 30 or 1:
    onek=random.randint(1,6)
    twok=random.randint(1,6)
    threek=random.randint(1,6)
    fourk=random.randint(1,6)
    fivek=random.randint(1,6)
    vsego=onek+twok+threek+fourk+fivek
    print(onek,twok,threek,fourk,fivek)
    if vsego == 30:
        print("У вас все по 6.")
        break
    elif vsego == 6:
        print("Вы проиграли.")
        break