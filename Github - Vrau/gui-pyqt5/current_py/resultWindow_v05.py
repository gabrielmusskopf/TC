# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultWindow_v05.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(664, 567)
        self.centralwidget = QtWidgets.QWidget(ResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(30, 30, 30);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_2.setMaximumSize(QtCore.QSize(1200, 700))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgb(40,40,40);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.alignmentTab = QtWidgets.QWidget()
        self.alignmentTab.setObjectName("alignmentTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.alignmentTab)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.alignmentScrollArea = QtWidgets.QScrollArea(self.alignmentTab)
        self.alignmentScrollArea.setStyleSheet("QScrollBar:vertical {\n"
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
        self.alignmentScrollArea.setWidgetResizable(True)
        self.alignmentScrollArea.setObjectName("alignmentScrollArea")
        self.alignmentScrollAreaWidgetContents = QtWidgets.QWidget()
        self.alignmentScrollAreaWidgetContents.setGeometry(QtCore.QRect(-479, 0, 1200, 1200))
        self.alignmentScrollAreaWidgetContents.setObjectName("alignmentScrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.alignmentScrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.alignmentScrollFrame = QtWidgets.QFrame(self.alignmentScrollAreaWidgetContents)
        self.alignmentScrollFrame.setMinimumSize(QtCore.QSize(1200, 1200))
        self.alignmentScrollFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alignmentScrollFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alignmentScrollFrame.setObjectName("alignmentScrollFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.alignmentScrollFrame)
        self.verticalLayout_3.setContentsMargins(12, 9, 9, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.alignmentResultLabel = QtWidgets.QLabel(self.alignmentScrollFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.alignmentResultLabel.setFont(font)
        self.alignmentResultLabel.setStyleSheet("/* Result Label */\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"    border-radius: 5px;\n"
"}")
        self.alignmentResultLabel.setText("")
        self.alignmentResultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.alignmentResultLabel.setObjectName("alignmentResultLabel")
        self.verticalLayout_3.addWidget(self.alignmentResultLabel)
        self.horizontalLayout.addWidget(self.alignmentScrollFrame)
        self.alignmentScrollArea.setWidget(self.alignmentScrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.alignmentScrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.alignmentTab, "")
        self.sitesTab = QtWidgets.QWidget()
        self.sitesTab.setObjectName("sitesTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.sitesTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sitesScrollArea = QtWidgets.QScrollArea(self.sitesTab)
        self.sitesScrollArea.setStyleSheet("QScrollBar:vertical {\n"
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
        self.sitesScrollArea.setWidgetResizable(True)
        self.sitesScrollArea.setObjectName("sitesScrollArea")
        self.sitesScrollAreaWidgetContents = QtWidgets.QWidget()
        self.sitesScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 10000, 1200))
        self.sitesScrollAreaWidgetContents.setObjectName("sitesScrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sitesScrollAreaWidgetContents)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sitesFrame = QtWidgets.QFrame(self.sitesScrollAreaWidgetContents)
        self.sitesFrame.setMinimumSize(QtCore.QSize(1000, 1200))
        self.sitesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sitesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sitesFrame.setObjectName("sitesFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sitesFrame)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sitesResultLabel = QtWidgets.QLabel(self.sitesFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sitesResultLabel.setFont(font)
        self.sitesResultLabel.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"    border-radius: 5px;\n"
"}")
        self.sitesResultLabel.setText("")
        self.sitesResultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.sitesResultLabel.setObjectName("sitesResultLabel")
        self.verticalLayout_4.addWidget(self.sitesResultLabel)
        self.horizontalLayout_3.addWidget(self.sitesFrame)
        self.sitesScrollArea.setWidget(self.sitesScrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.sitesScrollArea)
        self.tabWidget.addTab(self.sitesTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.result_image = QtWidgets.QLabel(self.frame_2)
        self.result_image.setText("")
        self.result_image.setObjectName("result_image")
        self.verticalLayout_2.addWidget(self.result_image)
        self.returnButton = QtWidgets.QPushButton(self.frame_2)
        self.returnButton.setMinimumSize(QtCore.QSize(100, 20))
        self.returnButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.returnButton.setObjectName("returnButton")
        self.verticalLayout_2.addWidget(self.returnButton)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame)
        ResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResultWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "MainWindow"))
        self.label.setText(_translate("ResultWindow", "Resultados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alignmentTab), _translate("ResultWindow", "Alinhamento"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sitesTab), _translate("ResultWindow", "Sítios"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ResultWindow", "Árvore Filogenética"))
        self.returnButton.setText(_translate("ResultWindow", "Retornar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultWindow()
    ui.setupUi(ResultWindow)
    ResultWindow.show()
    sys.exit(app.exec_())
