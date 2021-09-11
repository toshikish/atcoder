N, M = map(int, input().split())
E = []
for _ in range(M):
    Ai, Bi, Ci = map(int, input().split())
    Ai -= 1
    Bi -= 1
    E.append((Ci, Ai, Bi))

E.sort()

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

ds = DisjointSet(N)
ans = 0
for ci, ai, bi in E:
    if ds.find(ai) == ds.find(bi):
        ans += max(ci, 0)
        continue
    ds.unite(ai, bi)

print(ans)
