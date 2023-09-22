class ch():
    def __init__(self,one,two,three):
        self.one = one
        self.two = two
        self.three = three
    def sigma(self):
        kol = (float(self.one)+float(self.two)+float(self.three))
        p = 15000-kol
        if kol > 15000 or kol == 15000:
            print("Вам хватает")
        else:
            print("Вам не хватает ", p ," рублей")

one = int(input())
two =int(input())
three =int(input())
Alfa=ch(one,two,three)
Alfa.sigma()