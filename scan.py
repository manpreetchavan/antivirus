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


class Ui_ScanWindow(object):
    def setupUi(self, ScanWindow):
        ScanWindow.setObjectName("ScanWindow")
        ScanWindow.resize(1115, 915)
        self.centralwidget = QtWidgets.QWidget(ScanWindow)
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

        self.table_box = QtWidgets.QTableWidget(self.centralwidget)
        self.table_box.setGeometry(QtCore.QRect(130, 350, 800, 400))
        self.table_box.setObjectName("table_box")

        
        ScanWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ScanWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        ScanWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ScanWindow)
        self.statusbar.setObjectName("statusbar")
        ScanWindow.setStatusBar(self.statusbar)

        # self.timer = QtCore.QTimer(self.time_box)
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect(self.displayTime)
        # self.timer.start()

    


        self.retranslateUi(ScanWindow)
        QtCore.QMetaObject.connectSlotsByName(ScanWindow)

        self.setImages()
        self.createTable()
   
        self.timer = QtCore.QTimer(self.time_box)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayDate)
        self.timer.start()
    

    def displayDate(self):
        self.time_box.setText(QtCore.QDateTime.currentDateTime().toString())
      
       
    def setImages(self):
       
        self.img_title = QPixmap('scan.jpg')
        self.title.setPixmap(self.img_title)
        self.title.resize(310,140)
        self.img_title.scaledToWidth(431)
        self.img_title.scaledToHeight(87)

       


    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)
        self.tableWidget.show()
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
 
   
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 



    def retranslateUi(self, ScanWindow):
        _translate = QtCore.QCoreApplication.translate
        ScanWindow.setWindowTitle(_translate("ScanWindow", "ScanWindow"))
        self.time_box.setText(_translate("ScanWindow","time_box"))
        self.title.setText(_translate("ScanWindow","title"))
       # self.table_box.setTabOrder(_translate("ScanWindow", "table_box"))
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScanWindow = QtWidgets.QMainWindow()
    ui = Ui_ScanWindow()
    ui.setupUi(ScanWindow)
    ScanWindow.show()
    sys.exit(app.exec_())

