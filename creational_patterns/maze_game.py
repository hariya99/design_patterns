from components.direction import Direction
from components.doors import Door
from components.maze import Maze
from components.rooms import Room
from components.wall import Wall
from maze_builder import MazeBuilder, StandardMazeBuilder
from maze_factory import EnchantedMazeFactory, MazeFactory


class MazeGame:
    def create_maze(self) -> Maze:
        """
        Without the use of factory, inflexible, cannot create any other type of maze
        """
        maze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        door = Door(r1, r2)
        maze.add_room(r1)
        maze.add_room(r2)
        r1.set_side(Direction.NORTH, Wall())
        r1.set_side(Direction.EAST, door)
        r1.set_side(Direction.SOUTH, Wall())
        r1.set_side(Direction.WEST, Wall())

        r2.set_side(Direction.NORTH, Wall())
        r2.set_side(Direction.EAST, Wall())
        r2.set_side(Direction.SOUTH, Wall())
        r2.set_side(Direction.WEST, door)
        return maze

    def create_maze_from_builder(self, builder: MazeBuilder) -> Maze:
        """
        pros: construction of rooms and doors is abstracted away.
        cons: Abstraction perhaps is making the code difficult to understand for a regular person??
        """
        # builder.build_maze()
        builder.build_room(1)
        builder.build_room(2)
        builder.build_door(1, 2)
        return builder.get_maze()

    def create_maze_from_factory(self, factory: MazeFactory) -> Maze:
        """
        pros: flexible, using factory, can create multiple type of mazes
        cons: construction of room, door etc is still fixed, can't make different kind of rooms.
        """
        maze = factory.make_maze()
        r1 = factory.make_room(1)
        r2 = factory.make_room(2)
        door = factory.make_door(r1, r2)
        maze.add_room(r1)
        maze.add_room(r2)
        r1.set_side(Direction.NORTH, factory.make_wall())
        r1.set_side(Direction.EAST, door)
        r1.set_side(Direction.SOUTH, factory.make_wall())
        r1.set_side(Direction.WEST, factory.make_wall())

        r2.set_side(Direction.NORTH, factory.make_wall())
        r2.set_side(Direction.EAST, factory.make_wall())
        r2.set_side(Direction.SOUTH, factory.make_wall())
        r2.set_side(Direction.WEST, door)
        return maze


game = MazeGame()

print("========Create Maze========")
m = game.create_maze()
print(m)

print("========Maze Factory========")
maze_factory = MazeFactory()
m = game.create_maze_from_factory(maze_factory)
print(m)

print("========Enchanted Factory========")
enchanted_maze_factory = EnchantedMazeFactory()
m = game.create_maze_from_factory(enchanted_maze_factory)
print(m)
# print(m.room_no(1))

print("========Standard Maze Builder========")
standard_builder = StandardMazeBuilder()
m = game.create_maze_from_builder(standard_builder)
print(m)
