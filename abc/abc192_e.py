import heapq

N, M, X, Y = map(int, input().split())
X -= 1
Y -= 1
neighbors = [[] for i in range(N)]
for i in range(M):
    Ai, Bi, Ti, Ki = map(int, input().split())
    Ai -= 1
    Bi -= 1
    neighbors[Ai].append((Bi, Ti, Ki))
    neighbors[Bi].append((Ai, Ti, Ki))

INF = 1_000_000_000_000_000
d = [INF] * N
d[X] = 0
PQ = []
heapq.heappush(PQ, (d[X], X))

while PQ:
    du, u = heapq.heappop(PQ)
    if d[u] < du:
        continue
    for v, Ti, Ki in neighbors[u]:
        ndv = (d[u] + Ki - 1) // Ki * Ki + Ti
        if ndv < d[v]:
            d[v] = ndv
            heapq.heappush(PQ, (d[v], v))
print(d[Y] if d[Y] != INF else -1)
