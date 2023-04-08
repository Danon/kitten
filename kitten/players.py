from kitten.player import Player


class Players:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.is_player1 = True

    @property
    def current(self) -> Player:
        return self.player1 if self.is_player1 else self.player2

    @property
    def other(self) -> Player:
        return self.player2 if self.is_player1 else self.player1

    def next(self) -> None:
        self.is_player1 = not self.is_player1
