import sys, os
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import  *#QApplication, QMainWindow, QMessageBox, QRunnable
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from validate_email import validate_email


from loginWindow_v04 import *
from methodWindow_v06 import *
from loadingWindow_v01 import *
from resultWindow_v06 import *
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
    def __init__(self,identifier, handler, email,*args, **kwargs):
    	super(Worker,self).__init__()
    	self.identifier = identifier
    	self.handler = handler
    	self.email = email
    	self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
    # Se handler for method_ui -> Pesquisa no Entrez
        print("Thread start")
        # print(type(self.handler))
        # print(self.handler )

        if self.identifier == 0: # Arquivo local
        	# print('Sou tipo str. Vai para o LocalAlignment')
        	self.resultAlignment = LocalAlignment(self,self.handler)
        	

        elif self.identifier == 1:	# Arquivo web
        	# print("Sou method_ui. Vai para o WebAlignment")
        	self.resultSearch = Search(self,self.handler,self.email) # Busca no banco de dados
        	
        	if self.resultSearch["IdList"] != []:
        		self.resultAlignment = WebAlignment(self,self.resultSearch) # Realiza o alinhamento dessa busca

        
        self.signals.result.emit(self.resultAlignment)

        print("Thread complete")



class loginScreen(QMainWindow):
	def __init__(self):
		super().__init__()


		self.login_ui = Ui_LoginWindow()
		self.login_ui.setupUi(self)

		
		os.chdir('../images')
		self.login_ui.movie = QMovie(os.getcwd() + "/dna02-unscreen.gif")
		os.chdir('../current_py')
		self.login_ui.loginLabel_2.setMovie(self.login_ui.movie)
		self.login_ui.movie.setScaledSize(QSize(100,100))
		self.login_ui.movie.start()


		# self.login_ui.label = QLabel(self)
		# os.chdir('../images')
		# self.login_ui.loginLabel_2.setPixmap(QPixmap(os.getcwd()+'/v2.png'))
		# os.chdir('../current_py')

		# # self.login_ui.loginLabel_2.setScaledContents(False)
		# self.login_ui.loginLabel_2.scaled(QSize(200,200))

		# self.login_ui.loginLabel_2.resize(self.login_ui.loginLabel_2.width(), self.login_ui.loginLabel_2.height())

		# self.doAnimation()


		# Instância da classe methodScreen
		self.mthdScrn = methodScreen(self.login_ui.emailEdit.text())
		# print(self.login_ui.emailEdit.text())
		#
		# self.mthdScrn = methodScreen(PROVISORY_EMAIL)

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
		self.method_ui.insertButton.clicked.connect(self.fileBrowser)
		# Quando botão de pesquisar, verifica se a pesquisa é válida
		self.method_ui.searchButton.clicked.connect(self.isValidSearch)


	def fileBrowser(self):
		self.file_return = OpenDialogBox(self,self.method_ui) # Retorna só o ID
	


	def isValidSearch(self):
		# Verifica se a pesquisa é válida
		# Verifica qual tipo de pesquisa e envia para o backgroundSearch()
		# 0 = Local / 1 = Web

		self.valid=IsValidSearch(self,self.method_ui)	# Retorna um objeto com [Pesquisa Válida, Método de pesquisa]
		if self.valid[0] == 1:
			self.methodToLoadingScreen()
			if self.valid[1] == 1:
				self.backgroundSearch(1,self.method_ui)
			elif self.valid[1] == 0:

				self.backgroundSearch(0,self.method_ui)	



	def methodToLoadingScreen(self):
		# self.loadingFlag = True
		self.close()
		self.ldngScrn.show()
		# self.backgroundSearch()

	def backgroundSearch(self,identifier, handler): 
	# Handler pode ser 
	# self.method_ui, caso seja pesquisa web, ou
	# self.file_return, caso seja arquivo local
		# print(self.email)
		self.ldngScrn.multiTrheadSearch(identifier, handler,self.email)

		# LoadingPopUp()



class loadingScreen(QMainWindow):
	def __init__(self,methodObject):
		super().__init__()
		self.loading_ui = Ui_LoadingWindow()
		self.loading_ui.setupUi(self)

		os.chdir('../images')
		self.loading_ui.movie = QMovie( os.getcwd()+ "/dna-unscreen.gif")
		os.chdir('../current_py')
		self.loading_ui.label_2.setMovie(self.loading_ui.movie)
		self.loading_ui.movie.setScaledSize(QSize(200,200))
		self.loading_ui.movie.start()


		self.rsltScrn = resultScreen(methodObject)

		self.threadpool = QThreadPool()
		# print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())


	def multiTrheadSearch(self, identifier, handler, email):

		print("Entrei multiTrheadSearch")

		worker = Worker(identifier, handler, email)
		worker.signals.result.connect(self.shows)
		self.threadpool.start(worker)


	def shows(self, blast_record):
   		# print(blast_record)
   		# ShowAlignments(self, blast_record, self.rsltScrn)
   		print(blast_record)
   		self.rsltScrn.showAlignments(blast_record)
   		self.rsltScrn.showSites(blast_record)
   		self.loadingToResultWindow()


	def loadingToResultWindow(self):
		# print("Ta no resultado, dale!")
		self.close()
		self.rsltScrn.show()
		self.rsltScrn.showPhylo()



class resultScreen(QMainWindow):
	def __init__(self,methodObject):
		super().__init__()

		self.mthdScrn = methodObject

		self.result_ui = Ui_ResultWindow()
		self.result_ui.setupUi(self)

		self.result_ui.returnButton.clicked.connect(self.returnToMethod)
		# self.showPhylo()

	def showAlignments(self, blast_record):
		ShowAlignments(self, blast_record, self.mthdScrn)


	def showSites(self,blast_record):
		ShowSites(self, blast_record, self.mthdScrn)


	def showPhylo(self):
		ShowPhylo(self,self.result_ui)
	

	def returnToMethod(self):
		print("Retona ai mano!")
		self.mthdScrn.method_ui.searchEdit.setText('')
		self.mthdScrn.method_ui.insertEdit.setText('')
		self.mthdScrn.method_ui.sequencesAskLineEdit_2.setText('1')
		self.mthdScrn.show()
		self.close()
		


if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	ui = loginScreen()

	# ui = methodScreen()
	ui.show()
	sys.exit(app.exec_())