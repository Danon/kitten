from kitten.player import Player
from kitten.players import Players
from kitten.stack import Stack


def winner(players: list[Player], deck: list[str]) -> str:
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
                if players.current.puts_at_top:
                    stack.add_explode_on_top()
                else:
                    stack.add_explode_on_bottom()
        players.next()
        if players.is_only_player:
            return players.current.name
