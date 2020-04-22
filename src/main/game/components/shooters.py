"""
"""
import copy

from PyQt5.QtCore import Qt
from ...utils.enums.enums import Direction
from ...utils.constants import STEP, SHOOTER_SIZE, BULLET_SIZE
from .bullets import Bullet
from ..physics.position import Position
from ..physics.position import is_vertical
from ..logic.controls import Controls

class Shooter:
    """
    A shooter is a user controlled agent running and gunning
    around the maze.
    """

    no_of_shooters = 0

    def __init__(self, position: Position, initial_aim_direction: Direction, controls: Controls):
        self.position: Position = position
        self.aim: Direction = initial_aim_direction
        self.points: int = 0
        self.id: int = Shooter.no_of_shooters
        self.controls: Controls = controls

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
        move: int = -STEP if direction % 2 == 0 else STEP
        if is_vertical(direction):
            self.position.y += move
        else:
            self.position.x += move

    def move(self) -> None:
        """
        Moves player towards the specified direction.
        """
        move: int = -STEP if self.aim % 2 == 0 else STEP
        if is_vertical(self.aim):
            self.position.y += move
        else:
            self.position.x += move
    
    def reorient_aim(self, key: Qt.Key) -> None:
        """
        Changes direction according the key.
        """
        self.aim = self.controls.control_to_direction(key)

    def get_next_move(self) -> Position:
        """
        Computes the shooter's next move.

        Return:
            Position: the position of the shooter's next move
        """
        pos: Position = copy.deepcopy(self.position)
        move: int = - STEP if self.aim % 2 == 0 else STEP
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
        return Bullet(copy.deepcopy(self.position), self.aim, self.id)

    
    def is_hit(self, bullet: Bullet) -> bool:
        """
        Checks if the shooters has been hit by a bullet.

        params:
            bullet(Bullet): the bullet :D

        return:
            (bool): true if the shooter got hit.
        """
        bullet_position: Position = bullet.position
        return not self.id == bullet.shooter_id and \
              (((self.position.x <= bullet_position.x and bullet_position.x <= self.position.x + SHOOTER_SIZE) and \
                (self.position.y <= bullet_position.y and bullet_position.y <= self.position.y + SHOOTER_SIZE)) or \
               ((self.position.x <= bullet_position.x and bullet_position.x <= self.position.x + SHOOTER_SIZE) and \
                (self.position.y <= bullet_position.y + BULLET_SIZE and bullet_position.y + BULLET_SIZE <= self.position.y + SHOOTER_SIZE)) or \
               ((self.position.x <= bullet_position.x + BULLET_SIZE and bullet_position.x + BULLET_SIZE <= self.position.x + SHOOTER_SIZE) and \
                (self.position.y <= bullet_position.y and bullet_position.y <= self.position.y + SHOOTER_SIZE)) or \
               ((self.position.x <= bullet_position.x + BULLET_SIZE and bullet_position.x + BULLET_SIZE <= self.position.x + SHOOTER_SIZE) and \
                (self.position.y <= bullet_position.y + BULLET_SIZE and bullet_position.y + BULLET_SIZE <= self.position.y + SHOOTER_SIZE)))