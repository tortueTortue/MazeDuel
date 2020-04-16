"""
Here are all the enums necessary for Maze Duel
"""

from enum import IntEnum

class Direction(IntEnum):
    """
    Direction enum similar to a compass.
    """

    NORTH = 1
    SOUTH = 2
    EAST  = 3
    WEST  = 4
