import heapq

N, M = map(int, input().split())
neighbors = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi, Ci = map(int, input().split())
    Ai -= 1
    Bi -= 1
    neighbors[Ai].append((Bi, Ci))

INF = 1_000_000_000

for u in range(N):
    d = [INF] * N
    PQ = []

    def push(v, c):
        if d[v] <= c:
            return
        d[v] = c
        heapq.heappush(PQ, (c, v))

    for v, c in neighbors[u]:
        push(v, c)
    while PQ:
        dv, v = heapq.heappop(PQ)
        if dv > d[v]:
            continue
        for w, c in neighbors[v]:
            push(w, d[v] + c)
    print(d[u] if d[u] != INF else -1)
