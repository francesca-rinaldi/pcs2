from Bio import SeqIO
from Bio.Seq import Seq
stop_codons = ["TGA", "TAG", "TAA"]

def orf(s, cs):
    prots = []
    while 'ATG' in s:
        s = s[s.find('ATG'):]
        for stop in stop_codons:
            for j in range(0, len(s), 3):
                    if s[j:j+3] == stop:
                        orf = s[:j]
                        prots.append(orf.translate(to_stop = True))
        s = s[1:]
    while 'ATG' in cs:
        cs = cs[cs.find('ATG'):]
        for stop in stop_codons:
            for j in range(0, len(cs), 3):
                    if cs[j:j+3] == stop:
                        orf = cs[:j]
                        prots.append(orf.translate(to_stop = True))
        cs = cs[1:]
    for p in set(prots):
        print(p)
record = list(SeqIO.parse("rosalind_orf.txt", "fasta"))[0]
s = record.seq
cs = Seq.reverse_complement(record.seq)
orf(s, cs)
