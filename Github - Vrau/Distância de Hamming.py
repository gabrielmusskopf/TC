import Bio
from Bio.Seq import Seq # Trabalhando com sequência
from Bio.Alphabet import generic_dna,generic_rna,generic_protein # Para classificar o tipo do dna
from Bio import SeqIO # Carregar arquivo FASTA

def hamming(d1, d2):
    total = 0

    if d1 > d2:
        menor_dna = d2
    else: menor_dna = d1
    
    for i in range(len( menor_dna )):
        if d1[i] != d2[i]:
            total += 1
    print(total)
    

dna_cov = SeqIO.read("covid.fasta","fasta")
dna_influenza = SeqIO.read("influenza.fasta","fasta")

# Somente a sequência de nucleotídeos
ncov_dna = dna_cov.seq
ninfluenza_dna = dna_influenza.seq

print('covid',  len(ncov_dna),  'e influenza', len(ninfluenza_dna))

hamming(ncov_dna, ninfluenza_dna)


            
