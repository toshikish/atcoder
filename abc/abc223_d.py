from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
deg = [0] * N
G = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    G[Ai].append(Bi)
    deg[Bi] += 1

q = [i for i in range(N) if deg[i] == 0]
heapify(q)
ans = []
while q:
    v = heappop(q)
    ans.append(v)
    for nv in G[v]:
        deg[nv] -= 1
        if deg[nv] == 0:
            heappush(q, nv)

if len(ans) == N:
    print(' '.join(list(map(lambda x: str(x + 1), ans))))
else:
    print(-1)
