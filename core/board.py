from checker import Checker
import random


CLASSIC_GAME = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
                0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0]

OTHER = {'W': 'B', 'B': 'W'}


class InvalidMove(Exception):
    def __init__(self, message=""):
        self.message = message


class Board:

    def __init__(self):
        self.field = {}
        for i in range(24):
            self.field[i + 1] = {'B': CLASSIC_GAME[i], 'W': CLASSIC_GAME[23 - i]}
        self.taken = {'B': 0, 'W': 0}
        self.knocked = {'B': 0, 'W': 0}

    def reset_checkers(self):
        for i in range(24):
            self.field[i + 1] = {'B': CLASSIC_GAME[i], 'W': CLASSIC_GAME[23 - i]}

    def move_checker(self, position, color, places):
        if self.field[position][color] >= 1 and position + places < 24:
            if self.field[position + places][OTHER[color]] <= 1:
                
                self.field[position][color] -= 1
                self.field[position + places][color] += 1

                if self.field[position + places][OTHER[color]] == 1:

                    self.field[position + places][OTHER[color]] -= 1
                    self.knocked[OTHER[color]] += 1
                return 1
        return 0

    def throw_dice(self):
        a, b = random.randrange(1, 7), random.randrange(1, 7)
        if a == b:
            return [a, a, b, b]
        else:
            return [a, b]



    def print_board(self):
        print(self.field)
        print(self.taken)
        print(self.knocked)
a = Board()
#a.print_board()
#print (a.move_checker(1, 'B', 5))
for i in range(20):
    print (a.throw_dice())
#a.print_board()
