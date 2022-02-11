import sys

sys.setrecursionlimit(1000000)


class DisjointSet():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            x, y = y, x
        self.parent[x] = y
        self.rank[y] += self.rank[x]


N = int(input())
P = list(map(lambda s: int(s) - 1, input().split()))
M = int(input())
ds = DisjointSet(N)
G = [[] for _ in range(N)]
operation = []
for i in range(M):
    ai, bi = map(lambda s: int(s) - 1, input().split())
    if ds.find(ai) == ds.find(bi):
        continue
    ds.unite(ai, bi)
    G[ai].append((bi, i + 1))
    G[bi].append((ai, i + 1))
    operation.append((ai, bi))

possible = all(ds.find(i) == ds.find(P[i]) for i in range(N))
if possible:
    ans = []

    def pull(v, tg, p):
        if P[v] == tg:
            return True
        for nv, op in G[v]:
            if nv == p:
                continue
            if pull(nv, tg, v):
                P[v], P[nv] = P[nv], P[v]
                ans.append(op)
                return True
        return False

    def dfs(v, p):
        for nv, _ in G[v]:
            if nv == p:
                continue
            dfs(nv, v)
        pull(v, v, -1)

    for v in range(N):
        if v != ds.find(v):
            continue
        dfs(v, -1)
    print(len(ans))
    print(*ans)
else:
    print(-1)
