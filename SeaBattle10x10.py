from random import randint


class GameException(Exception):
    pass


class NotInBoard(GameException):
    def __str__(self):
        return "Не стреляй за доску!"


class AlreadyUsed(GameException):
    def __str__(self):
        return "В эту точку ты уже стрелял!"


class WrongShipLocation(GameException):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


class Ship:
    def __init__(self, firstpoint, length, oriental):
        self.fp = firstpoint
        self.len = length
        self.o = oriental
        self.hp = length

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.len):
            current_x = self.fp.x
            current_y = self.fp.y

            if self.o == 0:
                current_x += i

            elif self.o == 1:
                current_y += i

            ship_dots.append(Dot(current_x, current_y))

        return ship_dots

    def damage(self, dmg):
        return dmg in self.dots


s = 0


class Board:
    def __init__(self, hid=False, size=10):
        self.size = size
        self.hid = hid

        self.destroyed_ships = 0

        self.field = [["0"] * size for _ in range(size)]

        self.used = []
        self.ships = []

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.used:
                raise WrongShipLocation()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.used.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for d in ship.dots:
            for dx, dy in near:
                current = Dot(d.x + dx, d.y + dy)
                if not (self.out(current)) and current not in self.used:
                    if verb:
                        self.field[current.x][current.y] = '.'
                    self.used.append(current)

    def __str__(self):
        res = ''
        res += '  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|'
        for i, row in enumerate(self.field):
            if i < 9:
                res += f'\n{i + 1} | ' + ' | '.join(row) + ' |'
            else:
                res += f'\n{i + 1}| ' + ' | '.join(row) + ' |'

        if self.hid:
            res = res.replace("■", "0")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise NotInBoard()

        if d in self.used:
            raise AlreadyUsed()

        self.used.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.hp -= 1
                self.field[d.x][d.y] = 'X'
                if ship.hp == 0:
                    self.destroyed_ships += 1
                    self.contour(ship, verb=True)
                    print("Корабль потоплен!")
                    return True
                else:
                    print("Корабль поврежден!")
                    return True
        self.field[d.x][d.y] = '.'
        print("Промах!")
        return False

    def begin(self):
        self.used = []


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except GameException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 9), randint(0, 9))
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except GameException as e:
                print(e)


class User(Player):
    def ask(self):
        while True:
            cords = input("Куда стреляем? ").split()

            if len(cords) != 2:
                print("Введи 2 цифры!")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Это не цифры! Введи цифры")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:
    def __init__(self, size=10):
        self.size = size
        player = self.random_board()
        computer = self.random_board()
        computer.hid = True

        self.ai = AI(computer, player)
        self.us = User(player, computer)

    def try_board(self):
        lens = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for el in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), el, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except WrongShipLocation:
                    pass

        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("-" * 43)
        print("      Добро пожаловать в морской бой!  ")
        print(" При запросе выстрела вводите две цифры: x y ")
        print("            x - номер строки  ")
        print("            y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-" * 43)
            print("            Доска пользователя:")
            print(self.us.board)
            print("-" * 43)
            print("            Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 43)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 43)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.destroyed_ships == 10:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.destroyed_ships == 10:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
