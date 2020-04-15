__author__ = "David Latortue"

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QEvent
from queue import Queue
# from player import Player
from ..game.physics.position import Position
import copy
import sys
import time
from ..utils.constants import *
from ..utils.enums.enums import Direction
# from ..game.logic.game import Game
from ..game.components.arena import Arena
from ..game.components.shooters import Shooter

class Board(QMainWindow):

    def __init__(self, game):
        super().__init__()
        
        self.title = "Bike race"
        self.top = 100
        self.left = 200
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.control_p2 = True
        self.init_buttons()
        self.init_window()
        self.init_scoreboard()
        self.installEventFilter(self)
        self.setFocusPolicy(Qt.NoFocus)
        self.game = game
        self.show()


    # I N I T  M E T H O D S

    def init_buttons(self):
        start_btn = QPushButton('Start', self)
        pause_btn = QPushButton('Pause', self)
        restart_btn = QPushButton('Restart', self)
        stop_btn = QPushButton('Stop', self)
        start_btn.installEventFilter(self)
        pause_btn.installEventFilter(self)
        restart_btn.installEventFilter(self)
        stop_btn.installEventFilter(self)
        start_btn.move(0, 30)
        restart_btn.move(0, 60)
        stop_btn.move(0, 90)
        start_btn.clicked.connect(self.startGame)
        pause_btn.clicked.connect(self.pauseGame)
        restart_btn.clicked.connect(self.restartGame)
        stop_btn.clicked.connect(self.endGame)
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
            # TODO : Refactor as handle painting comp or some 
            if isinstance(component_to_paint, Arena):
                self.__draw_frame(board, component_to_paint)
            elif isinstance(component_to_paint, Shooter):
                self.__draw_shooter(board, component_to_paint)
            elif isinstance(component_to_paint, str):
                self.__draw_title(board, e, component_to_paint)

            self.__clear_painting_tools(board)
        # if self.game_status == GAME_STARTED :
        #     # TODO : refactor as a function
        #     board.setBrush(QBrush(self.playerOne.get_color(), Qt.SolidPattern))
        #     for pos in self.playerOne.getTraceHistory() :
        #         if Position.is_same_position(pos, self.playerOne.getPostion()) :
        #             board.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        #         board.drawRect(pos.getX(), pos.getY(), PLAYER_DIMENSIONS, PLAYER_DIMENSIONS)
        #     board.setBrush(QBrush(self.playerTwo.get_color(), Qt.SolidPattern))
        #     for pos in self.playerTwo.getTraceHistory() :
        #         if Position.is_same_position(pos, self.playerTwo.getPostion()) :
        #             board.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        #         board.drawRect(pos.getX(), pos.getY(), PLAYER_DIMENSIONS, PLAYER_DIMENSIONS)
        #     self.drawFrame(board)   
        
        # elif self.game_status == GAME_ENDED:
        #     board.drawText(self.height/2, self.width/2, "GAME OVER")
        #     self.btns.get('pause').hide()
        #     self.btns.get('start').show()
        #     self.resetPlayers()
        #     self.update_scoreboard()
        #     self.pickers.get('one').show()
        #     self.pickers.get('two').show()
        #     self.pickers.get('control').show()
        #     self.picker_labels.get('one').show()
        #     self.picker_labels.get('two').show()
        #     self.picker_labels.get('control').show()
        
            

    # TODO : Refactor using same method
    def __draw_frame(self, board: QPainter, frame: Arena) -> None:
        board.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        board.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        board.drawRect(FRAME_X_POS, 0, frame.height, frame.width)

    def __draw_shooter(self, board: QPainter, shooter: Shooter) -> None:
        board.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        board.setPen(QPen(Qt.white, 1, Qt.SolidLine))
        board.drawRect(shooter.position.x, shooter.position.y, SHOOTER_SIZE, SHOOTER_SIZE)
        
    def __draw_title(self, board:QPainter, e, text: str) -> None:
        board.setPen(Qt.white)
        board.setFont(QFont('Ubuntu', 50))
        board.drawText(e.rect(), Qt.AlignCenter, text)
    
    def __clear_painting_tools(self, board: QPainter) -> None:
        board.setPen(QPen(Qt.NoPen))
        board.setBrush(QBrush(Qt.NoBrush))

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if self.control_p2 :
                self.handle_directions(key)
        return super(Board, self).eventFilter(source, event)

    def keyPressEvent(self, event):
        key = event.key()
        self.handle_directions(key)

    def mousePressEvent(self, event):
        self.mouse_x = event.x()
        self.mouse_y = event.y()
        #print("x : " + str(self.mouse_x) + "y : " + str(self.mouse_y))

    def mouseReleaseEvent(self, event):
        # if not self.control_p2 :
        #     x_move = KEY_RIGHT if self.mouse_x < event.x() else KEY_LEFT
        #     y_move = KEY_DOWN if self.mouse_y < event.y() else KEY_UP
        #     move = x_move if Position.is_vertical(self.playerTwo.getPostion()) else y_move
        #     self.handle_directions(move)
        pass
 
    def handle_directions(self, key):
        # if self.game_status == GAME_STARTED or self.game_status == GAME_RESTARTED:
        #     if key == KEY_A and not self.playerOne.getPostion() == WEST:
        #         self.playerOne.getPostion().setDirection(WEST)
        #     elif key == KEY_D and not self.playerOne.getPostion() == EAST:
        #         self.playerOne.getPostion().setDirection(EAST)
        #     elif key == KEY_W and not self.playerOne.getPostion() == NORTH:
        #         self.playerOne.getPostion().setDirection(NORTH)
        #     elif key == KEY_S and not self.playerOne.getPostion() == SOUTH:
        #         self.playerOne.getPostion().setDirection(SOUTH)
        #     elif key == KEY_LEFT and not self.playerTwo.getPostion() == WEST:
        #         self.playerTwo.getPostion().setDirection(WEST)
        #     elif key == KEY_RIGHT and not self.playerTwo.getPostion() == EAST:
        #         self.playerTwo.getPostion().setDirection(EAST)
        #     elif key == KEY_UP and not self.playerTwo.getPostion() == NORTH:
        #         self.playerTwo.getPostion().setDirection(NORTH)
        #     elif key == KEY_DOWN and not self.playerTwo.getPostion() == SOUTH:
        #         self.playerTwo.getPostion().setDirection(SOUTH)
        pass

    def closeEvent(self, event):
        pass

     # A C T I O N  M E T H O D S

    def startGame(self):
        self.event_queue = Queue() # Here put all the inputs to be handled
        self.game.start_game(self.event_queue)
        self.btns.get('pause').show()
        self.btns.get('start').hide()
        

    def restartGame(self):
        # print("Game restarted!")
        # self.event_queue = Queue()
        # self.thread = Control_Thread(self.event_queue, self.playerOne, self.playerTwo)
        # self.thread.change_value.connect(self.updateGame)
        # self.thread.start()
        # self.btns.get('stop').hide()
        # self.btns.get('restart').hide()
        # self.btns.get('pause').show()
        pass

    def pauseGame(self):
        # self.event_queue.put(GAME_PAUSE)
        # self.btns.get('stop').show()
        # self.btns.get('restart').show()
        # self.btns.get('pause').hide()
        pass

    def endGame(self):
        # self.event_queue.put(GAME_ENDED)
        # self.btns.get('stop').hide()
        # self.btns.get('restart').hide()
        # self.btns.get('start').show()
        # self.game_status = GAME_ENDED
        # self.repaint()
        pass

    def is_over(self, trace_history_1, trace_history_2, pos):
        # for pos_i in trace_history_1:
        #     if Position.is_same_position(pos_i, pos) :
        #         return True

        # for pos_i in trace_history_2:
        #     if Position.is_same_position(pos_i, pos) :
        #         return True

        # return self.touching_frame(pos)
        pass

    def updateGame(self, val):
        # if val == GAME_STARTED :
        #     two_wins = False
        #     if self.is_over(self.playerOne.getTraceHistory(), self.playerTwo.getTraceHistory(), self.playerOne.getPostion()) :
        #         two_wins = True
        #     if self.is_over(self.playerOne.getTraceHistory(), self.playerTwo.getTraceHistory(), self.playerTwo.getPostion()) :
        #         # Both lost simultaneously
        #         if not two_wins:
        #             self.playerOne.add_point()
        #             self.game_status = GAME_ENDED
        #         else :
        #             self.game_status = GAME_ENDED
        #     else :
        #         if two_wins :
        #             self.playerTwo.add_point()
        #             self.game_status = GAME_ENDED

        #     if self.game_status == GAME_ENDED :
        #         self.playerOne.resetTraceHistory()
        #         self.playerTwo.resetTraceHistory()
        #         self.event_queue.put(GAME_ENDED)
        #     else :
        #         self.playerOne.add_current_pos_to_trace_his()
        #         self.playerTwo.add_current_pos_to_trace_his()

        #     self.repaint()

        # elif val == GAME_PAUSE :
        #     #we'll see
        #     print("paused")
        #     self.repaint()
        pass

    def touching_frame(self, pos):
        return pos.getY() == 0 or pos.getY() == 1000 or pos.getX() == 500 or pos.getX() == 1500