from collections import Counter, defaultdict

N = int(input())
P = []
R = []
D = defaultdict(int)
for i in range(N):
    Ri, Hi = map(int, input().split())
    Hi -= 1
    P.append((Ri, Hi))
    R.append(Ri)
    D[(Ri, Hi)] += 1

C = Counter(R)
T = dict()
t = 0
for r in sorted(C.keys()):
    T[r] = t
    t += C[r]

for p in P:
    w = T[p[0]] + D[(p[0], (p[1] + 1) % 3)]
    l = N - T[p[0]] - C[p[0]] + D[(p[0], (p[1] + 2) % 3)]
    d = D[p] - 1
    print(w, l, d)
