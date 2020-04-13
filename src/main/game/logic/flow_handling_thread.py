

from PyQt5.QtCore import QThread, pyqtSignal
from ...utils.constants import *
import time

class FlowHandlingThread(QThread):

    def __init__(self, queue, playerOne, playerTwo, parent=None):
        self.event_queue = queue
        self.pause = False
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.level = SPEED
        super(FlowHandlingThread, self).__init__(parent=parent)

    change_value = pyqtSignal(int)
    def run(self):
        cnt = 0
        while not self.pause:
            if not self.event_queue.empty():
                event = self.event_queue.get()
                if event == config.GAME_PAUSE :
                    self.pause = True
                    break
                elif event == config.GAME_ENDED :
                    break
            time.sleep(self.level)
            self.playerOne.move()
            self.playerTwo.move()
            self.change_value.emit(config.GAME_STARTED)
            cnt += 1
            self.level_update(cnt)
            print("...")
        self.exit()

    def level_update(self, cnt):
        if cnt == 10:
            self.level = config.LEVEL_2
        elif cnt == 22:
            self.level = config.LEVEL_3
        elif cnt == 38:
            self.level = config.LEVEL_4
        elif cnt == 63:
            self.level = config.LEVEL_5
        elif cnt == 113:
            self.level = config.LEVEL_6
        elif cnt == 213:
            self.level = config.LEVEL_7