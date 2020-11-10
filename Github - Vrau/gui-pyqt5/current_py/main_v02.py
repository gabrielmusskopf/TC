import sys, os
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import  *#QApplication, QMainWindow, QMessageBox, QRunnable
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from validate_email import validate_email
import time

from loginWindow_v04 import *
from methodWindow_v06 import *
from loadingWindow_v01 import *
from resultWindow_v03 import *
from methods import *


PROVISORY_EMAIL = "gabrielgmusskopf@gmail.com"

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress 

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread
    '''
    def __init__(self,identifier, handler,*args, **kwargs):
    	super(Worker,self).__init__()
    	self.identifier = identifier
    	self.handler = handler
    	self.signals = WorkerSignals()



    @pyqtSlot()
    def run(self):

    # Se handler for method_ui -> Pesquisa no Entrez
        print("Thread start")
        # print(type(self.handler))
        # print(self.handler )

        if self.identifier == 0: # Arquivo local
        	# print('Sou tipo str. Vai para o LocalAlignment')
        	LocalAlignment(self,self.handler)
        	

        elif self.identifier == 1:	# Arquivo web
        	# print("Sou method_ui. Vai para o WebAlignment")
        	self.resultSearch = Search(self,self.handler,PROVISORY_EMAIL) # Busca no banco de dados
        	WebAlignment(self,self.resultSearch) # Realiza o alinhamento dessa busca
        	print(self.resultSearch["IdList"])

        	self.signals.result.emit(self.resultSearch)


        print("Thread complete")

    #     self.tst()

    # def searchLocalThread(self):
    # 	print("Entrei tst()")



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

		# self.threadpool = QThreadPool()
		# print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

		# Quando botão é clicado, vai para a função fileBrowser()
		self.method_ui.fileButton.clicked.connect(self.fileBrowser)
		# Quando botão de pesquisar, verifica se a pesquisa é válida
		self.method_ui.searchButton.clicked.connect(self.isValidSearch)


	def fileBrowser(self):
		self.file_return = OpenDialogBox(self,self.method_ui) # Retorna só o ID
		# self.method_ui.fileEdit.setText(self.file_return.path)

		if self.file_return != "None":
			# print(self.file_return)
			self.method_ui.insertButton.clicked.connect(self.localAlignment)
			# Alignment(self,self.method_ui)

	def localAlignment(self):
		self.methodToLoadingScreen()
		self.backgroundSearch(0,self.file_return)
		# LocalAlignment(self,self.file_return)

		# self.ldngScrn.multiTrheadSearch(self.file_return)
		# Função para fazer o alinhameto 


	def isValidSearch(self):
		self.valid=IsValidSearch(self,self.method_ui)
		if self.valid:
			self.methodToLoadingScreen()
			self.backgroundSearch(1,self.method_ui)

			# worker = Worker(self.method_ui)
			# worker.signals.result.connect(self.print_output)
			# self.threadpool.start(worker)


	# def print_output(self, s):
 #   		print(s)

 #   		if s["IdList"] != []:
 #   			self.ldngScrn.loadingToResultWindow()


	def methodToLoadingScreen(self):
		# self.loadingFlag = True
		self.close()
		self.ldngScrn.show()
		# self.backgroundSearch()

	def backgroundSearch(self,identifier, handler): 
	# Handler pode ser 
	# self.method_ui, caso seja pesquisa web, ou
	# self.file_return, caso seja arquivo local

		self.ldngScrn.multiTrheadSearch(identifier, handler)

		# LoadingPopUp()





class loadingScreen(QMainWindow):
	def __init__(self,methodObject):
		super().__init__()
		self.loading_ui = Ui_LoadingWindow()
		self.loading_ui.setupUi(self)

		# self.mthd = methodObject
		self.rsltScrn = resultScreen(methodObject)

		self.threadpool = QThreadPool()
		# print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())


	def multiTrheadSearch(self, identifier, handler):

		print("Entrei multiTrheadSearch")

		worker = Worker(identifier, handler)
		# worker.tst()
		worker.signals.result.connect(self.print_output)
		self.threadpool.start(worker)


	def print_output(self, s):
   		print(s)

   		if s["IdList"] != []:
   			self.loadingToResultWindow()


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

		# self.result_ui.resultTree.setText("Texto")
		# self.result_ui.resultTree.setPixmap(QtGui.QPixmap("C:/Usersfabri_000/Documents/_Pesquisas TCC/Bioinformática Python/gui-pyqt5/images/dna.png"))
		
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