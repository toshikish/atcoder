class DisjointSet:
    def __init__(self, n):
        self.parent = {i: -1 for i in range(n)}

    def root(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.root(self.parent[a])
        return self.parent[a]

    def size(self, a):
        return -self.parent[self.root(a)]

    def link(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return False

        if self.size(a) < self.size(b):
            a, b = b, a

        self.parent[a] += self.parent[b]
        self.parent[b] = a

        return True

N, M = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    A.append(a)
    B.append(b)

ds = DisjointSet(N)
ans = {M - 1: int(N * (N - 1) / 2)}
# M-1 >= i >= 1
for i in range(M - 1, 0, -1):
    ans[i - 1] = ans[i]
    if ds.root(A[i]) != ds.root(B[i]):
        ans[i - 1] -= ds.size(A[i]) * ds.size(B[i])
        ds.link(A[i], B[i])

for i in range(M):
    print(ans[i])
