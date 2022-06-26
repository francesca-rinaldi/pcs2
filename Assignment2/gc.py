def gc(f):
    ID = ''
    freq = 0
    for l in f:
        l = l.split('\n', 1)
        s = l[1].replace('\n', '')
        nfreq = float((s.count('C') + s.count('G'))/(len(s)))
        if nfreq > freq:
            ID = l[0]
            freq = nfreq
    return ID, round(freq*100, 6)

with open('rosalind_gc.txt', 'r') as f:
    f = f.read().split('>')[1:]
    print(gc(f)[0])
    print(gc(f)[1])
