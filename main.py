import sys
import time
import datetime
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import *
from mainwindow import Ui_MainWindow
from mytime import MyTime
from alarmdatabase import Datebase
from alarmthread import AlarmThread
from timerthread import TimerThread
from stopwatchtread import StpoWatchThread



class Worldclockthread_iran(QThread):
    signal_show=Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.now = datetime.datetime.now()
        self.now.time()
        datetime.time()
        hour=self.now.hour
        minute=self.now.minute
        second=self.now.second
        self.time=MyTime(hour,minute,second)
        self.show_time_worldclock(self.time)


    def run(self):
         while True:
            Thread_worldclock.start()
            self.time.plus()
            self.signal_show.emit(self.time)
            time.sleep(1)

    def show_time_worldclock(time):
        mainwindow.ui.lbl_ir_time.setText((f"{time.hour}:{time.minute}:{time.second}"))

    class Worldclockthread_germany(QThread):
        signal_show=Signal(MyTime)
        def __init__(self):
            super().__init__()
            self.now = datetime.datetime.now()
            self.now.time()
            datetime.time()
            hour=self.now.hour
            minute=self.now.minute
            second=self.now.second
            self.time=MyTime(hour,minute,second)
            self.show_time_worldclock(self.time)


        def run(self):
            while True:
                Thread_worldclock.start()
                self.time.convert_ir_to_germany()
                self.signal_show.emit(self.time)
                time.sleep(1)

        def show_time_worldclock(time):
            mainwindow.ui.lbl_gr_time.setText((f"{time.hour}:{time.minute}:{time.second}"))
       
        # mainwindow.ui.label_4.setText(str(time.second))
    #<<<<<<<<<<<<<<<<<Stopwatch Functions>>>>>>>>>>>>>>>

    def start_stopwatch():
            Thread_stopwatch.start()

    def stop_stopwatch():
        Thread_stopwatch.terminate()

    def reset_stopwatch():
        Thread_stopwatch.reset()

    def show_time_stopwatch(time):
        mainwindow.ui.lbl_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")

#<<<<<<<<<<<<<<<<<Timer Functions>>>>>>>>>>>>>>>>>>> 
   
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
            new_btn_edit.clicked.connect(self.msgupdate)
            new_lineEdi_title.textChanged.connect(partial(self.edit_alarm , alarms[i][0]))
            # new_lineEdi_time.textChanged.connect(partial(self.edit_alarm , alarms[i][0]))
            self.ui.gl_alarms.addWidget(new_lineEdi_title , i ,1)
            self.ui.gl_alarms.addWidget(new_btn , i ,2)
            self.ui.gl_alarms.addWidget(new_lineEdi_time , i ,0)
            self.ui.gl_alarms.addWidget(new_btn_edit,i,3)

    def msgupdate(self):
        msg_box=QMessageBox()
        msg_box.setText("update successfully")
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
    Thread_worldclock=Worldclockthread_iran()
    Thread_worldclock=Worldclockthread_germany()
    Thread_worldclock=Worldclockthread_usa()
    Thread_alarm=AlarmThread()
    Thread_stopwatch.signal_show.connect(show_time_stopwatch)
    Thread_timer.signal_show.connect(show_time_timer)
    Thread_worldclock.signal_show.connect(show_time_worldclock)

    app.exec_()