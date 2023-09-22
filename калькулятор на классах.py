class number():
    def __init__(self, n1, n2):
        self.n1 = int(input('введите число: '))
        self.n2 = int(input('введите число: '))
    def p(self):
        print(self.n1 + self.n2)
    def v(self):
        print(self.n1 - self.n2)

    def y(self):
        print(self.n1 * self.n2)

    def d(self):
       print(self.n1 / self.n2)

c = number('n1', 'n2')
while True:
    b = input('выберите действие: ')
    if b == 'сложение':
        c.p()
            print(c.p())
elif b == 'вычитание':
    c.v()
    print(c.v())
elif b == 'деление':
    c.d()
    print(c.d())
elif b == 'умножение':
    c.y()
    print(c.y())    