
import sys

from queue import Queue

from PyQt5.QtWidgets import QApplication
from ..components.shooters import Shooter
from ..physics.position import Position
from ...utils.enums.enums import Direction
from ...ui.board import Board
from ...tools.tools import set_window_style
from ...utils.constants import *
from ..components.arena import Arena
from .flow_handling_thread import FlowHandlingThread
from .match import Match
from .controls import get_default_controls, Controls

class Game:
    """
    A game is a flow of matches between two shooters represented in the UI.
    """

    def __init__(self):
        controls: (Controls) = get_default_controls()
        self.shooters: (Shooter) = (Shooter(Position(WINDOW_WIDTH/2, WINDOW_HEIGHT - 3*STEP, Direction.NORTH), Direction.NORTH, controls[0]),
                                    Shooter(Position(WINDOW_WIDTH/2, 2*STEP, Direction.SOUTH), Direction.SOUTH, controls[1]))
        self.board = None
        self.thread = None
        self.event_queue = Queue()
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
        self.current_match: Match = None
        sys.exit(app.exec())

        return self.board

    def stuff_to_paint(self) -> tuple:
        """
        Returns the components to be painted of the board
        depending on the state of the game.
        """
        if self.state == TITLE:
            return (Arena(WINDOW_HEIGHT, WINDOW_HEIGHT), "M A Z E  D U E L") 
        elif self.state == PLAYING:
            return (Arena(WINDOW_HEIGHT, WINDOW_HEIGHT), self.shooters[0], self.shooters[1], self.current_match.bullets)
        elif self.state == PAUSED:
            return (Arena(WINDOW_HEIGHT, WINDOW_HEIGHT), f"P A U S E D \n S1 : {self.shooters[0].points} and S2 : {self.shooters[1].points}") # Add score message, with leading player
        elif self.state == GAME_OVER:
            return (Arena(WINDOW_HEIGHT, WINDOW_HEIGHT), self.current_match.conclusion) 

    def start(self, new: bool) -> None:
        """
        Starts a match
        
        params:
            new(bool): if True starts new game
        """
        self.state = PLAYING
        if new: 
            self.__reset_shooter_params()
            self.current_match = Match(None, self.shooters)
        self.__exec_thread()

    def pause(self):
        """
        Pauses the game
        """
        self.state = PAUSED
        self.thread.pause = True  

    def stop(self):
        """
        Stops the game
        """
        self.state = TITLE
        self.board.repaint()

# TODO: Implement maze generator
    def update_game(self, e):
        if e == OVER:
            self.state = GAME_OVER
            self.board.stop_game()
        self.board.repaint()

    def __exec_thread(self) -> None:
        """
        """
        self.thread = FlowHandlingThread(self.event_queue, self.current_match)
        self.thread.change_value.connect(self.update_game)
        self.thread.start()

    def __reset_shooter_params(self) -> None:
        """
        Resets the shooters the their initial positions
        """
        self.shooters[0].position = Position(WINDOW_WIDTH/2, WINDOW_HEIGHT - 3*STEP, Direction.NORTH)
        self.shooters[0].aim = Direction.NORTH
        self.shooters[1].position = Position(WINDOW_WIDTH/2, 2*STEP, Direction.SOUTH)
        self.shooters[1].aim = Direction.SOUTH