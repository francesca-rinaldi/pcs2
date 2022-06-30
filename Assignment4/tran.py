transitions = [['A', 'G'], ['C', 'T']]
transversions = [['A', 'C'], ['A', 'T'], ['C', 'G'], ['G', 'T']]
def tran(s1, s2):
    transitions_count = 0
    transversions_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if sorted([s1[i], s2[i]]) in transitions:
                transitions_count += 1
            elif sorted([s1[i], s2[i]]) in transversions:
                transversions_count += 1
    return(transitions_count/transversions_count)

with open('rosalind_tran.txt', 'r') as f:
    f = f.read().split('>')[1:]
    s1 = f[0].split('\n', 1)[1].replace('\n', '')
    s2 = f[1].split('\n', 1)[1].replace('\n', '')
    print(tran(s1, s2))
