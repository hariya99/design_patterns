from abc import abstractmethod

from components.direction import Direction
from components.doors import Door
from components.maze import Maze
from components.rooms import Room
from components.wall import Wall


class MazeBuilder:
    @abstractmethod
    def build_door(self, room_from: int, room_to: int):
        pass

    @abstractmethod
    def build_maze(self):
        pass

    @abstractmethod
    def build_room(self, room: int):
        pass

    @abstractmethod
    def get_maze(self) -> Maze:
        pass


class StandardMazeBuilder(MazeBuilder):
    def __init__(self) -> None:
        super().__init__()
        # type hints are not allowing to set this to None
        # self._current_maze = None
        self.build_maze()

    def build_door(self, room_from: int, room_to: int):
        r1 = self._current_maze.room_no(room_from)
        r2 = self._current_maze.room_no(room_to)
        d = Door(r1, r2)
        door_wall = self.common_wall(r1, r2)
        r1.set_side(door_wall, d)
        r2.set_side(door_wall, d)

    def build_maze(self):
        self._current_maze = Maze()

    def build_room(self, room_no: int):
        try:
            _ = self._current_maze.room_no(room_no)
        except KeyError:
            room = Room(room_no)
            room.set_side(Direction.EAST, Wall())
            room.set_side(Direction.WEST, Wall())
            room.set_side(Direction.NORTH, Wall())
            room.set_side(Direction.SOUTH, Wall())
            self._current_maze.add_room(room)

    def common_wall(self, r1: Room, r2: Room) -> Direction:
        if r1.room_no < r2.room_no:
            return Direction.EAST
        else:
            return Direction.WEST

    def get_maze(self) -> Maze:
        return self._current_maze
