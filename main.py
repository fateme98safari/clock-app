import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import *
from mainwindow import Ui_MainWindow
from mytime import MyTime
# from timerthread import TimerThread


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.timer=QTimer
        self.timer.timeout.connect(self.update_time)
        self.

class StpoWatchThread(QThread):
    signal_show=Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.time=MyTime(0,0,0)
        
    
    def run(self):
        while True:
            self.time.plus()
            self.signal_show.emit(self.time)
            time.sleep(1)

    def reset(self):
         self.time.hour=0
         self.time.minute=0
         self.time.second=0


def start_stopwatch():
        Thread_stopwatch.start()

def stop_stopwatch():
     Thread_stopwatch.terminate()

def reset_stopwatch():
     Thread_stopwatch.reset()

def show_time_stopwatch(time):
     mainwindow.ui.lbl_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")



#TimerThread class------------------------------------------------------------------
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

    
def start_timer():
    Thread_timer.start()

def stop_timer():
    Thread_timer.terminate()

def reset_timer():
    Thread_timer.reset()

def show_time_timer(time):
    mainwindow.ui.lnhour.setText(str(time.hour))
    mainwindow.ui.lnminute.setText(str(time.minute))
    mainwindow.ui.lnsecond.setText(str(time.second))

# if time.hour==0 and time.minute==0 and time.second==0:
#         msg_box=QMessageBox()
#         msg_box.setText("💥Time is out💥")
#         msg_box.exec()

#Alarm Thread class------------------------------------------------------------------





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbl_stopwatch.setText("0:0:0")
        # self.ui.lbl_stopwatch.setText("0:0:0")
        self.ui.pbstart_stopwatch.clicked.connect(start_stopwatch)
        self.ui.pbstop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.pbreset_stopwatch.clicked.connect(reset_stopwatch)
        self.ui.pbstart_timer.clicked.connect(start_timer)
        self.ui.pbstop_timer.clicked.connect(stop_timer)
        self.ui.pbreset_timer.clicked.connect(reset_timer)

    



if __name__=="__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()
  


    Thread_stopwatch=StpoWatchThread()
    Thread_timer=TimerThread()
    Thread_stopwatch.signal_show.connect(show_time_stopwatch)
    Thread_timer.signal_show.connect(show_time_timer)


    app.exec_()