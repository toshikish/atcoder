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


N = int(input())
A = list(map(lambda s: int(s) - 1, input().split()))
M = 200000

ds = DisjointSet(M)

for i in range(N // 2):
    if A[i] == A[N - i - 1]:
        continue
    ds.unite(A[i], A[N - i - 1])

ans = 0
for i in range(M):
    if ds.find(i) != i:
        continue
    ans += ds.size(i) - 1

print(ans)
