from kitten.player import Player
from kitten.bot import Bot
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
        Player("Kamil", 0, push_at=99),
        Player("Daniel", 0, push_at=0),
        Player("Mikołaj", 1, push_at=0)
    ]
    # when
    assert winner(players, ['defuse', 'explode', 'explode', 'filler', 'defuse']) == "Mikołaj"


def test_player_puts_card_in_the_middle():
    # given
    players = [
        Player("Kamil", 1, push_at=1),
        Player("Daniel", 0),
    ]
    # when
    assert winner(players, ['filler', 'filler', 'explode']) == "Daniel"


def test_player_puts_card_in_multiple_places():
    # given
    players = [
        Player("Kamil", 1, push_at=Bot(2, 4)),
        Player("Daniel", 2),
    ]
    cards = ["defuse", 'filler', "filler", "filler", "defuse", "filler", 'explode']
    # when
    assert winner(players, cards) == "Kamil"
