N, C = map(int, input().split())
Q = []
for i in range(N):
    ai, bi, ci = map(int, input().split())
    Q.append((ai, ci))
    Q.append((bi + 1, -ci))

S = 0
Q.sort()
D, total = Q[0]
for i in range(1, 2 * N):
    Dn, Cn = Q[i]
    S += min(total, C) * (Dn - D)
    D = Dn
    total += Cn

print(S)
