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
ds = DisjointSet(N)
E = []
for i in range(M):
    Ui, Vi = map(lambda s: int(s) - 1, input().split())
    ds.unite(Ui, Vi)
    E.append((Ui, Vi))
MOD = 998244353

numE = [0] * N
for ui, _ in E:
    numE[ds.find(ui)] += 1

ans = 1
for i in range(N):
    if ds.find(i) != i:
        continue
    if ds.rank[i] != numE[i]:
        ans = 0
        break
    ans *= 2
    ans %= MOD
print(ans)
