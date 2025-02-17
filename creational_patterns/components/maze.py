from typing import Dict

from components.type_hints import RoomType


class Maze:
    def __init__(self) -> None:
        self._rooms: Dict[int, RoomType] = {}

    def add_room(self, room: RoomType) -> None:
        self._rooms[room.room_no] = room

    def room_no(self, room_no: int) -> RoomType:
        return self._rooms[room_no]

    def __repr__(self) -> str:
        return f"{self._rooms}"
