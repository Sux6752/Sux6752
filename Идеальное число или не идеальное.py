a=int(input())
if a%3==0 and a>0:
    print("Оно идеально")
if a%3!=0 and a>0:
    print("Оно не идеально не делится на 3")
if a%3==0 and a<0:
    print("Оно не идеально меньше 0")
if a%3!=0 and a<0:
    print("Оно не идеально меньше 0 и не делится на 3")