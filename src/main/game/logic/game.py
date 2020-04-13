
import sys

from PyQt5.QtWidgets import QApplication
from ..components.shooters import Shooter
from ..physics.position import Position
from ...utils.enums.enums import Direction
from ...ui.board import Board

class Game:
    """
    A game is a flow of matches between two shooters represented in the UI.
    """

    def __init__(self):
        self.shooters: (Shooter) = (Shooter(Position(0, 0, Direction.SOUTH), Direction.SOUTH),
                                    Shooter(Position(0, 0, Direction.NORTH), Direction.NORTH))
        self.board = None

    def launch(self) -> Board:
        """
        Launches a game of
        M A Z E  D U E L
        """
        print("launch")
        app = QApplication(sys.argv)
        self.board = Board()
        sys.exit(app.exec())

        return self.board
