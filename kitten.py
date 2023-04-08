def winner(player1: str, player2: str, player1_defuse: int, player2_defuse: int, cards: list[str]) -> str:
    if player1_defuse + leading_refuses(cards) % 2 > player2_defuse:
        return player1
    return player2


def leading_refuses(cards: list[str]) -> int:
    if len(cards) == 0:
        return 0
    if "explode" not in cards:
        return len(cards)
    return len(cards) - cards.index("explode") - 1
