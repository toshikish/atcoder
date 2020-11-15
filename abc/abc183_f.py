from collections import defaultdict

N, Q = map(int, input().split())
C = list(map(lambda s: int(s) - 1, input().split()))


class DisjointSet():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.cnt = [defaultdict(int) for i in range(N)]
        for i in range(N):
            self.cnt[i][C[i]] += 1

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
            self.merge(x, y)
        else:
            self.parent[y] = x
            self.merge(y, x)
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def merge(self, fr, to):
        for k, v in self.cnt[fr].items():
            self.cnt[to][k] += v

    def count(self, x, y):
        return self.cnt[self.find(x)][y]


d = DisjointSet(N)
for i in range(Q):
    t, x, y = map(lambda s: int(s) - 1, input().split())
    if t == 0:
        d.unite(x, y)
    else:
        print(d.count(x, y))
