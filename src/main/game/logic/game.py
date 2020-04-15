
import sys

from PyQt5.QtWidgets import QApplication
from ..components.shooters import Shooter
from ..physics.position import Position
from ...utils.enums.enums import Direction
from ...ui.board import Board
from ...tools.tools import set_window_style
from ...utils.constants import *
from ..components.arena import Arena

class Game:
    """
    A game is a flow of matches between two shooters represented in the UI.
    """

    def __init__(self):
        self.shooters: (Shooter) = (Shooter(Position(WINDOW_WIDTH/2, WINDOW_HEIGHT - 2*STEP, Direction.SOUTH), Direction.SOUTH),
                                    Shooter(Position(WINDOW_WIDTH/2, STEP, Direction.NORTH), Direction.NORTH))
        self.board = None
        # self.state: int = PLAYING # TODO : Temp
        self.state: int = TITLE

    def launch(self) -> Board:
        """
        Launches a game of
        M A Z E  D U E L
        """
        print("launch")
        app = QApplication(sys.argv)
        set_window_style(app)
        self.board = Board(self) # TODO: Find another solution, too much coupling
        sys.exit(app.exec())

        return self.board

    def stuff_to_paint(self) -> tuple:
        """
        Returns the components to be painted of the board
        depending on the state of the game.
        """
        if self.state == TITLE:
            return (Arena(WINDOW_HEIGHT, WINDOW_HEIGHT), "M A Z E  D U E L") # Add statring message
        elif self.state == PLAYING:
            return (Arena(WINDOW_HEIGHT, WINDOW_HEIGHT), self.shooters[0], self.shooters[1])
        elif self.state == PAUSE:
            return (Arena(WINDOW_HEIGHT, WINDOW_HEIGHT), Arena(WINDOW_HEIGHT, WINDOW_HEIGHT)) # Add score message, with leading player
