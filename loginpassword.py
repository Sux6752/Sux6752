loginpass={}
a=0
while a == 0:
    login=input("Напишите логин ")
    password=input("Напишите пароль ")
    if len(password)<8:
        print("Ваш пароль должен быть не менее 8 знаков")
    else:
        loginpass[login]=password
        print(loginpass)
        a=1
    
