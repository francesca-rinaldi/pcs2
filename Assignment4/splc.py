from Bio.Seq import Seq
def splc(s, introns):
    for intron in introns:
        s = s.replace(intron, '')
    dna_seq = Seq(s)
    prot = dna_seq.translate(to_stop = True)
    return(prot)
with open('rosalind_splc.txt', 'r') as f:
    introns = []
    f = f.read().split('>')[1:]
    s = str(f[0]).split('\n', 1)[1].replace('\n', '')
    for i in range(1, len(f)):
        intron = f[i].split('\n', 1)[1].replace('\n', '')
        introns.append(intron)
    print(splc(s, introns))
