"""
"""

from ...utils.enums.enums import Direction

class Position:

    def __init__(self, x, y, direction: Direction):
        self.x: int = x
        self.y: int = y
        self.direction: Direction = direction


def is_same_position(pos1: Position, pos2: Position) -> bool:
    """
    Checks if those to positions are the same.

    params:
        pos1(Position): first position
        pos2(Position): second position

    return:
        bool: whether it is the same position or not
    """
    return pos1.x == pos2.x and pos1.y == pos2.y

def is_vertical(direction: Direction):
    return direction == Direction.NORTH or direction == Direction.SOUTH
