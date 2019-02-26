# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(582, 406)
        self.scan_now = QtWidgets.QGraphicsView(Dialog)
        self.scan_now.setGeometry(QtCore.QRect(40, 140, 151, 131))
        self.scan_now.setObjectName("scan_now")
        self.update_database = QtWidgets.QGraphicsView(Dialog)
        self.update_database.setGeometry(QtCore.QRect(200, 140, 151, 131))
        self.update_database.setObjectName("update_database")
        self.history = QtWidgets.QGraphicsView(Dialog)
        self.history.setGeometry(QtCore.QRect(360, 140, 151, 131))
        self.history.setObjectName("history")
        self.scanlabel = QtWidgets.QLabel(Dialog)
        self.scanlabel.setGeometry(QtCore.QRect(50, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.scanlabel.setFont(font)
        self.scanlabel.setAutoFillBackground(False)
        self.scanlabel.setObjectName("scanlabel")
        self.updatelabel = QtWidgets.QLabel(Dialog)
        self.updatelabel.setGeometry(QtCore.QRect(210, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.updatelabel.setFont(font)
        self.updatelabel.setObjectName("updatelabel")
        self.historylabel = QtWidgets.QLabel(Dialog)
        self.historylabel.setGeometry(QtCore.QRect(370, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.historylabel.setFont(font)
        self.historylabel.setObjectName("historylabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.scan_now.setToolTip(_translate("Dialog", "<html><head/><body><p>gfhg</p></body></html>"))
        self.scanlabel.setText(_translate("Dialog", "Scan Now"))
        self.updatelabel.setText(_translate("Dialog", "Update"))
        self.historylabel.setText(_translate("Dialog", "History"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
