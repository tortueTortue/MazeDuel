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
        self.speed = SPEED
        super(FlowHandlingThread, self).__init__(parent=parent)

    change_value = pyqtSignal(int)
    def run(self):
        while not self.pause and not self.match.conclusion:
            key_events = set()
            while not self.event_queue.empty():
                event = self.event_queue.get()
                # if isinstance(event, QKeyEvent) :
                if isinstance(event, tuple) : # find real issue
                # if isinstance(event, Qt.Key) :
                    if event[0] not in key_events:
                        self.match.handle_key_pressed(event[0])
                        key_events.add(event[0])
                    break

            self.match.handle_bullets()
            if self.match.conclusion:
                self.change_value.emit(OVER)
                break
            time.sleep(self.speed/2)
            if not self.match.conclusion:
                self.match.handle_bullets()
            if self.match.conclusion:
                self.change_value.emit(OVER)
                break
            time.sleep(self.speed/2)
            self.change_value.emit(1)

        self.exit()
