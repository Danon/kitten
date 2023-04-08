from kitten.player import Player
from kitten.winner import winner


def test_put_back_on_top_player1_has_defuse():
    assert winner(Player("Kamil", 1, True), Player("Daniel", 0, True), ["defuse", "explode"]) == "Kamil"
    assert winner(Player("Daniel", 1, True), Player("Kamil", 0, True), ["defuse", "explode"]) == "Daniel"


def test_put_back_on_bottom_player1_has_defuse():
    assert winner(Player("Kamil", 1, False), Player("Daniel", 0, False), ["defuse", "explode"]) == "Daniel"
    assert winner(Player("Daniel", 1, False), Player("Kamil", 0, False), ["defuse", "explode"]) == "Kamil"


def test_put_back_on_top_players_has_defuse():
    assert winner(Player("Kamil", 1), Player("Daniel", 1), ["defuse", "explode"]) == "Daniel"
    assert winner(Player("Daniel", 1), Player("Kamil", 1), ["defuse", "explode"]) == "Kamil"


def test_put_back_on_bottom_players_have_defuse():
    assert winner(Player("Kamil", 1), Player("Daniel", 1), ["defuse", "explode"]) == "Daniel"
    assert winner(Player("Daniel", 1), Player("Kamil", 1), ["defuse", "explode"]) == "Kamil"


def test_put_back_many_times():
    # given
    cards = ['defuse', 'explode', 'defuse', 'defuse', 'defuse']
    # when
    assert winner(Player("Kamil", 0, puts_at_top=False), Player("Daniel", 0, puts_at_top=True), cards) == "Daniel"
