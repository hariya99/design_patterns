from typing import Dict

from components.direction import Direction
from components.map_site import MapSite


class Room(MapSite):
    def __init__(self, room_no: int) -> None:
        super().__init__()
        self._room_no = room_no
        self._sides: Dict[str, MapSite] = {}

    def enter(self):
        print(f"Entered in room: {self._room_no}")

    def get_side(self, direction: Direction) -> MapSite:
        return self._sides[direction.name]

    def set_side(self, direction: Direction, entity: MapSite):
        self._sides[direction.name] = entity

    @property
    def room_no(self):
        return self._room_no

    def __repr__(self) -> str:
        s = "\nRoom No: " + str(self._room_no) + "\nSides: "
        for k, v in self._sides.items():
            s += f"{k} : {v}\n"
        return s


class EnchantedRoom(Room):
    def __init__(self, room_no: int, spell: str) -> None:
        super().__init__(room_no)
        self._spell = spell

    def __repr__(self) -> str:
        s = super().__repr__()
        s += f"Spell: {self._spell}\n"
        return s
