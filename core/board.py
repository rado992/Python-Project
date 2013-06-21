from checker import Checker


class Board:

    def __init__(self):
        self.points = {}
        for i in range(26):
            self.points[i] = []
        self.checkers = {}
        for i in range(15):
        	print(i)
        	self.checkers[i] = Checker("B", 0)
        	self.checkers[i + 15] = Checker("W", 0)
