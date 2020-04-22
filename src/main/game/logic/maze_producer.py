"""
Maze tools
"""

import copy

from ..physics.position import Position
from ..components.walls import Wall
from ...utils.enums.enums import Direction

class Maze: 
    """
    """
    def __init__(self, width: int, height: int, position: Position):
        self.walls = []
        self.__create_frame(width, height, position)
    
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