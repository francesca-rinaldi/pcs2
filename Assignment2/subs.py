def subs(s, t):
    r = []
    i = s.find(t)
    while i != -1:
        r.append(i+1)
        j = s.find(t, i+1)
        i = j
    return r
with open('rosalind_subs.txt', 'r') as f:
    f = f.readlines()
    s = f[0].replace('\n', '')
    t = f[1].replace('\n', '')
    print(*subs(s, t))
