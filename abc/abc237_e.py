from heapq import heappush, heappop

N, M = map(int, input().split())
H = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    Ui, Vi = map(lambda s: int(s) - 1, input().split())
    if H[Ui] < H[Vi]:
        Ui, Vi = Vi, Ui
    G[Ui].append((Vi, 0))
    G[Vi].append((Ui, H[Ui] - H[Vi]))

INF = 1e15
d = [INF] * N
d[0] = 0
hq = [(0, 0)]
while hq:
    dv, v = heappop(hq)
    if dv > d[v]:
        continue
    for nv, c in G[v]:
        ndv = dv + c
        if ndv >= d[nv]:
            continue
        d[nv] = ndv
        heappush(hq, (ndv, nv))

print(H[0] - min(H[i] + d[i] for i in range(N)))
