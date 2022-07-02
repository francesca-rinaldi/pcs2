import requests
from Bio import SeqIO
import re
ID = []
ids = []
with open('rosalind_mprt.txt') as f:
    for line in f:
        l = line.strip()
        ids.append(l)
        if "_" in l:
            l = l[:l.index("_")]
        ID.append(l)
lib_data = []
for i in range(len(ID)):
    
    URL = 'http://www.uniprot.org/uniprot/' + ID[i] + '.fasta'

    data = requests.get(URL)
    lib_data.append(data.text)

with open('seq_file.fasta', 'w') as text_file:
    text_file.write('\n'.join(lib_data))

handle = open('seq_file.fasta', 'r')
motifs = re.compile(r'(?=(N[^P][ST][^P]))')
count = 0
print('\n\n\n\n')
for record in SeqIO.parse(handle, 'fasta'):
    sequence = record.seq
    positions = []
    for m in re.finditer(motifs, str(sequence)):
        positions.append(m.start() + 1)
    if len(positions) > 0:
        for i in range(len(ids)):
            if ids[i][0:len(ID[count])] == ID[count]:
                print(ids[i])

        print(' '.join(map(str, positions)))
    count += 1
