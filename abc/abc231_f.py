from collections import defaultdict


class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = defaultdict(list)
compressed_b = {}
for i in range(N):
    d[A[i]].append(B[i])
    compressed_b[B[i]] = 0
m = 0
for bi in sorted(compressed_b.keys(), reverse=True):
    m += 1
    compressed_b[bi] = m

bit = BIT(m)
ans = 0
for _, bs in sorted(d.items()):
    for bi in bs:
        bit.add(compressed_b[bi], 1)
    for bi in bs:
        ans += bit.sum(compressed_b[bi])
print(ans)
