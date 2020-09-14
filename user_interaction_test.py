import Bio
from Bio import Entrez  #  Importar módulo Bio.Entrez 
from Bio import SeqIO   #   Módulo para analisar sequências

#Entrez.email = str(input("Digite seu e-mail: "))
Entrez.email = 'gabrielgmusskopf@gmail.com'
#print (Entrez.email)

'''
Entrez.efetch(db, id, rettype, retmode)


    db - data base de onde retirar os dados (Tabela 2)
    id - UID da espécie pesquisada (específico de cada db)
    rettype - Tipo de retorno (GenBank, fasta... Conferir na tabela 1)
    retmode - Modo de retorno (text, XML, HTML... Conferir na tabela 1)


    Tabela 1: https://www.ncbi.nlm.nih.gov/books/NBK25499/table/chapter4.T._valid_values_of__retmode_and/?report=objectonly
    Tabela 2: https://www.ncbi.nlm.nih.gov/books/NBK25497/table/chapter2.T._entrez_unique_identifiers_ui/?report=objectonly
'''

'''
db = str(input("Digite o Banco de Dados: "))
id = str(input("Digite o ID: "))
retmode = str(input("Digite o Retmode: "))
rettype = str(input("Digite o Rettype: "))


handle = Entrez.efetch(db=db, id=id, rettype=rettype, retmode=retmode)

record = SeqIO.read(handle, 'fasta')

print (handle.url)
print (record.name)
print (record.id)
print (record.seq)
'''
'''
handle2 = Entrez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]", rettype = "fasta", retmode = "text", idtype="acc") 
record = Entrez.read(handle2)
handle2.close()

print (handle2.url)

for id in record["IdList"] :
    print (id, record["IdList"].index(id))
'''    



