from kitten.player import Player
from kitten.players import Players


def winner(player1: Player, player2: Player, cards: list[str]) -> str:
    players = Players(player1, player2)

    while len(cards) > 0:
        last_card = cards.pop()
        if last_card == "defuse":
            players.current.defuses += 1
        elif last_card == "explode":
            if players.current.defuses == 0:
                return players.other.name

            players.current.defuses -= 1
            if players.current.puts_at_top:
                cards.append("explode")
            else:
                cards = ["explode", *cards]
        players.next()
