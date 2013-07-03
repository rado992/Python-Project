#from checker import Checker
import random


CLASSIC_GAME = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
                0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0]

OTHER = {'W': 'B', 'B': 'W'}


class InvalidMove(Exception):
    def __init__(self, message=""):
        self.message = message

class TakenSpace(Exception):
    def __init__(self, message=""):
        self.message = message


class Board:

    def __init__(self, game=CLASSIC_GAME):
        self.field = {}
        self.reset_checkers(game)

    def reset_checkers(self, game=CLASSIC_GAME):
        self.field = {'B': [], 'W': []}
        for i in range(26):
            self.field['B'].append(game[i])
            self.field['W'].append(game[i])
        self.takeout = {'B': False, 'W': False}

    def check_for_takeout(self, colors):
        for c in colors:
            self.takeout[c] = True
            for i in range(19):
                if self.field[c][i] > 0:
                    self.takeout[c] = False
                    break


    def try_to_move(self, color, old, new):
        if self.field[OTHER[color]][25 - new] > 1:
            return False

        if self.field[OTHER[color]][25 - new] <= 1:
            self.field[color][new] += 1
            self.field[color][old] -= 1

        if self.field[OTHER[color]][25 - new] == 1:
            self.field[OTHER[color]][0] += 1
            self.field[OTHER[color]][25 - new] -= 1
        return True


    def move_checker(self, color, position, roll):

        self.check_for_takeout(color)

        if self.field[color][0] > 0:
            if position == 0:
                return self.try_to_move(color, position, position + roll)
            else:
                pass
                #raise InvalidMove()

        if self.takeout[color]:
            if position >= 19:
                if position + roll == 25:
                    return self.try_to_move(color, position, 25)
                elif position + roll > 25:
                    for i in range(19, position):
                        if self.field[color][i] > 0:
                            return False
                            #raise InvalidMove()
                    return self.try_to_move(color, position, 25)
                else:
                    return self.try_to_move(color, position, position + roll)
            else:
                pass
                #raise InvalidMove()

        if 1 <= position <= 23 and position + roll < 24:
            return self.try_to_move(color, position, position + roll)
        else:
            pass
            # raise InvalidMove()

        return False



    def throw_dice(self):
        a, b = random.randrange(1, 7), random.randrange(1, 7)
        if a == b:
            return [a, a, b, b]
        else:
            return [a, b]



    def get_board(self):
        return self.field
        #print(self.taken)
        #print(self.knocked)
a = Board()
#print(a.get_board())
#print (a.move_checker('B', 1, 5))
#for i in range(20):
#    print (a.throw_dice())
#a.print_board()

