from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import Bio
#   Importar módulo Bio.Entrez 
#   Módulo para analisar sequências
#   Módulo para árvores filogenéticas
from Bio import Entrez, SeqIO, Phylo  
from validate_email import validate_email

from main_v02 import *

# Checa se tem formato de email
def CheckEmail(email):  
    # self.email = self.ui.emailEdit.text()
    if( validate_email( email )):  
        # print(email)
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
    self.filename = QFileDialog.getOpenFileName(filter="Fasta files (*.fasta)")
    self.path = self.filename[0]
    method_ui.fileEdit.setText(self.path)

    # print(self.file.read())
    if self.path != '':
        self.file = open(self.path,"r")
        return self.file.read()
    else:
        return False

    # PopResultLocal(self,self.file.read())

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
        # search(self,method_ui)
        print("Pesquisa Valida")
        return True
    else:
        print('Pesquisa não válida')
        return False


def Search(self,method_ui,email):
    print("Entrou no Search()")
    Entrez.email = email

    self.handle = Entrez.esearch(db="nucleotide", term = self.method_ui.searchEdit.text(), idtype="acc", retmax = 1) 
    self.record = Entrez.read(self.handle) #lendo as infos geradas pela pesquisa
    self.handle.close()

    # print (self.handle.url)
    # print(self.record["Count"])
    print("ID List: ", self.record["IdList"])
    # print("Term: ", self.record["TranslationStack"])

    if self.record["Count"] == "0" or self.record["IdList"]==[]:
        print ("não encontrado semelhantes")
        print("vai criar um popup pra isso!")
        # popError(self)


    # self.tree = Phylo.parse(self.handle, 'phyloxml')
    # Phylo.draw_ascii(self.tree)


    return self.record
    # popResultWeb(self)

def Alignment(self,method_ui):
    # print("Alinhando sequência local")
    self.method_ui.insertButton.clicked.connect()

def ShowPhylo(self,result_ui):
    # self.result_ui.result_image.setPixmap(QtGui.QPixmap("C:/Users/fabri_000/Documents/_Pesquisas TCC/Bioinformática Python/gui-pyqt5/images/dna.png"))
    pass
# Temp
def ShowPhyloLocal(self,fileHandler):
#     self.tree = Phylo.parse(fileHandler, 'phyloxml').next()
#     print(tree)
    pass