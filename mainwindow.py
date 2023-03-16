# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(615, 416)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(100, 10, 441, 301))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 40, 151, 51))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 60, 321, 101))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.pbstart_stopwatch = QPushButton(self.tab_3)
        self.pbstart_stopwatch.setObjectName(u"pbstart_stopwatch")
        self.pbstart_stopwatch.setGeometry(QRect(110, 210, 75, 24))
        self.pbreset_stopwatch = QPushButton(self.tab_3)
        self.pbreset_stopwatch.setObjectName(u"pbreset_stopwatch")
        self.pbreset_stopwatch.setGeometry(QRect(200, 210, 75, 24))
        self.pbstop_stopwatch = QPushButton(self.tab_3)
        self.pbstop_stopwatch.setObjectName(u"pbstop_stopwatch")
        self.pbstop_stopwatch.setGeometry(QRect(290, 210, 75, 24))
        self.lbl_stopwatch = QLabel(self.tab_3)
        self.lbl_stopwatch.setObjectName(u"lbl_stopwatch")
        self.lbl_stopwatch.setGeometry(QRect(150, 60, 171, 91))
        font = QFont()
        font.setFamilies([u"Seven Segment"])
        font.setPointSize(46)
        self.lbl_stopwatch.setFont(font)
        self.lbl_stopwatch.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.lnhour = QLineEdit(self.tab_4)
        self.lnhour.setObjectName(u"lnhour")
        self.lnhour.setGeometry(QRect(63, 50, 102, 99))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnhour.sizePolicy().hasHeightForWidth())
        self.lnhour.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Seven Segment"])
        font1.setPointSize(54)
        self.lnhour.setFont(font1)
        self.lnhour.setStyleSheet(u"color: rgb(255, 0, 127);")
        self.lnhour.setAlignment(Qt.AlignCenter)
        self.lnminute = QLineEdit(self.tab_4)
        self.lnminute.setObjectName(u"lnminute")
        self.lnminute.setGeometry(QRect(171, 50, 103, 99))
        sizePolicy.setHeightForWidth(self.lnminute.sizePolicy().hasHeightForWidth())
        self.lnminute.setSizePolicy(sizePolicy)
        self.lnminute.setFont(font1)
        self.lnminute.setStyleSheet(u"color: rgb(255, 0, 127);")
        self.lnminute.setAlignment(Qt.AlignCenter)
        self.lnsecond = QLineEdit(self.tab_4)
        self.lnsecond.setObjectName(u"lnsecond")
        self.lnsecond.setGeometry(QRect(280, 50, 102, 99))
        sizePolicy.setHeightForWidth(self.lnsecond.sizePolicy().hasHeightForWidth())
        self.lnsecond.setSizePolicy(sizePolicy)
        self.lnsecond.setFont(font1)
        self.lnsecond.setStyleSheet(u"color: rgb(255, 0, 127);")
        self.lnsecond.setAlignment(Qt.AlignCenter)
        self.pbreset_timer = QPushButton(self.tab_4)
        self.pbreset_timer.setObjectName(u"pbreset_timer")
        self.pbreset_timer.setGeometry(QRect(180, 180, 75, 24))
        self.pbstop_timer = QPushButton(self.tab_4)
        self.pbstop_timer.setObjectName(u"pbstop_timer")
        self.pbstop_timer.setGeometry(QRect(270, 180, 75, 24))
        self.pbstart_timer = QPushButton(self.tab_4)
        self.pbstart_timer.setObjectName(u"pbstart_timer")
        self.pbstart_timer.setGeometry(QRect(90, 180, 75, 24))
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 615, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.BottomToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.pbstart_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pbreset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pbstop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.lbl_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.lnhour.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lnminute.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.lnsecond.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.pbreset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pbstop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pbstart_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

