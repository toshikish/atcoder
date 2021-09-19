from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    si, ti = map(int, input().split())
    si -= 1
    ti -= 1
    G[si].append((ti, i))


def bfs():
    d = [-1] * N
    p = [False] * M
    d[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for nv, i in G[v]:
            if d[nv] != -1:
                continue
            d[nv] = d[v] + 1
            p[i] = True
            q.append(nv)
        if d[N - 1] != -1:
            break
    return d[N - 1], p


def bfs2(ex=-1):
    d = [-1] * N
    d[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for nv, i in G[v]:
            if i == ex or d[nv] != -1:
                continue
            d[nv] = d[v] + 1
            q.append(nv)
        if d[N - 1] != -1:
            break
    return d[N - 1]


d0, p0 = bfs()

for i in range(M):
    if not p0[i]:
        print(d0)
        continue
    print(bfs2(i))
