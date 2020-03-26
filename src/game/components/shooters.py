"""
"""
from ..utils.enums import Direction
from .physics.position import Position
import copy

class Shooter:
    """
    A shooter is a user controlled agent
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

    def shoot(self) -> Bullet:
        """
        Instiates a bullet at the position of the
        shooter oriented at its aim's direction.
        """
        return Bullet(copy.deepcopy(self.position), self.aim)