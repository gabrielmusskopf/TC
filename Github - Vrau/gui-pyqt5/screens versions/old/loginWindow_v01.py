# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from validate_email import validate_email




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 270, 291, 51))
        self.lineEdit.setObjectName("lineEdit")


        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setGeometry(QtCore.QRect(180, 210, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginLabel.setFont(font)
        self.loginLabel.setObjectName("loginLabel")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 360, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check)


        self.dnaPhoto = QtWidgets.QLabel(self.centralwidget)
        self.dnaPhoto.setGeometry(QtCore.QRect(140, 60, 331, 121))
        self.dnaPhoto.setText("")
        self.dnaPhoto.setPixmap(QtGui.QPixmap("images/dna03.png"))
        self.dnaPhoto.setObjectName("dnaPhoto")


        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 20))
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
        self.loginLabel.setText(_translate("MainWindow", "Insira seu e-mail"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def check(self,email):  
        # print("Check")
        # print(self.lineEdit.text())

        if( validate_email( self.lineEdit.text() )):  
            print("Valid Email")  
        else:  
            print("Invalid Email") 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())