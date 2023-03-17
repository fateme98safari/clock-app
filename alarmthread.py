import time
from PySide6.QtCore import *
from mytime import MyTime

class AlarmThread(QThread):
    signal_show=Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.time=MyTime(0,15,30)

    def run(self):
        while True:
            self.time.minus()
            self.signal_show.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.second=30
        self.time.minute=15
        self.time.hour=0

    
def start_timer():
    Thread_timer.start()

def stop_timer():
    Thread_timer.terminate()

def reset_timer():
    Thread_timer.reset()