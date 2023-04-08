def winner(player1: str, player2: str, player1_defuse: int, player2_defuse: int, cards: list[str]) -> str:
    if len(cards) == 2:
        if cards[0] == "defuse":
            return player2
        return player1
    if player1_defuse > player2_defuse:
        return player1
    return player2
