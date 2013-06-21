class Checker:

    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self, position):
        if(position < 26):
            self.position = position

