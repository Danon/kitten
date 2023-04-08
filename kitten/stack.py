class Stack:
    def __init__(self, cards: list[str]):
        self.cards = cards

    @property
    def empty(self) -> bool:
        return len(self.cards) == 0

    def put_explode_on(self, position: int) -> None:
        self.cards.insert(len(self.cards) - position, 'explode')

    def pop(self) -> str:
        return self.cards.pop()
