# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\TE\VI\SE\av.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 915)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(360, 30, 431, 87))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setObjectName("title")
        
        self.time_box = QtWidgets.QTextEdit( self.centralwidget)
        self.time_box.setGeometry(QtCore.QRect(210, 150, 118, 22))
        self.time_box.setObjectName("time_box")
        
        self.date_box = QtWidgets.QDateEdit(self.centralwidget)
        self.date_box.setGeometry(QtCore.QRect(40, 150, 110, 22))
        self.date_box.setObjectName("date_box")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(260, 240, 120, 80))
        self.widget.setObjectName("widget")
        
        self.update_box = QtWidgets.QLabel(self.centralwidget)
        self.update_box.setGeometry(QtCore.QRect(750, 440, 321, 141))
        self.update_box.setObjectName("update_box")
        
        self.scan_box = QtWidgets.QLabel(self.centralwidget)
        self.scan_box.setGeometry(QtCore.QRect(10, 440, 321, 141))
        self.scan_box.setObjectName("scan_box")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.timer = QtCore.QTimer(self.time_box)
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect(self.displayTime)
        # self.timer.start()

    


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setImages()

   
        self.timer = QtCore.QTimer(self.time_box)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayDate)
        self.timer.start()
    

    def displayDate(self):
        self.time_box.setText(QtCore.QDateTime.currentDateTime().toString())
      
       
    def setImages(self):
        self.img_scan = QPixmap('scan1.jpg')
        self.img_update = QPixmap('update1.jpg')
        self.img_title = QPixmap('title.jpg')
        self.scan_box.setPixmap(self.img_scan)
        self.update_box.setPixmap(self.img_update)
        self.title.setPixmap(self.img_title)
        self.scan_box.resize(310,140)
        self.update_box.resize(self.update_box.width(), self.update_box.height())
        self.img_scan.scaledToWidth(321)
        self.img_scan.scaledToHeight(144)
        self.img_update.scaledToWidth(321)
        self.img_update.scaledToHeight(144)
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time_box.setText(_translate("MainWindow","time_box"))
        self.title.setText(_translate("MainWindow","title"))
        self.update_box.setText(_translate("MainWindow", "update_box"))
        self.scan_box.setText(_translate("MainWindow", "scan_box"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

