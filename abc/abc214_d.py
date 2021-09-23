N = int(input())
E = []
for _ in range(N - 1):
    ui, vi, wi = map(int, input().split())
    ui -= 1
    vi -= 1
    E.append((wi, ui, vi))

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

    def size(self, x):
        return self.rank[self.find(x)]


ds = DisjointSet(N)
ans = 0
for wi, ui, vi in E:
    ans += wi * ds.size(ui) * ds.size(vi)
    ds.unite(ui, vi)

print(ans)
