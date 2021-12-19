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
ds = DisjointSet(N)
loop = False
for _ in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    G[Ai].append(Bi)
    G[Bi].append(Ai)
    if ds.find(Ai) == ds.find(Bi):
        loop = True
    ds.unite(Ai, Bi)

ans = all(len(Gi) <= 2 for Gi in G) and not loop
print('Yes' if ans else 'No')
