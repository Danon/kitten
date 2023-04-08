from kitten.player import Player
from kitten.winner import winner


def test_put_back_on_top_player1_has_defuse():
    assert winner(Player("Kamil", 1), Player("Daniel", 0), ["defuse", "explode"], czy_wsadzil_na_gore=True) == "Kamil"
    assert winner(Player("Daniel", 1), Player("Kamil", 0), ["defuse", "explode"], czy_wsadzil_na_gore=True) == "Daniel"


def test_put_back_on_top_players_has_defuse():
    assert winner(Player("Kamil", 1), Player("Daniel", 1), ["defuse", "explode"], czy_wsadzil_na_gore=True) == "Daniel"
    assert winner(Player("Daniel", 1), Player("Kamil", 1), ["defuse", "explode"], czy_wsadzil_na_gore=True) == "Kamil"


def test_put_back_on_bottom_player1_has_defuse():
    assert winner(Player("Kamil", 1), Player("Daniel", 0), ["defuse", "explode"], czy_wsadzil_na_gore=False) == "Daniel"
    assert winner(Player("Daniel", 1), Player("Kamil", 0), ["defuse", "explode"], czy_wsadzil_na_gore=False) == "Kamil"


def test_put_back_on_bottom_players_have_defuse():
    assert winner(Player("Kamil", 1), Player("Daniel", 1), ["defuse", "explode"], czy_wsadzil_na_gore=False) == "Daniel"
    assert winner(Player("Daniel", 1), Player("Kamil", 1), ["defuse", "explode"], czy_wsadzil_na_gore=False) == "Kamil"
