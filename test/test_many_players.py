from kitten.player import Player
from kitten.winner import winner


def test_three_players():
    # given
    players = [
        Player("Kamil", 0),
        Player("Daniel", 0),
        Player("Mikołaj", 0)
    ]
    # when
    assert winner(players, ['explode', 'explode']) == "Mikołaj"


def test_four_players():
    # given
    players = [
        Player("Kamil", 0),
        Player("Daniel", 0),
        Player("Mikołaj", 0),
        Player("Izabela", 0),
    ]
    # when
    assert winner(players, ['explode', 'explode', 'explode']) == "Izabela"


def test_three_players_last_player_puts_at_top():
    # given
    players = [
        Player("Kamil", 0, puts_at_top=False),
        Player("Daniel", 0, puts_at_top=True),
        Player("Mikołaj", 1, puts_at_top=True)
    ]
    # when
    assert winner(players, ['defuse', 'explode', 'explode', 'filler', 'defuse']) == "Mikołaj"
