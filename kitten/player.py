class Player:
    def __init__(self, name: str, defuses: int, push_at: int = 0):
        self.name = name
        self.defuses = defuses
        self.push_at = push_at
