print("Это игра квест! Пишите все с большой буквы")
print("Предистория: Вы живёте в деревне где недавно пропал десяти летний мальчик. Вы решили исследовать это дело. Ваша имя Александр(а) возраст 12 лет родились в 1987 году всё происходит в 1997 году")
a=input("Вы находитесь в лесу. Вы видете варежку, но какой-то силуэт находится за деревом: Взять, окликнуть силуэт или бежать?\n")
while a != "Взять" and a != "окликнуть силуэт" and a != "Бежать":
    a = input("выберите: Взять, окликнуть силуэт или Бежать:\n")
if a == "Взять":
    print("Вы взяли варежку")
    print("За деревом вы услышали шорох.")
    a = input("У вас есть выбор: Бежать или ждать?\n")
    while a != "Бежать" and a != "Ждать":
        a = input("У вас есть выбор: Бежать или ждать?\n")
    if a == "Ждать":
        print("Вы стали ждать")
        print("Спустя какое-то время этот силуэт резко двинулся")
        print("Вы сильно испугались и не знаете что делать")
        print("Прошло 3 минуты")
        print("Силуэт не дивгался")
    elif a == "Бежать":
        print("Вы очень быстро побежали домой и думали кто это?")
        a = input("Вы можете уйти или окликнуть силуэт")
        while a != " Окликнуть силуэт" and a != "Уйти":
            a = input("Вы можете уйти или окликнуть силуэт")
        if a == "Окликнуть силуэт":
            print("-Вы кто?")
            print("Силуэт слегка двнулся в вашу сторону и быстро побежал")
            print("Вы побежали и стали думать")
            print("-Кто это или что?!")
            print("-Почему он побежал за мной?!")
            print("Вы выронили перчатку и потеряли её")
            print("Вы посмотрели назад и увидели что там никого нет и вы не увидили следов")
            print("Вы заметели что выронили варежку")
            print("-блин я её потерял")
        elif a == "Уйти":
            print("Вы тихо ушли домой.")
            a = input("Вы можете уйти домой или вернутся за ней")
            while a != "Уйти домой" and a !="Вернутся за варежкой":
                a = input("Вы можете уйти домой или вернутся за ней")
            if a == "Вернутся за варежкой":
                print("Вы решили вернутся за варежкой")
                print("Но увы она пропала")
                print("Вы думаете куда она пропала")
                print("-Может это силуэт взял варежку? Или мне она показалась.Эта варежка")
                print("Вы печальные пошли домой")
            elif a == "Уйти домой":
                print("Вы повернулись и быстро пошли домой")
elif a == "Бежать":
    print("Вы быстро побежали в дом и ещё два дня думали что это было")
elif a == "Окликнуть силуэт":
    print("Вы окликнули силуэт")
    print("Он быстро побежал за вами и вы резко проснулись в своей кровати")