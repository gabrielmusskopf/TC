from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import Bio
#   Importar módulo Bio.Entrez 
#   Módulo para analisar sequências
#   Módulo para árvores filogenéticas
from Bio import Entrez, SeqIO, AlignIO, Phylo  
from Bio.Phylo import PhyloXMLIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
from validate_email import validate_email

from time import gmtime, strftime

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


def LoadingPopUp():
    pop = QMessageBox()
    pop.setWindowTitle("Carregando")
    pop.setText("Carregando alinhamento")
    pop.exec_()
	

# Janela de pesquisa de arquivo
def OpenDialogBox(self,method_ui):
    self.filename = QFileDialog.getOpenFileName(filter="Fasta files (*.fasta)")
    self.path = self.filename[0]
    method_ui.fileEdit.setText(self.path)

    # print(self.filename.read())


    if self.path != '':
        record = SeqIO.read(self.path,"fasta")
        return record.id
    else:
        return "None"

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

    self.handle = Entrez.esearch(db="nucleotide", term = method_ui.searchEdit.text(), idtype="acc", retmax = 1) 
    # Retorna um XMLh
    self.record = Entrez.read(self.handle) #lendo as infos geradas pela pesquisa
    # Converte XML para estrutura de dados python (dicionários)





    print(method_ui.searchEdit.text())
    print(self.handle.url)


    # self.result_hande = NCBIWWW.qblast("blastn", "nt",'NG_070885.1', alignments=2)

    # self.save_file = open("xml","w")
    # self.save_file.write(self.result_hande.read())
    # self.save_file.close()


    self.handle.close()



    # print (self.handle.url)
    # print(self.record["Count"])
    print("ID List: ", self.record["IdList"])
    # print("Term: ", self.record["TranslationStack"])

    if self.record["Count"] == "0" or self.record["IdList"]==[]:
        print ("não encontrado semelhantes")
        print("vai criar um popup pra isso!")
        # popError(self)

    # WebAlignment(self,method_ui)

    return self.record
    # popResultWeb(self)

def LocalAlignment(self, id):
    print("Entrei no LocalAlignment")
    self.result_hande = NCBIWWW.qblast("blastn", "nt",id, alignments=2)

    self.save_file = open("alignment_result","w")
    self.save_file.write(self.result_hande.read())
    self.save_file.close()

    print("Fim do LocalAlignment")

def WebAlignment(self,method_ui):
    print("Entrei no WebAlignment")
    print( strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) )
    
    self.result_hande = NCBIWWW.qblast("blastn", "nt",'NG_070885.1', alignments=2)

    self.save_file = open("xml","w")
    self.save_file.write(self.result_hande.read())
    self.save_file.close()

    # Caso não seja salvo em um arquivo, retornar a variável
    print("Fim do WebAlignment")
    print( strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) )

    def ShowPhylo(self):
        pass