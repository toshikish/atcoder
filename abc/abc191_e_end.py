import heapq

N, M = map(int, input().split())
neighbors = [[] for _ in range(N)]
sources = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi, Ci = map(int, input().split())
    Ai -= 1
    Bi -= 1
    neighbors[Ai].append((Bi, Ci))
    sources[Bi].append((Ai, Ci))

INF = 1_000_000_000

for u in range(N):
    d = [INF] * N
    PQ = []

    def push(v, c):
        if d[v] <= c:
            return
        d[v] = c
        heapq.heappush(PQ, (c, v))

    push(u, 0)
    while PQ:
        dv, v = heapq.heappop(PQ)
        if dv > d[v]:
            continue
        for w, c in neighbors[v]:
            push(w, d[v] + c)
    candidates = []
    for v, c in sources[u]:
        if d[v] == INF:
            continue
        candidates.append(d[v] + c)
    print(min(candidates) if len(candidates) > 0 else -1)
