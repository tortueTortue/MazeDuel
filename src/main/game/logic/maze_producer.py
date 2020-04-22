"""
Maze tools
"""

import copy
import random

from ..physics.position import Position
from ..components.walls import Wall
from ...utils.enums.enums import Direction

class Maze: 
    """
    """
    def __init__(self, width: int, height: int, position: Position):
        self.walls = []
        self.position: Position = position
        self.height: int = height
        self.width: int = width
        self.__create_frame(width, height, position)
        self.__generate_maze()
    
    def __create_frame(self, width: int, height: int, position: Position) -> None:
        """
        """
        entrance_size: int = 60
        self.walls.append(Wall(position, (width-entrance_size)/2, Direction.EAST))
        pos: Position = copy.deepcopy(position)
        pos.x += (width-entrance_size)/2 + entrance_size
        self.walls.append(Wall(pos, (width-entrance_size)/2, Direction.EAST))
        self.walls.append(Wall(position, height, Direction.NORTH))
        
        pos: Position = copy.deepcopy(position)
        pos.x += width
        self.walls.append(Wall(pos, height, Direction.NORTH))
        pos: Position = copy.deepcopy(position)
        pos.y += height
        self.walls.append(Wall(pos, (width-entrance_size)/2, Direction.EAST))
        pos: Position = copy.deepcopy(position)
        pos.y += height
        pos.x += (width-entrance_size)/2 + entrance_size
        self.walls.append(Wall(pos, (width-entrance_size)/2, Direction.EAST))

    def __generate_maze(self):
        """
        """
        entrance_size: int = 60
        jump: int = self.height / 7
        pos: Position = copy.deepcopy(self.position)
        for i in range(7-1):
            pos.y += jump
            wall_no:int = random.randint(2, 5)
            wall_size: int = (self.width - (wall_no - 1) * entrance_size)/wall_no
            for j in range(wall_no):
                self.walls.append(Wall(pos, wall_size, Direction.EAST))
                pos: Position = copy.deepcopy(pos)
                if bool(random.getrandbits(1)) :
                    if bool(random.getrandbits(1)) :
                        self.walls.append(Wall(pos, jump, Direction.NORTH))
                    else:
                        p: Position = copy.deepcopy(pos)
                        p.y -= jump
                        self.walls.append(Wall(p, jump, Direction.NORTH))
                pos.x += wall_size + entrance_size
            pos.x = self.position.x

    def touches(self, position: Position):
        """
        Verifies whether the position touches the maze's walls
        or not

        params:
            position(Position): position to verify 

        return:
            bool: whether position is touches wall or not
        """
        for wall in self.walls:
            if wall.touching(position):
                return True
        return False

def produce_maze() -> Maze:
    """
    """
    return None