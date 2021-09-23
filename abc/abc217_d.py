L, Q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

X = sorted(list(set([q[1] for q in queries] + [0, L])))
_X = {}
for i in range(len(X)):
    _X[X[i]] = i


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

    def upper_bound(self, x):
        s = self.sum(x)
        left = x
        right = self.n
        while left + 1 < right:
            mid = (left + right) // 2
            if self.sum(mid) == s:
                left = mid
            else:
                right = mid
        return right

    def lower_bound(self, x):
        s = self.sum(x)
        left = 0
        right = x
        while left + 1 < right:
            mid = (left + right) // 2
            if self.sum(mid) == s:
                right = mid
            else:
                left = mid
        return right


bit = BIT(len(X))
for ci, xi in queries:
    xi = _X[xi] + 1
    if ci == 1:
        bit.add(xi, 1)
    else:
        r = bit.upper_bound(xi)
        l = bit.lower_bound(xi)
        print(X[r - 1] - X[l - 1])
