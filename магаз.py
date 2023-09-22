class ch():
    def __init__(self,moloko,hleb,sosiska):
        self.moloko = moloko
        self.hleb = hleb
        self.sosiska = sosiska
    def sigma(self):
        kol = 100*self.moloko+32*self.hleb+6*self.sosiska
        print("Вы проиграли в казино(магазине)",kol,"рублей")

moloko = int(input())
hleb =int(input())
sosiska =int(input())
Alfa=ch(moloko,hleb,sosiska)
Alfa.sigma()