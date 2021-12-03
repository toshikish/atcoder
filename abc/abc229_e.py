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


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    G[Ai].append(Bi)

ans = [0] * N
ds = DisjointSet(N)
for i in range(N - 2, -1, -1):
    s = set([ds.find(j) for j in G[i + 1]])
    ans[i] = ans[i + 1] + 1 - len(s)
    for j in G[i + 1]:
        ds.unite(i + 1, j)

for ai in ans:
    print(ai)
