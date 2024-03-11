mas = [[' ', 1, 2, 3], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-']]

def field():
    global mas
    for i in range(0, len(mas)):
        for j in range(0, len(mas[i])):
            print(mas[i][j], end=' ')
        print()

def move_p1():
    move_numb = int(input("Введите номер столбца в который вы хотите поставить Х: "))
    move_liter = int(input("Введите номер строки в который вы хотите поставить Х: "))
    if mas[move_liter][move_numb] != '-':
        print("Эта ячейка уже занята! Выбери другую.")
        return move_p1()
    mas[move_liter][move_numb] = 'X'
    return field()

def move_p2():
    move_numb = int(input("Введите номер столбца в который вы хотите поставить О: "))
    move_liter = int(input("Введите номер строки в который вы хотите поставить О: "))
    if mas[move_liter][move_numb] != '-':
        print("Эта ячейка уже занята! Выбери другую.")
        return move_p2()
    mas[move_liter][move_numb] = 'O'
    return field()

def win_conditionO():
    if mas[1][1] == 'O' and mas[1][2] == 'O' and mas[1][3] == 'O':
        print("Игра окончена! Победил игрок 2")
        exit()
    elif mas[2][1] == 'O' and mas[2][2] == 'O' and mas[2][3] == 'O':
        print("Игра окончена! Победил игрок 2")
        exit()
    elif mas[3][1] == 'O' and mas[3][2] == 'O' and mas[3][3] == 'O':
        print("Игра окончена! Победил игрок 2")
        exit()
    elif mas[1][1] == 'O' and mas[2][1] == 'O' and mas[3][1] == 'O':
        print("Игра окончена! Победил игрок 2")
        exit()
    elif mas[1][2] == 'O' and mas[2][2] == 'O' and mas[3][2] == 'O':
        print("Игра окончена! Победил игрок 2")
        exit()
    elif mas[1][3] == 'O' and mas[2][3] == 'O' and mas[3][3] == 'O':
        print("Игра окончена! Победил игрок 2")
        exit()
    elif mas[1][1] == 'O' and mas[2][2] == 'O' and mas[3][3] == 'O':
        print("Игра окончена! Победил игрок 2")
        exit()
    elif mas[3][1] == 'O' and mas[2][2] == 'O' and mas[1][3] == 'O':
        print("Игра окончена! Победил игрок 2")
        exit()

def win_condition():
    if mas[1][1] == 'X' and mas[1][2] == 'X' and mas[1][3] == 'X':
        print("Игра окончена! Победил игрок 1")
        exit()
    elif mas[2][1] == 'X' and mas[2][2] == 'X' and mas[2][3] == 'X':
        print("Игра окончена! Победил игрок 1")
        exit()
    elif mas[3][1] == 'X' and mas[3][2] == 'X' and mas[3][3] == 'X':
        print("Игра окончена! Победил игрок 1")
        exit()
    elif mas[1][1] == 'X' and mas[2][1] == 'X' and mas[3][1] == 'X':
        print("Игра окончена! Победил игрок 1")
        exit()
    elif mas[1][2] == 'X' and mas[2][2] == 'X' and mas[3][2] == 'X':
        print("Игра окончена! Победил игрок 1")
        exit()
    elif mas[1][3] == 'X' and mas[2][3] == 'X' and mas[3][3] == 'X':
        print("Игра окончена! Победил игрок 1")
        exit()
    elif mas[1][1] == 'X' and mas[2][2] == 'X' and mas[3][3] == 'X':
        print("Игра окончена! Победил игрок 1")
        exit()
    elif mas[3][1] == 'X' and mas[2][2] == 'X' and mas[1][3] == 'X':
        print("Игра окончена! Победил игрок 1")
        exit()

def game():
    move_p1()
    win_condition()
    move_p2()
    win_conditionO()
    move_p1()
    win_condition()
    move_p2()
    win_conditionO()
    move_p1()
    win_condition()
    move_p2()
    win_conditionO()
    move_p1()
    win_condition()
    move_p2()
    win_conditionO()
    move_p1()
    win_condition()

game()


