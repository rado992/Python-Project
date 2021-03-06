from board import Board
import board
import copy

OTHER = board.OTHER


def make_move(board, color, roll):
    print ("Called with: ", color, roll)
    field = board.get_board()
    max_eval, move = -100000000, 0
    if field[color][0] > 0:
        #print("Hit Case")
        if field[OTHER[color]][25 - roll] <= 1:
            board.move_checker(color, 0, roll)
            return board
    elif board.takeout[color]:
        #print("Takeout Case")
        if field[color][25 - roll] > 0:
            board.move_checker(color, 25-roll, roll)
            return board
        else:
            for i in range(19, 25 - roll):
                if field[color][i] > 0:
                    board.move_checker(color, i, roll)
                    return board
            for i in range(25 - roll, 25):
                if field[color][i] > 0:
                    board.move_checker(color, i, roll)
                    return board
    else:
        #print("Default Case")
        new_board = copy.deepcopy(board)
        for i in range(24, 0, -1):
            if 0 < i - roll < 25 and field[color][i - roll] > 0:
                if new_board.move_checker(color, i - roll, roll):
                    #new_board.print_board()
                    if value(new_board, color) >= max_eval:
                        max_eval = value(new_board, color)
                        move = i
                #print(i)
                #board.print_board()
                #print(value(board, color), max_eval)
                new_board = copy.deepcopy(board)
                #board.print_board()
        #print("Got to here")
        #print(move)
        #board.print_board()
        board.move_checker(color, move - roll, roll)
        return board


def value(board, color):
    field = board.get_board()
    value = 0
    for position in range(1, 25):
        if field[OTHER[color]][25 - position] >= 2:
            value -= (5 - field[OTHER[color]][25 - position])
        if field[OTHER[color]][25 - position] == 1:
            value += 3
        if field[color][position] == 1:
            value += 0.9 - (position / 12)
        if field[color][position] >= 2:
            value += (4 - field[color][position])
        if field[OTHER[color]][25 - position] == field[color][position] == 0:
            value += 0
    return value


def play(board, color, dice):
    max_board = Board()
    new_board = copy.deepcopy(board)
    new_board = copy.deepcopy(make_move(new_board, color, dice[0]))
    new_board = copy.deepcopy(make_move(new_board, color, dice[1]))
    print(new_board.print_board())

    new_board = copy.deepcopy(board)
    new_board = copy.deepcopy(make_move(new_board, color, dice[1]))
    new_board = copy.deepcopy(make_move(new_board, color, dice[0]))
    print(new_board.print_board())

    print(m1, m2, value(max_board, color))
    if m2 > m1:
        #new_board.print_board()
        max_board = copy.deepcopy(new_board)
    else:
        #new_board.print_board()
        max_board = copy.deepcopy(new_board)
    return max_board


def main():
    board = Board()
    dice = board.throw_dice()
    color = 'B'
    line = ""
    board.print_board()
    try:
        while True:
            if color == 'B':
                dice = board.throw_dice()
                print("DICE: ", dice)
                i = 0
                while (i < len(dice)):
                    line = input("What to move " + str(dice[i]) + " places? (0 to switch dice)")
                    if int(line) == 0:
                        tmp = dice[0]
                        for i in range(len(dice) - 1):
                            dice[i] = dice[i + 1]
                        dice[len(dice) - 1] = tmp
                        continue
                    elif line == "exit":
                        return
                    pos = int(line)
                    if board.move_checker(color, pos, dice[i]):
                        i += 1
                    else:
                        print("Cannot move this, try again!")
                    board.print_board()
                color = OTHER[color]
            else:
                dice = board.throw_dice()
                print("DICE: ", dice)
                try:
                    if len(dice) == 2:
                        try:
                            board = copy.deepcopy(play(board, color, dice))
                        except:
                            board = copy.deepcopy(play(board, color, [dice[1], dice[0]]))
                        #print("Max: \n", play(board, color, dice).print_board())
                    elif len(dice) == 4:
                        board = copy.deepcopy(play(board, color, [dice[0], dice[1]]))
                        board = copy.deepcopy(play(board, color, [dice[2], dice[3]]))
                    board.print_board()
                    color = OTHER[color]
                except:
                    color = OTHER[color]
    except:
        print("End of game")


def can_form_heap(board, color, position, rolls):
    benefit = 0
    field = board.get_board()
    if field[OTHER[color]][25 - position] >= 2:
        benefit -= 30
    if field[OTHER[color]][25 - position] == 1:
        benefit += 7
        if field[color][position - rolls[0]] > 2:
            if field[color][position - rolls[1]] >= 2:
                benefit += 2
            elif field[color][position - rolls[1]] == 1:
                benefit += 3
        elif field[color][position - rolls[0]] == 1:
            if field[color][position - rolls[1]] > 2:
                benefit += 3
            elif field[color][position - rolls[1]] == 1:
                benefit += 4
    if field[color][position] == 1:
        benefit += 4
    if field[color][position] >= 2:
        benefit += (3 - field[color][position])
    if field[OTHER[color]][25 - position] == 0 and field[color][position] == 0:
        benefit += 2


def point_benefit(board, color, position):
    benefit = 0
    field = board.get_board()
    if field[OTHER[color]][25 - position] >= 2:
        benefit -= 30
    if field[OTHER[color]][25 - position] == 1:
        benefit += 5
    if field[color][position] == 1:
        benefit += 4
    if field[color][position] >= 2:
        benefit += 3
    if field[OTHER[color]][25 - position] == 0 and field[color][position] == 0:
        benefit += 2
    return benefit

if __name__ == "__main__":
    main()
