def transcribe(s):
    return s.replace('T', 'U')
with open('rosalind_rna.txt', 'r') as f:
    s = f.read()
    print(transcribe(s))
