import board


OTHER = board.OTHER

def make_move(self, board):
    pass

def point_benefit(self, board, position, color):
    checker_count = board.get_field()[position][OTHER[color]]
    if checker_count == 1:
        return 2
    elif checker_count == 0:
        return 1
    else:
        return -1

print(OTHER['W'])


