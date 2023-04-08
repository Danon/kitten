from pytest import raises

from kitten.player import Player
from kitten.winner import winner, StackException


def test():
    # given
    players = [Player("Kamil", 0), Player("Daniel", 0)]
    # when
    with raises(StackException):
        winner(players, [])

def test_():
    # given
    players = [Player("Kamil", 0), Player("Daniel", 0)]
    # when
    with raises(StackException):
        winner(players, ['defuse'])

def test_4():
    # given
    players = [Player("Kamil", 0), Player("Daniel", 0), Player("Mikołaj", 0)]
    # when
    with raises(StackException):
        winner(players, ['defuse'])

def test_2():
    # given
    players = [Player("Kamil", 0), Player("Daniel", 0)]
    # when
    with raises(StackException):
        winner(players, ['explode', 'explode'])


def test_26():
    # given
    players = [Player("Kamil", 0), Player("Daniel", 0), Player("Mikołaj", 0)]
    # when
    with raises(StackException):
        winner(players, ['explode', 'explode', "explode"])
