from kitten.player import Player


def winner(player1: Player, player2: Player, cards: list[str], czy_wsadzil_na_gore: bool = True) -> str:
    if len(cards) > 0 and cards[-1] == "explode":
        if player1.defuses > 0:
            new_stack = ['explode', *cards[:-1]] if not czy_wsadzil_na_gore else cards
            return winner(player2, Player(player1.name, player1.defuses - 1), new_stack)
    if player1.defuses + leading_refuses(cards) % 2 > player2.defuses:
        return player1.name
    return player2.name


def leading_refuses(cards: list[str]) -> int:
    if len(cards) == 0:
        return 0
    if "explode" not in cards:
        return len(cards)
    return len(cards) - cards.index("explode") - 1
