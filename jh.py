keyandlogin3={"Пароль" : "АБОБУС228","Логин" : "СУСОВИЧ","Пароль1" : "МЕГАХАРОШ","Логин1" : "ХАРОШ","Пароль2" : "СССССУУУУУССССС","Логин3" : "ИМПОСТЕРИССУС"}
print(keyandlogin3.values())
command=0
key=0
login=0
key1=0
login1=0
key2=0
login2=0
while command != 3:
    command=int(input('''Введите число |1| чтобы зарегатся |2| чтобы залогинится и |3| чтобы выйти
'''))
    if command == 2:
        login=input("Введите пароль -- ")
        if login in keyandlogin3.keys():
            key=input("Введите пароль")
        if key == keyandlogin3[login]:
            print("Вы вошли")
    if command == 1:
        login1=input("Введите логин -- ")
        def code(key1,key2):
            if not login1 in keyandlogin3.values():
                key1=input("Введите пароль -- ")
                key2=input("Введите пароль ещё раз -- ")
                if key1 == key2:
                    print("Вы зарегестрировались!")
                if key1 != key2:
                    code(key1,key2)
        code(key1,key2)
        if login1 in keyandlogin3.values():
            while login1 in keyandlogin3.values():
                login1=input("Введите логин заново")
            code(key1,key2)
    if command == 3:
        break;
                