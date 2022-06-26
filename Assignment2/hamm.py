def hamm(s1, s2):
    c = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            c += 1
    return(c)

with open('rosalind_hamm.txt', 'r') as f:
    f = f.read().split('\n')
    s1, s2 = f[0], f[1]
    print(hamm(s1, s2))
