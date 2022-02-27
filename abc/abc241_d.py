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

    def kth_smallest(self, k):
        i = 0
        base = 1
        while base < self.n:
            base <<= 1
        width = base
        total = 0
        while width > 0:
            if i + width <= self.n and total + self.bit[i + width] < k:
                total += self.bit[i + width]
                i += width
            width >>= 1
        return i + 1


Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

X = sorted(set(queries[i][1] for i in range(Q)))
XI = {}
IX = {}
for i, x in enumerate(X):
    i += 1
    XI[i] = x
    IX[x] = i
N = len(X)

bit = BIT(N)
for query in queries:
    if query[0] == 1:
        bit.add(IX[query[1]], 1)
        continue
    x, k = query[1:]
    ix = IX[x]
    if query[0] == 2:
        s = bit.sum(ix)
        if s < k:
            ans = -1
        else:
            ans = XI[bit.kth_smallest(s - k + 1)]
    else:
        s = bit.sum(ix - 1)
        if bit.sum(N) - s < k:
            ans = -1
        else:
            ans = XI[bit.kth_smallest(s + k)]
    print(ans)
