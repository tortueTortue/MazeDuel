
import sys

from PyQt5.QtWidgets import QApplication
from src.game.components.shooters import Shooter
from src.game.physics.position import Position
from src.utils.enums.enums import Direction
from src.ui.board import Board

class Game:
    """
    A game is a flow of matches between two shooters represented in the UI.
    """

    def __init__(self):
        self.shooters: (Shooter) = (Shooter(Position(0, 0, Direction.SOUTH), Direction.SOUTH),
                                    Shooter(Position(0, 0, Direction.NORTH), Direction.NORTH))
        
        self.board = Board()

    def launch(self) -> Board:
        """
        Launches a game of
        M A Z E  D U E L
        """
        app = QApplication(sys.argv)
        sys.exit(app.exec())

        return self.board
