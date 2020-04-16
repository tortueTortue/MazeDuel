import time

from queue import Queue

from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent
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
            while not self.event_queue.empty():
                event = self.event_queue.get()
                # print(f"Event {event.k}")
                # if isinstance(event, QKeyEvent) :
                if isinstance(event, tuple) : # find real issue
                # if isinstance(event, Qt.Key) :
                    self.match.handle_key_pressed(event[0])
                    break
                # elif event == GAME_ENDED :
                #     break
            time.sleep(self.level)
            self.change_value.emit(1)
            cnt += 1
            # print("...")
        self.exit()