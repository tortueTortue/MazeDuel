__author__ = "David Latortue"

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont, QColor
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QEvent
from queue import Queue

import copy
import sys
import time

from ..utils.constants import *
from ..utils.enums.enums import Direction
from ..game.physics.position import Position
from ..game.components.arena import Arena
from ..game.components.shooters import Shooter
from ..game.components.bullets import Bullet

class Board(QMainWindow):

    def __init__(self, game):
        super().__init__()
        
        self.title = "M A Z E  D U E L"
        self.top = 100
        self.left = 200
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.control_p2 = True
        self.init_buttons()
        self.init_window()
        self.init_scoreboard()
        self.setFocusPolicy(Qt.NoFocus) # TODO :TO REMOVE
        self.game = game
        self.event_queue = game.event_queue # Here put all the inputs to be handled
        self.show()

    # I N I T  M E T H O D S

    def init_buttons(self):
        start_btn = QPushButton('Start', self)
        pause_btn = QPushButton('Pause', self)
        restart_btn = QPushButton('Restart', self)
        stop_btn = QPushButton('Stop', self)
        pause_btn.installEventFilter(self)
        restart_btn.installEventFilter(self)
        stop_btn.installEventFilter(self)
        stop_btn.move(0, 30)
        start_btn.clicked.connect(self.start_game)
        pause_btn.clicked.connect(self.pause_game)
        restart_btn.clicked.connect(self.restart_game)
        stop_btn.clicked.connect(self.stop_game)
        pause_btn.hide()
        restart_btn.hide()
        stop_btn.hide()
        self.btns = {'start' : start_btn, 'pause' : pause_btn, 'restart' : restart_btn,'stop' : stop_btn}
  

    def init_scoreboard(self):
        pass

    def update_scoreboard(self):
        pass

    def init_window(self):
        #TODO: Fix that
        #self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.show()

    def resetPlayers(self):
        pass

    def paintEvent(self, e):
        board = QPainter(self)
        self.setFocusPolicy(Qt.NoFocus)
        for component_to_paint in self.game.stuff_to_paint():
            # TODO : Refactor as handle painting comp or some , add method where you pass class as argument
            if isinstance(component_to_paint, Arena):
                self.__draw_frame(board, component_to_paint)
            elif isinstance(component_to_paint, Shooter):
                self.__draw_shooter(board, component_to_paint)
            elif isinstance(component_to_paint, str):
                self.__draw_title(board, e, component_to_paint)
            elif isinstance(component_to_paint, list):
                self.__draw_bullets(board, component_to_paint)
            self.__clear_painting_tools(board)           

    # TODO : Refactor using same method
    def __draw_frame(self, board: QPainter, frame: Arena) -> None:
        board.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        board.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        board.drawRect(FRAME_X_POS, 0, frame.height, frame.width)

    def __draw_shooter(self, board: QPainter, shooter: Shooter) -> None:
        board.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        board.setPen(QPen(Qt.white, 1, Qt.SolidLine))
        board.drawRect(shooter.position.x, shooter.position.y, SHOOTER_SIZE, SHOOTER_SIZE)
    
    def __draw_bullets(self, board: QPainter, bullets: list):
        for bullet in bullets:
            board.setBrush(QBrush(QColor(15, 215, 255), Qt.SolidPattern))
            board.setPen(QPen(QColor(15, 215, 255), 1, Qt.SolidLine))
            board.drawRect(bullet.position.x, bullet.position.y, BULLET_SIZE, BULLET_SIZE)

    def __draw_title(self, board:QPainter, e, text: str) -> None:
        board.setPen(Qt.white)
        board.setFont(QFont('Ubuntu', 50))
        board.drawText(e.rect(), Qt.AlignCenter, text)
    
    def __clear_painting_tools(self, board: QPainter) -> None:
        board.setPen(QPen(Qt.NoPen))
        board.setBrush(QBrush(Qt.NoBrush))

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            self.event_queue.put((event.key(), ""))

        return super(Board, self).eventFilter(source, event)


     # A C T I O N  M E T H O D S

    def start_game(self):
        self.game.start(new=True)
        self.btns.get('pause').show()
        self.btns.get('start').hide()
        

    def restart_game(self):
        self.game.start(new=False)
        self.btns.get('stop').hide()
        self.btns.get('restart').hide()
        self.btns.get('pause').show()

    def pause_game(self):
        self.game.pause()
        self.btns.get('stop').show()
        self.btns.get('restart').show()
        self.btns.get('pause').hide()

    def stop_game(self):
        if self.game.state != GAME_OVER:
            self.game.stop()
        self.btns.get('stop').hide()
        self.btns.get('restart').hide()
        self.btns.get('pause').hide()
        self.btns.get('start').show()
        