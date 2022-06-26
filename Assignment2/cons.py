def cons(collection):
    prof = {}
    prof['A'] = []
    prof['C'] = []
    prof['G'] = []
    prof['T'] = []
    for j in range(len(collection[0])):
        Acount = 0
        Ccount = 0
        Gcount = 0
        Tcount = 0
        for s in collection:
            if s[j] == 'A':
                Acount += 1
            elif s[j] == 'C':
                Ccount += 1
            elif s[j] == 'G':
                Gcount += 1
            elif s[j] == 'T':
                Tcount += 1
        prof['A'].append(Acount)
        prof['C'].append(Ccount)
        prof['G'].append(Gcount)
        prof['T'].append(Tcount)
    cons = ''
    for k in range(len(prof['A'])):
        n = ''
        m = 0
        for key, value in prof.items():
            if value[k] > m:
                m = value[k]
                n = key
            else: None
        cons += n
    print(cons)
    for key, value in prof.items():
        print(str(key) + ':', *value)
with open('rosalind_cons.txt', 'r') as f:
    collection = []
    f = f.read().split('>')[1:]
    for i in range(len(f)):
        line = f[i].split('\n', 1)
        s = line[1].replace('\n', '')
        collection.append(s)
    cons(collection)
