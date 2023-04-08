from typing import Union

from kitten.bot import Bot


class Player:
    def __init__(self, name: str, defuses: int, push_at: Union[int, Bot] = 0):
        self.name = name
        self.defuses = defuses
        self._push_at = push_at

    @property
    def push_at(self) -> int:
        if type(self._push_at) == int:
            return self._push_at
        return self._push_at.gdzie()
