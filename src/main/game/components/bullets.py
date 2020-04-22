from ..physics.position import Position
from ...utils.enums.enums import Direction
from ..physics.position import is_vertical
from ...utils.constants import STEP

class Bullet:
    """
    Projectile deadly for shooters.
    """

    def __init__(self, position: Position, direction: Direction, shooter_id: int):
        self.position: Position = position
        self.direction: Direction = direction
        self.shooter_id: int = shooter_id

    def move(self) -> None:
        """
        Moves bullet towards its direction.
        """
        move: int = -STEP if self.direction % 2 == 0 else STEP
        if is_vertical(self.direction):
            self.position.y += move
        else:
            self.position.x += move