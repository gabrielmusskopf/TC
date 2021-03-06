# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'methodWindow_v06.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MethodWindow(object):
    def setupUi(self, MethodWindow):
        MethodWindow.setObjectName("MethodWindow")
        MethodWindow.resize(830, 629)
        self.centralwidget = QtWidgets.QWidget(MethodWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(30, 30, 30);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(800, 800))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgb(40,40,40);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 10))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet("QFrame{\n"
"background-color: rgb(85, 82, 125);\n"
"border-radius: 3px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.methodLabel = QtWidgets.QLabel(self.frame_6)
        self.methodLabel.setMinimumSize(QtCore.QSize(0, 10))
        self.methodLabel.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.methodLabel.setFont(font)
        self.methodLabel.setStyleSheet("color:rgb(235, 235, 235)\n"
"")
        self.methodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.methodLabel.setObjectName("methodLabel")
        self.horizontalLayout_2.addWidget(self.methodLabel)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 738, 518))
        self.scrollAreaWidgetContents_2.setStyleSheet("")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.methodFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.methodFrame.setMinimumSize(QtCore.QSize(0, 500))
        self.methodFrame.setStyleSheet("QFrame{\n"
"    background-color: rgb(76, 76, 76);\n"
"    border-radius: 3px;\n"
"}")
        self.methodFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.methodFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.methodFrame.setObjectName("methodFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.methodFrame)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(40, 9, 40, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.webFrame = QtWidgets.QFrame(self.methodFrame)
        self.webFrame.setMaximumSize(QtCore.QSize(16777215, 300))
        self.webFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.webFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.webFrame.setObjectName("webFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.webFrame)
        self.gridLayout_2.setContentsMargins(9, 9, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.webSearchTitleFrame = QtWidgets.QFrame(self.webFrame)
        self.webSearchTitleFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.webSearchTitleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.webSearchTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.webSearchTitleFrame.setObjectName("webSearchTitleFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.webSearchTitleFrame)
        self.horizontalLayout_8.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.searchLabel_2 = QtWidgets.QLabel(self.webSearchTitleFrame)
        self.searchLabel_2.setMaximumSize(QtCore.QSize(1000, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchLabel_2.setFont(font)
        self.searchLabel_2.setStyleSheet("QLabel{\n"
"    color:rgb(235, 235, 235);\n"
"    background-color: rgb(85, 82, 125);\n"
"    border-radius: 10px;\n"
"}")
        self.searchLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.searchLabel_2.setObjectName("searchLabel_2")
        self.horizontalLayout_8.addWidget(self.searchLabel_2)
        self.gridLayout_2.addWidget(self.webSearchTitleFrame, 0, 0, 1, 1)
        self.searchEdit = QtWidgets.QLineEdit(self.webFrame)
        self.searchEdit.setMinimumSize(QtCore.QSize(0, 160))
        self.searchEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.searchEdit.setFont(font)
        self.searchEdit.setStyleSheet("QLineEdit{\n"
"border-radius: 3px;\n"
"}")
        self.searchEdit.setText("")
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout_2.addWidget(self.searchEdit, 1, 0, 1, 1)
        self.sequencesAskFrame_2 = QtWidgets.QFrame(self.webFrame)
        self.sequencesAskFrame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.sequencesAskFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sequencesAskFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sequencesAskFrame_2.setObjectName("sequencesAskFrame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.sequencesAskFrame_2)
        self.horizontalLayout_9.setContentsMargins(40, 0, 40, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sequencesAskLabel_2 = QtWidgets.QLabel(self.sequencesAskFrame_2)
        self.sequencesAskLabel_2.setMinimumSize(QtCore.QSize(300, 0))
        self.sequencesAskLabel_2.setMaximumSize(QtCore.QSize(400, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sequencesAskLabel_2.setFont(font)
        self.sequencesAskLabel_2.setStyleSheet("color:rgb(235, 235, 235);\n"
"background-color: rgb(85, 82, 125);\n"
"border-radius: 10px;")
        self.sequencesAskLabel_2.setObjectName("sequencesAskLabel_2")
        self.horizontalLayout_9.addWidget(self.sequencesAskLabel_2)
        self.sequencesAskLineEdit_2 = QtWidgets.QLineEdit(self.sequencesAskFrame_2)
        self.sequencesAskLineEdit_2.setText("1")
        self.sequencesAskLineEdit_2.setFont(font)
        self.sequencesAskLineEdit_2.setObjectName("sequencesAskLineEdit_2")
        self.horizontalLayout_9.addWidget(self.sequencesAskLineEdit_2)
        self.gridLayout_2.addWidget(self.sequencesAskFrame_2, 2, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.webFrame)
        self.fileFrame = QtWidgets.QFrame(self.methodFrame)
        self.fileFrame.setMaximumSize(QtCore.QSize(16777215, 130))
        self.fileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileFrame.setObjectName("fileFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.fileFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.fileFrame)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_4.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.searchLabel_3 = QtWidgets.QLabel(self.frame_10)
        self.searchLabel_3.setMaximumSize(QtCore.QSize(1000, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchLabel_3.setFont(font)
        self.searchLabel_3.setStyleSheet("QLabel{\n"
"    color:rgb(235, 235, 235);\n"
"    background-color: rgb(85, 82, 125);\n"
"    border-radius: 10px;\n"
"}")
        self.searchLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.searchLabel_3.setObjectName("searchLabel_3")
        self.gridLayout_4.addWidget(self.searchLabel_3, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_10, 0, 0, 1, 2)
        self.insertEdit = QtWidgets.QLineEdit(self.fileFrame)
        self.insertEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.insertEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.insertEdit.setObjectName("insertEdit")
        self.gridLayout_3.addWidget(self.insertEdit, 1, 0, 1, 1)
        self.insertButton = QtWidgets.QPushButton(self.fileFrame)
        self.insertButton.setMinimumSize(QtCore.QSize(0, 30))
        self.insertButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        self.insertButton.setFont(font)
        self.insertButton.setStyleSheet("QPushButton{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(40,40,40);\n"
"    color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 3px solid rgb(90,90,90);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(80,80,80);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: rgb(255, 245, 140);\n"
"    border-radius: 3px;\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"")
        self.insertButton.setObjectName("insertButton")
        self.gridLayout_3.addWidget(self.insertButton, 1, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.fileFrame)
        self.frame_12 = QtWidgets.QFrame(self.methodFrame)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.frame_12.setFont(font)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.searchButton = QtWidgets.QPushButton(self.frame_12)
        self.searchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.searchButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(40,40,40);\n"
"    color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 3px solid rgb(90,90,90);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(80,80,80);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: rgb(255, 245, 140);\n"
"    border-radius: 3px;\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_10.addWidget(self.searchButton)
        self.verticalLayout_7.addWidget(self.frame_12)
        self.gridLayout.addWidget(self.methodFrame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MethodWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MethodWindow)
        QtCore.QMetaObject.connectSlotsByName(MethodWindow)

    def retranslateUi(self, MethodWindow):
        _translate = QtCore.QCoreApplication.translate
        MethodWindow.setWindowTitle(_translate("MethodWindow", "MainWindow"))
        self.methodLabel.setText(_translate("MethodWindow", "Escolha do método"))
        self.searchLabel_2.setText(_translate("MethodWindow", "Insira o nome, ID ou sequência nucleotídica"))
        self.sequencesAskLabel_2.setText(_translate("MethodWindow", "Com quantas sequências deseja alinhar?"))
        self.searchLabel_3.setText(_translate("MethodWindow", "ou insira um arquivo \".fasta\""))
        self.insertButton.setText(_translate("MethodWindow", "Inserir"))
        self.searchButton.setText(_translate("MethodWindow", "Pesquisar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MethodWindow = QtWidgets.QMainWindow()
    ui = Ui_MethodWindow()
    ui.setupUi(MethodWindow)
    MethodWindow.show()
    sys.exit(app.exec_())
