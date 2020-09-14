import Bio
from Bio import Entrez  #  Importar módulo Bio.Entrez 
from Bio import SeqIO   #   Módulo para analisar sequências

Entrez.email = "gabrielgmusskopf@gmail.com" #   Informar NCBI

'''Usando o ESearch - Buscando no bancos de dados Entrez'''

handle = Entrez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]", idtype="acc") 

#   Usando ESearch para pesquisar no GenBank
#   Buscando pelo gene "matK" de Cypripedioideae orquídeas

#record = Entrez.read(handle)


#print(record["Count"])
#print("ID List: ", record["IdList"])
#   Cada um desses ID's é um identificador do GenBank (número de acesso)

    

'''EPost - Carregando uma lista de identificadores'''

#   Bio.Entrez.epost()
#   Caso queira baixar uma longa lista de IDs usando o EFathc, usamos o EPost, por que se não o URL fica grande de mais e pode quebrar


'''EFetch - Baixando registros completos do Entrez'''

#handle = Entrez.efetch (db = "nucleotide", id = "EU490707", rettype = "gb", retmode = "text")
#print (handle.read ())

#   Ao baixarmos formatos aceitos pelo Bio.SeqIO, podemos analisar os dados de melhor forma
handle = Entrez.efetch (db = "nuccore", id = "EU490707", rettype = "fasta", retmode = "text")
record = SeqIO.read (handle, "fasta")
handle.close ()

print (handle.url)
print (record.id)
print (record.name)
print (record.description)
print (len (record.features)) 
print (record.seq)


#   É possível baixar os dados na máquina local, mas como não é o intuito do projeto, não vou aprofundar sobre


'''ELink - Procurando por itens relacionados no NCBI Entrez'''

pmid = "19304878"
record = Entrez.read(Entrez.elink(dbfrom="pubmed", id=pmid))

#print (record[0]["DbFrom"])
#print (record[0]["IdList"])

#   Em "LinkSetDb" contém os resultados em formato de lista

#print ( len(record[0]["LinkSetDb"]) )
#for link in record[0]["LinkSetDb"][0]["Link"]:
#    print(link["Id"])

#   Cada elemento é um ID  


'''Achando a Linhagem de um organismo'''


