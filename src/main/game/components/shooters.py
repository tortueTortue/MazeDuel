"""
"""
import copy
from ...utils.enums.enums import Direction
from ...utils.constants import STEP
from .bullets import Bullet
from ..physics.position import Position
from ..physics.position import is_vertical


class Shooter:
    """
    A shooter is a user controlled agent running and gunning
    around the maze.
    """

    no_of_shooters = 0

    def __init__(self, position: Position, initial_aim_direction: Direction):
        self.position: Position = position
        self.aim: Direction = initial_aim_direction
        self.points: int = 0
        self.id: int = Shooter.no_of_shooters

        Shooter.no_of_shooters += 1

    def increase_points(self) -> None:
        """
        Increases the no of points of the shooter
        by one.
        """
        self.points += 1

    def move_direction(self, direction: Direction) -> None:
        """
        Moves player towards the specified direction.
        """
        move: int = -STEP if 2 % direction else STEP
        if is_vertical(direction):
            self.position.y += move
        else:
            self.position.x += move

    def move(self) -> None:
        """
        Moves player towards the specified direction.
        """
        move: int = -STEP if 2 % self.aim else STEP
        if is_vertical(self.aim):
            self.position.y += move
        else:
            self.position.x += move
    
    def get_next_move(self) -> Position:
        """
        Computes the shooter's next move.

        Return:
            Position: the position of the shooter's next move
        """
        pos: Position = copy.deepcopy(self.position)
        move: int = -STEP if 2 % self.aim else STEP
        if is_vertical(self.aim):
            pos.y += move
        else:
            pos.x += move

        return pos

    def shoot(self) -> Bullet:
        """
        Instiates a bullet at the position of the
        shooter oriented at its aim's direction.
        """
        return Bullet(copy.deepcopy(self.position), self.aim)
