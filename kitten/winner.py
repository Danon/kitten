from kitten.player import Player
from kitten.players import Players
from kitten.stack import Stack


class StackException(Exception):
    pass


def winner(players: list[Player], deck: list[str]) -> str:
    if deck.count("explode") != len(players) - 1:
        raise StackException()

    players = Players(players)
    stack = Stack(deck)
    while not stack.empty:
        last_card = stack.pop()
        if last_card == "defuse":
            players.current.defuses += 1
        elif last_card == "explode":
            if players.current.defuses == 0:
                players.remove()
            else:
                players.current.defuses -= 1
                stack.put_explode_on(players.current.push_at)
        players.next()
        if players.is_only_player:
            return players.current.name
