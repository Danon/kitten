class Player:
    def __init__(self, name: str, defuses: int, puts_at_top: bool = True):
        self.name = name
        self.defuses = defuses
        self.puts_at_top = puts_at_top
