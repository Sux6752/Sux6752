players = []
while True:
    com1=input('''Добавьте игрока например:
    Игорь
    62
    ''')
    com2=input("")
    player = {"Имя" : com1, "Рек" : com2}
    players.append(player)
    print(players)