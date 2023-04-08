class Stack:
    def __init__(self, cards: list[str]):
        self.cards = cards

    @property
    def empty(self) -> bool:
        return len(self.cards) == 0

    def add_explode_on_top(self) -> None:
        self.cards.append("explode")

    def add_explode_on_bottom(self) -> None:
        self.cards = ["explode", *self.cards]

    def pop(self) -> str:
        return self.cards.pop()
