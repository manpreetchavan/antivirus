# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\TE\VI\SE\av.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import home
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTableWidget, QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


class Ui_UpdateWindow(object):
    def setupUi(self, UpdateWindow):
        UpdateWindow.setObjectName("UpdateWindow")
        UpdateWindow.resize(1115, 915)
        self.centralwidget = QtWidgets.QWidget(UpdateWindow)
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


        
        UpdateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UpdateWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        
        UpdateWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UpdateWindow)
        self.statusbar.setObjectName("statusbar")
        UpdateWindow.setStatusBar(self.statusbar)

        # self.timer = QtCore.QTimer(self.time_box)
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect(self.displayTime)
        # self.timer.start()

    


        self.retranslateUi(UpdateWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateWindow)

        self.setImages()
   
        self.timer = QtCore.QTimer(self.time_box)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayDate)
        self.timer.start()
    

    def displayDate(self):
        self.time_box.setText(QtCore.QDateTime.currentDateTime().toString())
      
       
    def setImages(self):
       
        self.img_title = QPixmap('update.jpg')
        self.title.setPixmap(self.img_title)
        self.title.resize(310,140)
        self.img_title.scaledToWidth(431)
        self.img_title.scaledToHeight(87)

    



    def retranslateUi(self, UpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateWindow.setWindowTitle(_translate("UpdateWindow", "UpdateWindow"))
        self.time_box.setText(_translate("UpdateWindow","time_box"))
        self.title.setText(_translate("UpdateWindow","title"))
       # self.table_box.setTabOrder(_translate("UpdateWindow", "table_box"))
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateWindow = QtWidgets.QMainWindow()
    ui = Ui_UpdateWindow()
    ui.setupUi(UpdateWindow)
    UpdateWindow.show()
    sys.exit(app.exec_())

