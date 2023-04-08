import kitten.winner
from kitten.player import Player


def test_one_defuse_in_stack_explode_last():
    assert winner("Kamil", "Daniel", 0, 0, ["explode", "defuse"]) == "Kamil"
    assert winner("Daniel", "Kamil", 0, 0, ["explode", "defuse"]) == "Daniel"


def test_one_defuse_in_stack_explode_first():
    assert winner("Kamil", "Daniel", 0, 0, ["defuse", "explode"]) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 0, ["defuse", "explode"]) == "Kamil"


def test_two_defuses_in_stack_explode_last():
    assert winner("Kamil", "Daniel", 0, 0, ["explode", "defuse", "defuse"]) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 0, ["explode", "defuse", "defuse"]) == "Kamil"


def test_two_defuses_in_stack_explode_middle():
    assert winner("Kamil", "Daniel", 0, 0, ["defuse", "explode", "defuse"]) == "Kamil"
    assert winner("Daniel", "Kamil", 0, 0, ["defuse", "explode", "defuse"]) == "Daniel"


def test_two_defuses_in_stack_explode_first():
    assert winner("Kamil", "Daniel", 0, 0, ["defuse", "defuse", "explode"]) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 0, ["defuse", "defuse", "explode"]) == "Kamil"


def test_initial_defuse_and_defuse_from_cards():
    assert winner("Kamil", "Daniel", 0, 2, ["explode", "defuse"]) == "Daniel"
    assert winner("Daniel", "Kamil", 0, 2, ["explode", "defuse"]) == "Kamil"


def winner(player1: str, player2: str, player1_defuse: int, player2_defuse: int, cards: list[str]) -> str:
    return kitten.winner.winner(Player(player1, player1_defuse), Player(player2, player2_defuse), cards)
