import kitten.winner
from kitten.player import Player


def test_no_defuses():
    assert winner("Kamil", "Daniel", 0, 0, ['explode']) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 0, ['explode']) == "Kamil"


def test_player1_has_defuse():
    assert winner("Kamil", "Daniel", 1, 0, ['explode']) == "Kamil"
    assert winner("Daniel", "Kamil", 1, 0, ['explode']) == "Daniel"


def test_player2_also_has_defuse():
    assert winner("Kamil", "Daniel", 1, 1, ['explode']) == "Daniel"
    assert winner("Daniel", "Kamil", 1, 1, ['explode']) == "Kamil"


def test_player2_only_has_defuse():
    assert winner("Kamil", "Daniel", 0, 1, ['explode']) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 1, ['explode']) == "Kamil"


def test_player1_has_two_defuses():
    assert winner("Kamil", "Daniel", 2, 1, ['explode']) == "Kamil"
    assert winner("Daniel", "Kamil", 2, 1, ['explode']) == "Daniel"


def test_player2_has_two_defuses():
    assert winner("Kamil", "Daniel", 1, 2, ['explode']) == "Daniel"
    assert winner("Daniel", "Kamil", 1, 2, ['explode']) == "Kamil"


def test_players_have_two_defuses():
    assert winner("Kamil", "Daniel", 2, 2, ['explode']) == "Daniel"
    assert winner("Daniel", "Kamil", 2, 2, ['explode']) == "Kamil"


def winner(player1: str, player2: str, player1_defuse: int, player2_defuse: int, cards: list[str]) -> str:
    return kitten.winner.winner([Player(player1, player1_defuse), Player(player2, player2_defuse)], cards)
