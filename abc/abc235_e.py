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


N, M, Q = map(int, input().split())
queries = []
for _ in range(M):
    ai, bi, ci = map(int, input().split())
    ai -= 1
    bi -= 1
    queries.append((ci, 0, ai, bi))
for i in range(Q):
    ui, vi, wi = map(int, input().split())
    ui -= 1
    vi -= 1
    queries.append((wi, i + 1, ui, vi))

queries.sort()
ds = DisjointSet(N)
ans = [True] * Q
for ci, i, ai, bi in queries:
    if i == 0:
        ds.unite(ai, bi)
    else:
        ans[i - 1] = ds.find(ai) != ds.find(bi)

for i in range(Q):
    print('Yes' if ans[i] else 'No')
