from itertools import permutations

S, K = input().split()
K = int(K)

s = set()
k = 0
p = permutations(sorted(list(S)), len(S))
for w in p:
    w = ''.join(w)
    if w in s:
        continue
    s.add(w)
    k += 1
    if k == K:
        break

print(w)
