from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainwindow import Ui_MainWindow


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel
        self.timer=QTimer
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time=QTime.currentTime()
        time_str=current_time.toString("hh:mm:ss")

        self.time_label.setText(time_str)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__=="__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()

    app.exec_()