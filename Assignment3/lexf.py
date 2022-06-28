import itertools

def lexf(alpha, l):
    indeces = list(itertools.product(range(len(alpha)), repeat = l))
    for i in indeces:
        s = ''
        for e in i:
            s += alpha[e]
        print(s)
with open('rosalind_lexf.txt', 'r') as f:
    f = f.readlines()
    alpha = list(f[0].replace(' ', '').replace('\n', ''))
    l = int(f[1])
    lexf(alpha, l)
