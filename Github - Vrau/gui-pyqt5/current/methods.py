from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import Bio
from Bio import Entrez  #  Importar módulo Bio.Entrez 
from Bio import SeqIO   #   Módulo para analisar sequências
from validate_email import validate_email

from main_v02 import *

# Checa se tem formato de email
def CheckEmail(email):  
    # self.email = self.ui.emailEdit.text()
    if( validate_email( email )):  
        print(email)
        return True
        # print("Valid Email")  
    else:
    	print("nop")
    	EmailPopUp()

# Pop up email inválido
def EmailPopUp():
		pop = QMessageBox()
		pop.setWindowTitle("Erro")
		pop.setText("Por favor, insira um email válido")
		pop.setIcon(QMessageBox.Critical)
		pop.exec_()
	

# Janela de pesquisa de arquivo
def OpenDialogBox(self,method_ui):
	# print("abriu")
    self.filename = QFileDialog.getOpenFileName(filter="Fasta files (*.fasta)")
    self.path = self.filename[0]
    method_ui.fileEdit.setText(self.path)

    # print(self.file.read())
    self.file = open(self.path,"r")
    PopResultLocal(self,self.file.read())

# Temporário
# Vai ser substuído pela próxima janela
def PopResultLocal(self,handler):
    pop = QMessageBox()
    pop.setWindowTitle("Resuldados")
    pop.setText(handler)
    pop.setIcon(QMessageBox.Information)
    pop.exec_()


def IsValidSearch(self,method_ui):
    # Verifica se o texto é válido

        if self.method_ui.searchEdit.text() != "":
            # print (self.searchEdit.text())
            search(self,method_ui)
        else:
            print('texto não válido')


def search(self,method_ui):
        self.handle = Entrez.esearch(db="nucleotide", term = self.method_ui.searchEdit.text(), idtype="acc", retmax = 1) 
        self.record = Entrez.read(self.handle) #lendo as infos geradas pela pesquisa
        self.handle.close()

        print (self.handle.url)
        print(self.record["Count"])
        print("ID List: ", self.record["IdList"])
        # print("Term: ", self.record["TranslationStack"])

        if self.record["Count"] == "0" or self.record["IdList"]==[]:
            print ("não encontrado semelhantes")
            popError(self)

        popResultWeb(self)

# Temporário
# Vai ser substuído pela próxima janela
def popResultWeb(self):
        self.pop = QMessageBox()
        self.pop.setWindowTitle("Resuldados")
        self.pop.setText("ID: "+ str(self.record["IdList"]) + "\n"  
            + "URL: " + self.handle.url +"\n"
            +"Número de bases: " + self.record["Count"] +"\n")
        # self.pop.setText(self.record["Count"])
        self.pop.setIcon(QMessageBox.Information)
        self.pop.exec_()

