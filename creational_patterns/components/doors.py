from components.map_site import MapSite
from components.rooms import EnchantedRoom, Room


class Door(MapSite):
    def __init__(self, room1: Room, room2: Room) -> None:
        super().__init__()
        self._room1 = room1
        self._room2 = room2
        self._is_open = False

    def enter(self):
        print("Entered Door")

    def is_open(self) -> bool:
        return self._is_open

    def __repr__(self) -> str:
        return f"Door {'Open' if self._is_open else 'Closed'} between room {self._room1.room_no} and {self._room2.room_no}"


class DoorNeedingSpell(Door):
    def __init__(self, room1: EnchantedRoom, room2: EnchantedRoom) -> None:
        super().__init__(room1, room2)
