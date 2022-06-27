

def nucleotides(s):
    return [s.count('A'), s.count('C'), s.count('G'), s.count('T')]
f = open('rosalind_dna.txt')
s = f.read()
print(*nucleotides(s))
