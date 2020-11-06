import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from validate_email import validate_email

from loginWindow_v04 import *
from methodWindow_v05 import *
from methods import *



class loginScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_LoginWindow()
		self.ui.setupUi(self)
		# Instância da classe methodScreen
		self.mthdScrn = methodScreen(self.ui.emailEdit.text())
		# Quando botão de login for clicado, conecta o SINAL ao SLOT
		self.ui.okButton.clicked.connect(self.checkEmail)


	def checkEmail(self):  
	    self.email = self.ui.emailEdit.text()
	    if( validate_email( self.email )):  
	        self.loginToMethodScreen()
	        print(self.email)
	        # print("Valid Email")  
	    else:
	    	self.emailPopUp()
	

	def emailPopUp(self):
		self.pop = QMessageBox()
		self.pop.setWindowTitle("Erro")
		self.pop.setText("Por favor, insira um email válido")
		self.pop.setIcon(QMessageBox.Critical)
		self.pop.exec_()


	def loginToMethodScreen(self):
		self.mthdScrn.show()
		self.close()


class methodScreen(QMainWindow):
	def __init__(self, email):
		super().__init__()
		self.ui = Ui_MethodWindow()
		self.ui.setupUi(self)

		# self.lgnScrn = loginScreen()

	def resultPopUp(self):
		pass
		# self.pop = QMessageBox()
		# self.pop.setWindowTitle("Resuldados")
		# self.pop.setText()
		# self.pop.setIcon(QMessageBox.Critical)
		# self.pop.exec_()








if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	ui = loginScreen()

	# ui = methodScreen()
	ui.show()
	sys.exit(app.exec_())