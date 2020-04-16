from PyQt5.QtCore import Qt

from .maze_producer import Maze
from ..physics.position import Position
from ..components.shooters import Shooter

class Match:
    """
    A match represent one duel in one particular maze between
    two shooters which ends either a win of one of the shooters
    or a tie.
    """

    def __init__(self, maze: Maze, shooters: (Shooter)):
        self.maze = maze
        self.shooters: (Shooter) = shooters
        self.bullets = None
        print("Key"+str(self.shooters[0].controls.left))

    def handle_key_pressed(self, key: Qt.Key) -> None:
        """
        Updates a shooter's state depanding on the key pressed
        by the user.
        params:
            key(Qt.Key): user pressed by a user
        """
        shooter_id: int = None
        if self.shooters[0].controls.is_key_control(key):
            print("Handling key")
            shooter_id = self.shooters[0].id
        elif self.shooters[1].controls.is_key_control(key):
            shooter_id = self.shooters[1].id
        
        if shooter_id :
            if self.shooters[shooter_id].controls.shoot != key : # this means it's a move 
                self.shooters[shooter_id].reorient_aim(key) 
                self.move_shooter(shooter_id)
            else:
                self.shooters[shooter_id].shoot()

    def move_shooter(self, shooter_id: int) -> None:
        """
        Moves the shooters in its aim direction if possible.

        params:
            shooter_id(int): id of the shooter to be moved
        """
        if not self.__unavailable_move(self.shooters[shooter_id].get_next_move()):
            self.shooters[shooter_id].move()

    def __unavailable_move(self, position: Position) -> bool:
        """
        Verify whether a move is legal according to the
        frame of the game and the maze's walls

        params:
            position(Position): position to verify if move
            would be legal or not.

        return:
            bool: whether position is legal or not
        """
        # return self.maze.touches(position)
        return False