S = input()

L = ['A', 'B', 'C', 'D', 'E', 'F']
n = [str(S.count(l)) for l in L]
print(' '.join(n))
