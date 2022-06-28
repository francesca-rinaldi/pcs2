def revp(s):
    ns = [['A', 'T'], ['C', 'G']]
    for i in range(len(s)):
        for l in range(4, 13, 2):
            if not i+l > len(s):
                pal = s[i : i + l]
                for x in range(l//2):
                    t = True
                    if sorted([pal[x], pal[l - x -1]]) not in ns:
                        t = False
                        break
                if t == True:
                    print(i+1, l)

with open('rosalind_revp.txt', 'r') as f:
    line = f.read().split('\n', 1)
    s = list(line[1].replace('\n', ''))
    revp(s)
