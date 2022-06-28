from Bio import SeqIO

def grph(rec):
    for i in rec:
        for j in rec:
            if i != j and rec[i][-3:] == rec[j][:3]:
                print(i, j)

rec = {}
for record in SeqIO.parse('rosalind_grph.txt', 'fasta'):
    rec[record.id] = record.seq
grph(rec)
