def tree(n, adj_lst):
    return n - len(adj_lst) - 1
with open('rosalind_tree.txt', 'r') as f:
    f = f.readlines()
    n = int(f[0])
    adj_lst = f[1:]
    print(tree(n, adj_lst))
