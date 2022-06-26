def revc(s):
    cs= ''
    for c in s[::-1]:
        if c== 'A':
            cs+= 'T'
        if c== 'C':
            cs+= 'G'
        if c== 'G':
            cs+= 'C'
        if c== 'T':
            cs+= 'A'
    return cs
with open('rosalind_revc.txt') as f:
    s=f.read()
    print(revc(s))
