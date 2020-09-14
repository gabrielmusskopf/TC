import Bio
# Trabalhando com sequência
from Bio.Seq import Seq
# Para classificar o tipo do dna
from Bio.Alphabet import generic_dna,generic_rna,generic_protein
# Carregar arquivo FASTA
from Bio import SeqIO
# Ver as proteínas usando Pandas
#import pandas as pd
# Para contar a frequencia de amino ácidos
from collections import Counter


# Criando uma sequência (do tipo DNAAlphabet())
dna = Seq('ATGATCTGTAA',generic_dna)
print(dna,dna.alphabet)

# Contando nucleotídeos
#print(dna.count("A"))

# Contando códons
#print(dna.count("ATG"))

# Tamanho da sequência
#print(len(dna))

# localização do nucleotídeo
#print(dna.find("A"))

# Overlap contagem
#print(dna.count_overlap("ATG"))

# Transcrição DNA para mRNA
mRNA = dna.transcribe()
#print(mRNA, mRNA.alphabet)

# Tradução de mRNA para proteína
protein = mRNA.translate()
#print(protein, protein.alphabet)

# Complemento A-T  G-C
#print(dna.complement())

# Complemento Reverso
#print(dna.reverse_complement())

# Lendo aquivo FASTA
#for record in SeqIO.parse("sequence.fasta","fasta"):
    #print(record)

# Análise do arquivo
ncov_record = SeqIO.read("sequence.fasta","fasta")
#print(ncov_record)

# Somente a sequência de nucleotídeos
ncov_dna = ncov_record.seq
#print(ncov_dna)

# Transcrição de DNA para mRNA
ncov_rna = ncov_dna.transcribe()
#print(ncov_rna)

# Tradução de mRNA para Amino Ácidos(AA)/Proteína
ncov_protein = ncov_rna.translate()
#print(ncov_protein)

# Achando todas sequências de AA antes do STOPCODON
ncov_aa = ncov_protein.split("*")
#print(ncov_aa)

ncov_clean = [str(i) for i in ncov_aa]
#print(ncov_clean)
    
#df = pd.DataFrame({"amino_acids":ncov_clean})
#print(df)

# Conta a frequência de amino ácidos
print(Counter(ncov_protein).most_common(10))
