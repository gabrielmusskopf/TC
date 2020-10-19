import Bio
from Bio import SeqIO
from Bio import Entrez
from Bio.Blast import NCBIWWW, NCBIXML

Entrez.email = input("e-mail ")

print("Digite P se deseja pesquisar pela sequencia nucleotidica")
print("Digite I se deseja inserir a sequencia nucleotidica")

tecla1 = input()

if tecla1 == 'P':
    tecla2 = input("Se deseja escrever o nome/nome cientifico do virus, digite N ou n para numero identificador") #tecla2
    tecla3 = input("Se deseja escrever o gene especifico, digite g ou G para genoma") #tecla3

    if tecla2 == 'N':
        term = input("Nome/nome cientifico: ")
        #preciso descobrir como retornar o numero de acesso ou GI se a pessoa não souber
        handle = Entrez.esearch(db = "nucleotide", term,  rettype = "uilist", retmode = "xml", retstart = 0, retmax = 1)
        record = Entrez.read(handle) #lendo as infos geradas pela pesquisa
        #print("{} Genomas mais parecidos com o de entrada".format(record["Count"]))
        #print("Aqui estao os IDs dos 10 genomas mais parecidos\n{}".format(record['IdList']))
        num = record["Count"]

    elif tecla2 == 'n':
        num = input("Numero de acesso/GI: ")

    if tecla3 == 'g':
        gene = input("Gene: ")
        term = term + gene
    elif tecla3 == 'G':
        term = term + 'complete genome'

tecla4 = input("Agora digite GO para submeter as infos ")

if tecla4 == 'GO':
    handle = Entrez.esearch(db = "nucleotide", term,  rettype = "uilist", retmode = "xml", retstart = 0, retmax = 10)
    print("cheguei aqui 1")

    record = Entrez.read(handle) #lendo as infos geradas pela pesquisa
    print("{} Genomas mais parecidos com o de entrada".format(record["Count"]))
    print("Aqui estao os IDs dos 10 genomas mais parecidos\n{}".format(record['IdList']))
    print("cheguei aqui 2")

    result_handle = NCBIWWW.qblast(arg1 = 'blastn', arg2 = 'nt', arg3 = num)
    print("cheguei ate aqui 3")

    blast_record = NCBIXML.read(result_handle) #eu queria printar esse resultado de alguma forma
    print("cheguei ate aqui 4")

if tecla1 == 'I':
    tecla5 = input("Digite F se deseja inserir o arquivo FASTA ou S para adicionar a sequencia nucleotidica ")

    if tecla5 == 'F':
        #vrau vai dizer como fazer isso ja fez?

    elif tecla5 == 'S':
        sequencia = input("Sequencia nucleotidica aqui: ")

tecla6 = input("Agora digite GO para submeter as infos ")

if tecla6 == 'GO':

    result_handle = NCBIWWW.qblast(arg1 = 'blastn', arg2 = 'nt', arg3 = sequencia)
    print("cheguei ate aqui 3")

    blast_record = NCBIXML.read(result_handle) #eu queria printar esse resultado de alguma forma
    print("cheguei ate aqui 4")
