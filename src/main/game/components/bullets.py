from ..physics.position import Position
from ...utils.enums.enums import Direction

class Bullet:
    """
    Projectile deadly for shooters.
    """

    def __init__(self, position: Position, direction: Direction):
        self.position = position
        self.direction = direction