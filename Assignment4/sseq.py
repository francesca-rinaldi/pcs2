from Bio import SeqIO

def sseq(s, t):
    i = 0
    for e in t:
        j = s.find(e, i)
        print(j + 1, end = ' ')
        i = j+1

records = list(SeqIO.parse("rosalind_sseq.txt", "fasta"))
s = records[0].seq
t = records[1].seq
sseq(s, t)
