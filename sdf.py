class ch():
    def __init__(self,one,two,three):
        self.one = one
        self.two = two
        self.three = three
    def sigma(self):
        print(int(self.one)+int(self.two)+int(self.three))

one = int(input())
two =int(input())
three =int(input())
Alfa=ch(one,two,three)
Alfa.sigma()