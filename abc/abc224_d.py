from collections import deque

M = int(input())
G = [[]for _ in range(9)]
for _ in range(M):
    ui, vi = map(lambda s: int(s) - 1, input().split())
    G[ui].append(vi)
    G[vi].append(ui)
P = list(map(lambda s: int(s) - 1, input().split()))

S = [8] * 9
for i in range(8):
    S[P[i]] = i
tS = tuple(S)
d = {}
d[tS] = 0
q = deque()
q.append((S.index(8), tS))
while q:
    v, tS = q.popleft()
    dtS = d[tS]
    S = list(tS)
    for nv in G[v]:
        S[v], S[nv] = S[nv], S[v]
        ntS = tuple(S)
        if ntS not in d:
            d[ntS] = dtS + 1
            q.append((nv, ntS))
        S[v], S[nv] = S[nv], S[v]

tE = tuple(range(9))
print(d[tE] if tE in d else -1)
