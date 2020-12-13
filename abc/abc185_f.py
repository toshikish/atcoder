N, Q = map(int, input().split())
A = list(map(int, input().split()))


class BIT():
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s ^= self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] ^= x
            i += i & -i


bit = BIT(N)
for i in range(N):
    bit.add(i + 1, A[i])
for i in range(Q):
    Ti, Xi, Yi = map(int, input().split())
    if Ti == 1:
        bit.add(Xi, Yi)
    else:
        ans = bit.sum(Yi)
        if Xi >= 1:
            ans ^= bit.sum(Xi - 1)
        print(ans)
