from kitten.player import Player


class Players:
    def __init__(self, players: list[Player]):
        self.players = players
        self.index = 0

    @property
    def current(self) -> Player:
        return self.players[self.index]

    def next(self) -> None:
        self.index = (self.index + 1) % len(self.players)

    def remove(self) -> None:
        self.players.pop(self.index)
        self.index -= 1

    @property
    def is_only_player(self) -> bool:
        return len(self.players) == 1
