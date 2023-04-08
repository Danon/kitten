class Bot:
    def __init__(self, first, sec):
        self.first = first
        self.sec = sec
        self.move = False

    def gdzie(self) -> int:
        if not self.move:
            self.move = not self.move
            return self.first
        self.move = not self.move
        return self.sec
