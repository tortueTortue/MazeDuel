"""
"""
import copy
from src.utils.enums.enums import Direction
from src.utils.constants import STEP
from .bullets import Bullet
from ..physics.position import Position
from ..physics.position import is_vertical


class Shooter:
    """
    A shooter is a user controlled agent running and gunning
    around the maze.
    """

    def __init__(self, position: Position, initial_aim_direction: Direction):
        self.position = position
        self.aim = initial_aim_direction
        self.points = 0

    def increase_points(self) -> None:
        """
        Increases the no of points of the shooter
        by one.
        """
        self.points += 1

    def move(self, direction: Direction) -> None:
        """
        Moves player towards the specified direction.
        """
        move: int = -STEP if 2 % direction else STEP
        if is_vertical(direction):
            self.position.y += move
        else:
            self.position.x += move

    def shoot(self) -> Bullet:
        """
        Instiates a bullet at the position of the
        shooter oriented at its aim's direction.
        """
        return Bullet(copy.deepcopy(self.position), self.aim)
