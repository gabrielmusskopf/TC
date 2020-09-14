import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

#help(NCBIWWW.qblast)

'''
Versão online do Blast -> qblast( arg1, arg2, arg3, ...)

    arg1 = programa Blast: 
        BLASTN programs search nucleotide databases using a nucleotide query
        BLASTP programs search protein databases using a protein query
        BLASTX search protein databases using a translated nucleotide query -> nucleotide (tr) vs protein
        TBLASTN search translated nucleotide databases using a protein query -> protein vs nucleotide (tr)
        TBLASTX search translated nucleotide databases using a translated nucleotide query -> nucleotide (tr) vs nucleotide (tr)

        https://blast.ncbi.nlm.nih.gov/Blast.cgi

    arg2 = Banco de dados:
        nt (default) -> All GenBank + EMBL + DDBJ + PDB sequences, excluding sequences from PAT, EST, STS, GSS, WGS, TSA and phase 0, 1 or 2 HTGS sequences. Non-redundant, records with identical sequences collapsed into a single entry.
        
        ftp://ftp.ncbi.nlm.nih.gov/pub/factsheets/HowTo_BLASTGuide.pdf

    arg3 = Sequência:

        Pode ser a sequência em si, em formato FASTA ou o identificador

    format_type = Formato:

        O formato padrão é XML, mas pode mudar para "HTML", "Text", "ASN.1" ou "XML"

'''
print("oi01")

#   Realizando a pesquisa e criando um identificador "result_handle"
result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")

#   Análise dos resultados
blast_record = NCBIXML.read(result_handle)

#   Muitos resultados:
#   blast_records = NCBIXML.parse(result_handle)

print("oi")


