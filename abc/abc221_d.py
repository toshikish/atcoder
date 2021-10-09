from collections import defaultdict

N = int(input())
D = defaultdict(int)
for _ in range(N):
    Ai, Bi = map(int, input().split())
    D[Ai] += 1
    D[Ai + Bi] -= 1

ans = [0] * (N + 1)
k = 0
pd = 0
for d in sorted(D.keys()):
    if D[d] == 0:
        continue
    ans[k] += d - pd
    k += D[d]
    pd = d

print(' '.join(list(map(str, ans[1:]))))
