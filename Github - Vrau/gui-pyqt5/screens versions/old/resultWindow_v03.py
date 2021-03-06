# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultWindow_v03.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(633, 600)
        self.centralwidget = QtWidgets.QWidget(ResultWindow)
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
        self.tabWidget.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.tabWidget.setObjectName("tabWidget")
        self.treeTab = QtWidgets.QWidget()
        self.treeTab.setObjectName("treeTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.treeTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.resultTree = QtWidgets.QLabel(self.treeTab)
        self.resultTree.setText("")
        self.resultTree.setObjectName("resultTree")
        self.gridLayout_2.addWidget(self.resultTree, 0, 0, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.treeTab)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 2, 1, 1)
        self.tabWidget.addTab(self.treeTab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.result_image = QtWidgets.QLabel(self.frame_2)
        self.result_image.setText("")
        self.result_image.setObjectName("result_image")
        self.verticalLayout_2.addWidget(self.result_image)
        self.returnButton = QtWidgets.QPushButton(self.frame_2)
        self.returnButton.setObjectName("returnButton")
        self.verticalLayout_2.addWidget(self.returnButton)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        ResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResultWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "MainWindow"))
        self.label.setText(_translate("ResultWindow", "Resultados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.treeTab), _translate("ResultWindow", "Árvore Filogenética"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ResultWindow", "Tab 2"))
        self.returnButton.setText(_translate("ResultWindow", "Retornar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultWindow()
    ui.setupUi(ResultWindow)
    ResultWindow.show()
    sys.exit(app.exec_())
