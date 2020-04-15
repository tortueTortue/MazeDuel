import time

from queue import Queue

from PyQt5.QtCore import QThread, pyqtSignal
from ...utils.constants import *
from .match import Match

class FlowHandlingThread(QThread):

    def __init__(self, queue, match: Match, parent=None):
        self.match: Match = match
        self.event_queue: Queue = queue
        self.pause = False
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
            self.change_value.emit(1)
            cnt += 1
            print("...")
        self.exit()
