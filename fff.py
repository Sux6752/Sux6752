keyandlogin3={"Пароль" : "АБОБУС228","Логин" : "СУСОВИЧ","Пароль1" : "МЕГАХАРОШ","Логин1" : "ХАРОШ","Пароль2" : "СССССУУУУУССССС","Логин3" : "ИМПОСТЕРИССУС"}
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
        if not login1 in keyandlogin3:
            key1=input("Введите пароль -- ")
            key2=input("Введите пароль ещё раз -- ")
            if key1 != key2
        else:
            while login1 not in keyandlogin3:
                login2=input("Введите пароль заново")
                
                
                
                
                