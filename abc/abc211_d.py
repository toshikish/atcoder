from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    g[Ai].append(Bi)
    g[Bi].append(Ai)

MOD = 1_000_000_007
INF = 1_000_000
d = [INF] * N
d[0] = 0
c = [0] * N
c[0] = 1
Q = deque([0])
while Q:
    v = Q.popleft()
    for u in g[v]:
        if d[u] < d[v] + 1:
            continue
        if d[u] > d[v] + 1:
            Q.append(u)
        d[u] = d[v] + 1
        c[u] += c[v]
        c[u] %= MOD

print(0 if d[N - 1] == INF else c[N - 1])
