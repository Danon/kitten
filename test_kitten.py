def winner(player1: str, player2: str) -> str:
    return player2


def test():
    assert winner("Kamil", "Daniel") == "Daniel"
    assert winner("Daniel", "Kamil") == "Kamil"
