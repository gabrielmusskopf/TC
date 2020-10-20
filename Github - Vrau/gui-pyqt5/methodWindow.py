# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'methodWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        Form.setMaximumSize(QtCore.QSize(500, 400))
        self.methodLabel = QtWidgets.QLabel(Form)
        self.methodLabel.setGeometry(QtCore.QRect(190, 20, 158, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.methodLabel.setFont(font)
        self.methodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.methodLabel.setObjectName("methodLabel")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(40, 70, 431, 271))
        self.toolBox.setObjectName("toolBox")
        self.pesquisar = QtWidgets.QWidget()
        self.pesquisar.setGeometry(QtCore.QRect(0, 0, 431, 217))
        self.pesquisar.setObjectName("pesquisar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pesquisar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.pesquisar)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.nameLine = QtWidgets.QLineEdit(self.frame_2)
        self.nameLine.setObjectName("nameLine")
        self.gridLayout_5.addWidget(self.nameLine, 0, 0, 1, 1)
        self.nameCheck = QtWidgets.QCheckBox(self.frame_2)
        self.nameCheck.setObjectName("nameCheck")
        self.gridLayout_5.addWidget(self.nameCheck, 0, 1, 1, 1)
        self.genLine = QtWidgets.QLineEdit(self.frame_2)
        self.genLine.setObjectName("genLine")
        self.gridLayout_5.addWidget(self.genLine, 1, 0, 1, 1)
        self.genCheck = QtWidgets.QCheckBox(self.frame_2)
        self.genCheck.setObjectName("genCheck")
        self.gridLayout_5.addWidget(self.genCheck, 1, 1, 1, 1)
        self.idLine = QtWidgets.QLineEdit(self.frame_2)
        self.idLine.setObjectName("idLine")
        self.gridLayout_5.addWidget(self.idLine, 2, 0, 1, 1)
        self.idCheck = QtWidgets.QCheckBox(self.frame_2)
        self.idCheck.setObjectName("idCheck")
        self.gridLayout_5.addWidget(self.idCheck, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.toolBox.addItem(self.pesquisar, "")
        self.inserir = QtWidgets.QWidget()
        self.inserir.setGeometry(QtCore.QRect(0, 0, 431, 217))
        self.inserir.setObjectName("inserir")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.inserir)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.inserir)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileName = QtWidgets.QLabel(self.frame)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout.addWidget(self.fileName)
        self.fileLabel = QtWidgets.QLineEdit(self.frame)
        self.fileLabel.setObjectName("fileLabel")
        self.horizontalLayout.addWidget(self.fileLabel)
        self.fileButton = QtWidgets.QPushButton(self.frame)
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout.addWidget(self.fileButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.toolBox.addItem(self.inserir, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.methodLabel.setText(_translate("Form", "Escolha o método"))
        self.nameCheck.setText(_translate("Form", "Nome"))
        self.genCheck.setText(_translate("Form", "Gene"))
        self.idCheck.setText(_translate("Form", "ID"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pesquisar), _translate("Form", "Pesquisar"))
        self.fileName.setText(_translate("Form", "Nome do arquivo"))
        self.fileButton.setText(_translate("Form", "Procurar"))
        self.fileButton.clicked.connect(self.fileBrowser)
        self.toolBox.setItemText(self.toolBox.indexOf(self.inserir), _translate("Form", "Inserir"))

    def fileBrowser(self):
        print ("button pressed")
        self.openDialogBox()

    def openDialogBox(self):
        filename = QFileDialog.getOpenFileName()
        print( filename)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
