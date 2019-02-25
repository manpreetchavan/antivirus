# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\TE\VI\SE\av.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 915)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QTextEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(360, 30, 431, 87))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setObjectName("title")
        self.time_box = QtWidgets.QTimeEdit(self.centralwidget)
        self.time_box.setGeometry(QtCore.QRect(210, 150, 118, 22))
        self.time_box.setObjectName("time_box")
        self.date_box = QtWidgets.QDateEdit(self.centralwidget)
        self.date_box.setGeometry(QtCore.QRect(40, 150, 110, 22))
        self.date_box.setObjectName("date_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 420, 291, 151))
        self.label.setObjectName("label")
        self.update_box = QtWidgets.QLabel(self.centralwidget)
        self.update_box.setGeometry(QtCore.QRect(750, 430, 321, 141))
        self.update_box.setObjectName("update_box")
        self.scan_box = QtWidgets.QLabel(self.centralwidget)
        self.scan_box.setGeometry(QtCore.QRect(370, 430, 311, 141))
        self.scan_box.setObjectName("scan_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">WELCOME TO AV ANTIVIRUS</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
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

