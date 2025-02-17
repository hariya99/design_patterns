from typing import override

from components.doors import Door, DoorNeedingSpell
from components.maze import Maze
from components.rooms import EnchantedRoom, Room
from components.wall import Wall


class MazeFactory:
    """
    abstract factory but also provide concrete implementation.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def make_door(r1: Room, r2: Room) -> Door:
        return Door(r1, r2)

    @staticmethod
    def make_maze() -> Maze:
        return Maze()

    @staticmethod
    def make_room(room_no: int) -> Room:
        return Room(room_no)

    @staticmethod
    def make_wall() -> Wall:
        return Wall()


class EnchantedMazeFactory(MazeFactory):
    @override
    @staticmethod
    def make_door(r1: EnchantedRoom, r2: EnchantedRoom) -> Door:
        return DoorNeedingSpell(r1, r2)

    @override
    @staticmethod
    def make_room(room_no: int) -> EnchantedRoom:
        return EnchantedRoom(room_no, "Colloportus")
