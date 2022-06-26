def lia(path):
    with open(path) as fp:
        n,k=[int(i) for i in fp.readline().split()]
    return lia_(n,k)
def Fic(n,res=1):
    for i in range(1,n+1):res*=i
    return res
def comb(n,k):
    return Fic(n)/(Fic(k)*Fic(n-k))
def lia_(n,k):

    return round(sum(comb(2**n,i)*0.25**i*0.75**(2**n-i) for i in range(k,2**n+1)),3)
print(lia(r'rosalind_lia.txt'))
