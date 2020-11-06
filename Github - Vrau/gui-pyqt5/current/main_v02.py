import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from validate_email import validate_email

from loginWindow_v04 import *
from methodWindow_v06 import *
from methods import *



class loginScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.login_ui = Ui_LoginWindow()
		self.login_ui.setupUi(self)
		# Instância da classe methodScreen
		self.mthdScrn = methodScreen(self.login_ui.emailEdit.text())
		# Quando botão de login for clicado, conecta o SINAL ao SLOT
		self.login_ui.okButton.clicked.connect(self.checkEmail)


	def checkEmail(self):  
	    self.ans = CheckEmail(self.login_ui.emailEdit.text())
	    if self.ans == 1:
	    	self.loginToMethodScreen()


	def loginToMethodScreen(self):
		self.mthdScrn.show()
		self.close()


class methodScreen(QMainWindow):
	def __init__(self, email):
		super().__init__()
		self.method_ui = Ui_MethodWindow()
		self.method_ui.setupUi(self)

		# Quando botão é clicado, vai para a função fileBrowser()
		self.method_ui.fileButton.clicked.connect(self.fileBrowser)
		# Quando botão de pesquisar, verifica se a pesquisa é válida
		self.method_ui.searchButton.clicked.connect(self.isValidSearch)
		# self.insertButton.clicked.connect(self.witchMethod)


	def fileBrowser(self):
		OpenDialogBox(self,self.method_ui)

	def isValidSearch(self):
		IsValidSearch(self,self.method_ui)



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