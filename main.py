import sys
import time
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import *
from mainwindow import Ui_MainWindow
from mytime import MyTime
from alarmdatabase import Datebase
# from timerthread import TimerThread


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # self.time_label=QLabel
        self.timer=QTimer
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time=QTime.currentTime()
        time_str=current_time.toString("hh:mm:ss")

        self.time_label.setText(time_str)


def iran_time():
    ...
def  germany_time():
    ...
def USA_time():
    ...


#-----worldclockThread-----------------------------------------------------
# class WorldclockThread(QThread):
#     def __init__(self):
#         super().__init__()
#         self.time=MyTime(0,0,0)
        
    
#     def run(self):
#         # while True:
#         #     self.time.plus()
#         #     self.signal_show.emit(self.time)
#         #     time.sleep(1)
#         ...



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
        # mainwindow.ui.lnhour.textChanged.connect(self.run)
        # mainwindow.ui.lnminute.textChanged.connect(self.run)
        # mainwindow.ui.lnsecond.textChanged.connect(self.run)
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
        self.db=Datebase()
        self.read_from_database()
        self.ui.btn_add_alarm.clicked.connect(self.new_alarm)
        self.ui.lbl_stopwatch.setText("0:0:0")
        self.ui.pbstart_stopwatch.clicked.connect(start_stopwatch)
        self.ui.pbstop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.pbreset_stopwatch.clicked.connect(reset_stopwatch)
        self.ui.pbstart_timer.clicked.connect(start_timer)
        self.ui.pbstop_timer.clicked.connect(stop_timer)
        self.ui.pbreset_timer.clicked.connect(reset_timer)

    def read_from_database(self):
        alarms=self.db.get_alarms()

        for i in range(len(alarms)):
            # new_label=QLabel()
            # new_label_time=QLabel()
            new_lineEdi_title=QLineEdit()
            new_lineEdi_time=QLineEdit()
            new_btn=QPushButton()
            new_btn_edit=QPushButton()
            
            # new_label.setText(alarms[i][1])
            # new_label_time.setText(alarms[i][2])

            new_lineEdi_title.setText(alarms[i][1])
            new_lineEdi_time.setText(alarms[i][2])
            new_btn.setText("❌")
            new_btn_edit.setText("✔")
            new_btn.clicked.connect(partial(self.del_alarm, alarms[i][0]))
            new_btn_edit.clicked.connect(self.notification)
            new_lineEdi_title.textChanged.connect(partial(self.edit_alarm , alarms[i][0]))
            # new_lineEdi_time.textChanged.connect(partial(self.edit_alarm , alarms[i][0]))
            self.ui.gl_alarms.addWidget(new_lineEdi_title , i ,1)
            self.ui.gl_alarms.addWidget(new_btn , i ,2)
            self.ui.gl_alarms.addWidget(new_lineEdi_time , i ,0)
            self.ui.gl_alarms.addWidget(new_btn_edit,i,3)

    def notification(self):
        msg_box=QMessageBox()
        msg_box.setText("update sucssfully")
        msg_box.exec_()




    def new_alarm(self):
        new_title=self.ui.ln_title_alarm.text()
        new_time=self.ui.timeEdit.text()

        feedback=self.db.add_new_alarm(new_title , new_time)

        if feedback==True:
          self.read_from_database()
          self.ui.ln_title_alarm.setText("")
          
        else:
            msg_box=QMessageBox()
            msg_box.setText("مشکل رخ داده است")
            msg_box.exec()
    
    def edit_alarm(self,id,text):
        self.db.edit_alarms(id , text)

    def del_alarm(self,id):
        self.db.remove_alarms(id)



if __name__=="__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()
  

    Thread_stopwatch=StpoWatchThread()
    Thread_timer=TimerThread()
    Thread_worldclock=WorldclockThread()
    Thread_stopwatch.signal_show.connect(show_time_stopwatch)
    Thread_timer.signal_show.connect(show_time_timer)
    # Thread_worldclock.signal_show.connect(show_time_worldclock)

    app.exec_()