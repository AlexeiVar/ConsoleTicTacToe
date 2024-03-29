def status(): # Просто печатаю поле
    print(" ", 0, 1, 2)
    i = 0
    for row in game_status:
        print(i, row[0], row[1], row[2])
        i += 1


def check_win(n):
    # Помечаю кто игрок если вдруг будет победа
    if n == 'X':
        player = "крестики"
    else:
        player = "нолики"
    # Проверки если есть центр
    if game_status[1][1] == n:
        if n == game_status[0][0] == game_status[2][2]:
            print(f"Победили {player}")
            return True
        if n == game_status[0][2] == game_status[2][0]:
            print(f"Победили {player}")
            return True
        if n == game_status[0][1] == game_status[2][1]:
            print(f"Победили {player}")
            return True
        if n == game_status[1][0] == game_status[1][2]:
            print(f"Победили {player}")
            return True
    # Все это проверка победы без центра
    else:
        if game_status[0][0] == n:
            if n == game_status[0][1] == game_status[0][2]:
                print(f"Победили {player}")
                return True
            elif n == game_status[1][0] == game_status[2][0]:
                print(f"Победили {player}")
                return True
        if game_status[2][2] == n:
            if n == game_status[1][2] == game_status[0][2]:
                print(f"Победили {player}")
                return True
            elif n == game_status[2][1] == game_status[2][0]:
                print(f"Победили {player}")
                return True

# Оба просто ставят символ куда надо с проверкой что свободно
def put_x():
    cords = input("Введите строку и столб без пробела в которую хотите поставить крестик")
    a, b = list(cords.strip())
    while game_status[int(a)][int(b)] == ('X' or 'O'):
        print("Место уже занято, выберите другое место")
        cords = input("Введите строку и столб без пробела в которую хотите поставить крестик")
        a, b = list(cords.strip())
    game_status[int(a)][int(b)] = 'X'


def put_o():
    cords = input("Введите строку и столб без пробела в которую хотите поставить нолик")
    a, b = list(cords.strip())
    while game_status[int(a)][int(b)] == ('X' or 'O'):
        print("Место уже занято, выберите другое место")
        cords = input("Введите строку и столб без пробела в которую хотите поставить нолик")
        a, b = list(cords.strip())
    game_status[int(a)][int(b)] = 'O'


game_status = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
status()
while True:
    put_x()
    status()
    if check_win("X"):
        break
    put_o()
    status()
    if check_win("O"):
        break
