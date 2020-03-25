from collections import Counter

S = input()
c = Counter(S)
v = [c[l] for l in 'abc']
print('YES' if max(v) - min(v) <= 1 else 'NO')
