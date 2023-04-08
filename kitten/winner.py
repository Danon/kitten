from kitten.player import Player
from kitten.players import Players
from kitten.stack import Stack


def winner(players: list[Player], cards: list[str]) -> str:
    players = Players(*players)
    stack = Stack(cards)
    while not stack.empty:
        last_card = stack.pop()
        if last_card == "defuse":
            players.current.defuses += 1
        elif last_card == "explode":
            if players.current.defuses == 0:
                return players.other.name
            players.current.defuses -= 1
            if players.current.puts_at_top:
                stack.add_explode_on_top()
            else:
                stack.add_explode_on_bottom()
        players.next()
