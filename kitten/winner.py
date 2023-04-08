from kitten.player import Player


def winner(player1: Player, player2: Player, cards: list[str]) -> str:
    if player1.defuses + leading_refuses(cards) % 2 > player2.defuses:
        return player1.name
    return player2.name


def leading_refuses(cards: list[str]) -> int:
    if len(cards) == 0:
        return 0
    if "explode" not in cards:
        return len(cards)
    return len(cards) - cards.index("explode") - 1
