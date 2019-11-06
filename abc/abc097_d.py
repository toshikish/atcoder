N, M = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))


class DisjointSet():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


d = DisjointSet(N)
for i in range(M):
    xi, yi = map(int, input().split())
    d.unite(p[xi - 1], p[yi - 1])

ans = 0
for i in range(N):
    if d.find(p[i]) == d.find(i):
        ans += 1
print(ans)
