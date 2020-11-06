from PyQt5 import QtCore, QtGui, QtWidgets
import Bio
from Bio import Entrez  #  Importar módulo Bio.Entrez 
from Bio import SeqIO   #   Módulo para analisar sequências
from validate_email import validate_email

def checkEmail(self,email):  
    if( validate_email( email )):  
        # self.loginToMethodScreen()
        print(self.email)
        # print("Valid Email")  
    # else:
    # 	self.emailPopUp()
	

def emailPopUp(self):
	self.pop = QMessageBox()
	self.pop.setWindowTitle("Erro")
	self.pop.setText("Por favor, insira um email válido")
	self.pop.setIcon(QMessageBox.Critical)
	self.pop.exec_()