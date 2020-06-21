from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = []
for i in range(Q):
    Bi, Ci = map(int, input().split())
    queries.append((Bi, Ci))

S = sum(A)
c = Counter(A)
for Bi, Ci in queries:
    S += (Ci - Bi) * c[Bi]
    print(S)
    c.update({Bi: -c[Bi], Ci: c[Bi]})
