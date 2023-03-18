import time
from PySide6.QtCore import *
from mytime import MyTime

class TimerThread(QThread):
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

    

# def show_time_timer(time):
#     mainwindow.ui.lnhour.setText(str(time.hour))
#     mainwindow.ui.lnminute.setText(str(time.minute))
#     mainwindow.ui.lnsecond.setText(str(time.second))

