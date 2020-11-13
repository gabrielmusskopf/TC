import os
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtWidgets import *
import Bio
#   Importar módulo Bio.Entrez 
#   Módulo para analisar sequências
#   Módulo para árvores filogenéticas
from Bio import Entrez, SeqIO, AlignIO, Phylo  
from Bio.Phylo import PhyloXMLIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
from Bio.Align.Applications import ClustalOmegaCommandline

from validate_email import validate_email

from datetime import datetime

# from main_v02 import *

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
    options = QFileDialog.Options()
    # options |= QFileDialog.DontUseNativeDialog
    self.filename = QFileDialog.getOpenFileName(filter="Fasta files (*.fasta)", options=options)
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

    # with open("entrez_search.xml","w") as save_file:
    #   self.save_file.write(self.result_hande.read())


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
    print("Entrei no LocalAlignment: ",datetime.now().hour, ":", datetime.now().minute, ":", datetime.now().second)

    # result_handle = NCBIWWW.qblast("blastn", "nt", id)

    # with open("alignment_result.xml","w") as save_file: # Para automaticamente fechar o "save_file"
    #     # self.save_file.write(str(datetime.now()))
    #     save_file.write(result_handle.read())
    #     result_handle.close()

    result_handle = open("alignment_result.xml","r")
    blast_record = NCBIXML.read(result_handle)

    print("Fim do LocalAlignment: ", datetime.now().hour, ":", datetime.now().minute, ":", datetime.now().second)
    return blast_record


def WebAlignment(self,method_ui):
    print("Entrei no WebAlignment:", datetime.now().hour, ":", datetime.now().minute, ":", datetime.now().second)
    
    # self.result_hande = NCBIWWW.qblast("blastn", "nt",'NG_070885.1', alignments=2)

    # self.save_file = open("alignment_result","w")
    # self.save_file.write(self.result_hande.read())
    # print(type(self.save_file))
    # self.save_file.close()

    self.result_handle = open("alignment_result.xml","r")
    self.blast_record = NCBIXML.read(self.result_handle)

    # Caso não seja salvo em um arquivo, retornar a variável
    print("Fim do WebAlignment: ", datetime.now().hour, ":", datetime.now().minute, ":", datetime.now().second)

    return self.blast_record

'''
Falta trocar de tela quando o alinhamento é local
'''

def ShowAlignments(self, blast_record):

    count = 0
    queryies=[]
    matches=[]
    subjects=[]

    with open("result.txt",'w') as result_file:
        for alignment in blast_record.alignments:
            if count<3:
                for hsp in alignment.hsps:
                    count+=1
                    result_file.write("\n ***Alignment*** \n" +
                    "Sequence: " + str(alignment.title) + "\n" + 
                    "Length: "+ str(alignment.length) + "\n"+
                    "Nums of differents bases: "+str(hamming(hsp.query,hsp.sbjct))+"\n"+
                     str(hsp.query[0:75])+"..." + "\n" +
                     str(hsp.match[0:75]) + "..." + "\n" +
                     str(hsp.sbjct[0:75]) + "..." +"\n")

                    #print('Alinhamento '+str(i)) #printa número do alinhamento
                    #print('Sequencia:'+a.title) #informações sobre a sequência
                    #print('Tamanho:',a.length)  #pares de base
                    #print('Score:',hsp.score)   #quanto teve de cobertura
                    #print('Gaps:',hsp.gaps)     #quantos indels (deleção,inserção)
                    queryies.append(hsp.query)
                    matches.append(hsp.match)
                    subjects.append(hsp.sbjct)

        # mat = 0
        # for i in range(0,len(matches)):
        #     for c in range(0,len(matches[i])):
        #         if matches[i][c] == ' ':
        #             mat+=1
        # print(mat)

    with open("result.txt","r") as r:
        # print(r.read())
        self.result_ui.alignmentResultLabel.setText(r.read())

    print("\n" + "Tem ",count,"sequências na saída do Blast")



def ShowSites(self,blast_record):

    count=0
    queryies=[]
    matches=[]
    subjects=[]
    lengths=[]
    leng = 0

    with open("sites_result.txt",'w') as result_file:
        result_file.write("\n ***Sites*** \n")

        for alignment in blast_record.alignments:
            if count<3:
                for hsp in alignment.hsps:
                    count+=1
                    self.result_ui.sitesFrame.setMinimumSize(QtCore.QSize(10*alignment.length, 1200))
                    # result_file.write( str(hsp.query) + "\t" +"\n")
                    # result_file.write( str(hsp.match) + "\t" +"\n")
                    queryies.append(hsp.query)
                    matches.append(hsp.match)
                    subjects.append(hsp.sbjct)
                    lengths.append(alignment.length)
                    leng += alignment.length 

        # for i in range(0,len(queryies)):
        result_file.write( str(queryies[0])+"\n")

        for c in range(0,len(matches[0])):
            result_file.write(str( matches[0][c] ) + " ")

        # for i in range(0,len(subjects)):
        result_file.write( str(subjects[0])+"\n")


    with open("sites_result.txt","r") as r:
        self.result_ui.sitesResultLabel.setText(r.read())


    wdir = os.getcwd()
    print(wdir)

    in_file = "sites_result.txt"
    out_file = "alignment_general.fasta"

    clustalomega_cline = ClustalOmegaCommandline(infile = in_file, outfile = out_file, verbose = True, auto = False)
    print(clustalomega_cline)

    path = "r'" + str(wdir)
    input_comand = '"' + wdir + '/clustal-omega-1.2.2-win64/' + str(clustalomega_cline)[0:8] + '" ' + str(clustalomega_cline)
    print(input_comand)
    os.system(input_comand)



    # for i in range(0,len(queryies)):
    #     for j in range(lengths[0]):
    #         if queryies[0][j] != subjects[i][j]:
    #             print("Alteração na posição: " + str(i) + ", " + str(j) + "\n")

    
    # print(sequences[0][0])


def hamming(d1, d2):
    total = 0

    if d1 > d2:
        menor_dna = d2
    else: menor_dna = d1
    
    for i in range(len( menor_dna )):
        if d1[i] != d2[i]:
            total += 1
    print(total)
    return total


def ShowPhylo(self,result_ui):
    print("Mostrando árvore filogenética..")
    # result_ui.resultText.setPixmap(QtGui.QPixmap("C:/Users/fabri_000/Documents/_Pesquisas TCC/Bioinformática Python/gui-pyqt5/images/loading_dna.gif"))
    
    


    # Alinhamento soemnte com arquivo local por enquanto
    # tree = Phylo.read('alignment_result.xml', 'phyloxml')
    # print(tree)

    print("Mostrada a árvore filogenética.")