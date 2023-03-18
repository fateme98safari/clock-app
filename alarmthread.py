
from PySide6.QtCore import *
from mytime import MyTime

class AlarmThread(QThread):
    signal_show=Signal(MyTime)
    def __init__(self):
        super().__init__()
      
    