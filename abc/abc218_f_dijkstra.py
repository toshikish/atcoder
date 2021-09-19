from heapq import heappop, heappush

N, M = map(int, input().split())
G = [{} for _ in range(N)]
for i in range(M):
    si, ti = map(int, input().split())
    si -= 1
    ti -= 1
    G[si][ti] = i
INF = 500


def dijkstra(ex=-1):
    d = [INF] * N
    p = [-1] * N
    d[0] = p[0] = 0
    hq = [(0, 0)]
    while hq:
        dv, v = heappop(hq)
        if dv > d[v]:
            continue
        for nv, i in G[v].items():
            if i == ex or d[nv] <= d[v] + 1:
                continue
            d[nv] = d[v] + 1
            p[nv] = v
            heappush(hq, (d[nv], nv))
    return (-1 if d[N - 1] == INF else d[N - 1]), p


d0, p0 = dijkstra()
route = [False] * M
i = N - 1
while i != 0 and p0[i] != -1:
    route[G[p0[i]][i]] = True
    i = p0[i]

for i in range(M):
    if not route[i]:
        print(d0)
        continue
    d1, _ = dijkstra(i)
    print(d1)
