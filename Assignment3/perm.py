import itertools
n = 6
lst = list(itertools.permutations(range(1, 7), 6))
print(len(lst))
for e in lst:
    print(*e)
