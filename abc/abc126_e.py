N, M = map(int, input().split())


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

    def count_groups(self):
        return len([i for i, x in enumerate(self.parent) if i == x])


d = DisjointSet(N)
for i in range(M):
    xi, yi, zi = map(int, input().split())
    d.unite(xi - 1, yi - 1)
print(d.count_groups())
