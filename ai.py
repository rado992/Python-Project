import board


OTHER = board.OTHER

def make_move(board):
    pass

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


print(OTHER['W'])
a = board.Board()
make_move(a)

for i in range(2,2):
    print (i)
