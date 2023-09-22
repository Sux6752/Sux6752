class ch():
    def __init__(self,one,two):
        self.one = one
        self.two = two
    def sigma(self):
        print((int(self.one)+int(self.two))/2)

one = int(input())
two =int(input())
Alfa=ch(one,two)
Alfa.sigma()