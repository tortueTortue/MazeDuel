
from ..physics.position import Position
from ..physics.position import is_vertical
from ...utils.enums.enums import Direction


class Wall:

    def __init__(self, position: Position, length: int, orientation: Direction) :
        self.position: Position = position
        self.length: int = length
        self.orientation: Direction = orientation

    def touching(self, position: Position) -> bool:
        """
        """
        if is_vertical(self.orientation):
            return self.position.x - 5 <= position.x and position.x <= self.position.x + 5 and \
                   self.position.y <= position.y and position.y <= self.position.y + self.length
        else :
            return self.position.y - 5 <= position.y and position.y <= self.position.y + 5 and \
                   self.position.x <= position.x and position.x <= self.position.x + self.length