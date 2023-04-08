def winner(player1: str, player2: str, player1_defuse: int, player2_defuse: int) -> str:
    if player1_defuse > player2_defuse:
        return player1
    return player2
