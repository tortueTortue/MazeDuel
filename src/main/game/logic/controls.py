from PyQt5.QtCore import Qt
from ...utils.enums.enums import Direction

class Controls:

    def __init__(self, left: Qt.Key, right: Qt.Key, up: Qt.Key, down: Qt.Key, shoot: Qt.Key):
        self.left: Qt.Key = left
        self.right: Qt.Key = right
        self.up: Qt.Key = up
        self.down: Qt.Key = down
        self.shoot: Qt.Key = shoot
        self.keys: (Qt.Key) = (left, right, up, down, shoot)

    def is_key_control(self, key: Qt.Key) -> bool:
        """
        Verifes whether the key belongs to this control
        or not.

        params:
            key(Key): key to check

        return:
            bool: whether the key belongs to the control or not.
        """
        return key in self.keys

    def control_to_direction(self, key: Qt.Key) -> Direction:
        """
        Gives the direction of a key if is one
        of the controls. Else it throws and exception

        params:
            key(Key): key to check
        returns:
            Direction: direction of the move
        """
        if not self.is_key_control(key):
            raise Exception("Not a key of this control config!")

        if self.left == key :
            return Direction.WEST
        elif self.right == key :
            return Direction.EAST
        elif self.up == key :
            return Direction.NORTH
        elif self.down == key :
            return Direction.SOUTH

# D E F A U L T  C O N T R O L S

def get_default_controls() -> (Controls):
    """
    return:
        (Controls): a tuple of the two default controls which are :

        Control 1:            Control 2:      
        up    : w             up    : up arrow
        down  : d             down  : down arrow
        left  : a             left  : left arrow
        right : d             right : right arrow
        shoot : e             shoot : Enter
    """
    return (Controls(Qt.Key.Key_A, Qt.Key.Key_D, Qt.Key.Key_W, Qt.Key.Key_S, Qt.Key.Key_E), 
            Controls(Qt.Key.Key_Left, Qt.Key.Key_Right, Qt.Key.Key_Up, Qt.Key.Key_Down, Qt.Key.Key_P))
