import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from validate_email import validate_email

from loginWindow_v04 import *
from methodWindow_v06 import *
from loadingWindow_v01 import *
from resultWindow_v02 import *
from methods import *


PROVISORY_EMAIL = "gabrielgmusskopf@gmail.com"


class loginScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.login_ui = Ui_LoginWindow()
		self.login_ui.setupUi(self)
		# Instância da classe methodScreen

		# self.mthdScrn = methodScreen(self.login_ui.emailEdit.text())
		self.mthdScrn = methodScreen(PROVISORY_EMAIL)

		# Quando botão de login for clicado, conecta o SINAL ao SLOT
		self.login_ui.okButton.clicked.connect(self.checkEmail)


	def checkEmail(self):  
	    self.isValid = CheckEmail(self.login_ui.emailEdit.text())
	    if self.isValid:
	    	self.loginToMethodScreen()



	def loginToMethodScreen(self):
		self.mthdScrn.show()
		self.close()
 

class methodScreen(QMainWindow):
	def __init__(self, email):
		super().__init__()
		self.email = email
		self.method_ui = Ui_MethodWindow()
		self.method_ui.setupUi(self)

		self.ldngScrn = loadingScreen(self)

		# Quando botão é clicado, vai para a função fileBrowser()
		self.method_ui.fileButton.clicked.connect(self.fileBrowser)
		# Quando botão de pesquisar, verifica se a pesquisa é válida
		self.method_ui.searchButton.clicked.connect(self.isValidSearch)


	def fileBrowser(self):
		self.file_return = OpenDialogBox(self,self.method_ui)

		if self.file_return:
			# print(self.file_return)
			self.method_ui.insertButton.clicked.connect(self.alignmentLocal)
			# Alignment(self,self.method_ui)

	def alignmentLocal(self):
		self.methodToLoadingScreen()
		ShowPhyloLocal(self,self.file_return)
		pass
		print(self.file_return)
		# Função para fazer o alinhameto 


	def isValidSearch(self):
		self.valid=IsValidSearch(self,self.method_ui)
		if self.valid:
			self.methodToLoadingScreen()
			self.searchResult = Search(self,self.method_ui,self.email)
		
			# print(self.email)
			# print(self.searchResult["Count"])
			# print("ID List: ", self.searchResult["IdList"])
			# print("Term: ", self.searchResult["TranslationStack"])

	def methodToLoadingScreen(self):
		self.ldngScrn.show()
		self.close()
		self.ldngScrn.loadingToResultWindow()



class loadingScreen(QMainWindow):
	def __init__(self,methodObject):
		super().__init__()
		self.loading_ui = Ui_LoadingWindow()
		self.loading_ui.setupUi(self)

		self.rsltScrn = resultScreen(methodObject)


	def loadingToResultWindow(self):
		# print("Ta no resultado, dale!")
		self.close()
		self.rsltScrn.show()



class resultScreen(QMainWindow):
	def __init__(self,methodObject):
		super().__init__()
		self.mthdScrn = methodObject

		self.result_ui = Ui_ResultWindow()
		self.result_ui.setupUi(self)

		# self.mthd = methodScreen("gabrielgmusskopf@gmail.com")
		# self.jorge = loginScreen()

		self.result_ui.returnButton.clicked.connect(self.returnToMethod)
		self.showPhylo()

	def showPhylo(self):
		# ShowPhylo(self,self.result_ui)
		pass

	def returnToMethod(self):
		print("Retona ai mano!")
		self.mthdScrn.show()
		self.close()
		


if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	ui = loginScreen()

	# ui = methodScreen()
	ui.show()
	sys.exit(app.exec_())