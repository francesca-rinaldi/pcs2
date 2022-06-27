def fib(n, k):
    p = 1
    c = 1
    for i in range(n-2):
        nc  = k*p + c
        p = c
        c = nc
    print(c)
with open('rosalind_fib.txt', 'r') as f:
    f = f.read()
    f = list(map(int, f.split()))
    n, k = f[0], f[1]
    fib(n, k)
