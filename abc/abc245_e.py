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

    def floor(self, x):
        s = self.sum(x)
        return self.kth_smallest(s) if s > 0 else 0

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


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

BD = sorted(set(B + D))
c = 1
BDI = {BD[0]: c}
for i in range(1, len(BD)):
    if BD[i - 1] < BD[i]:
        c += 1
    BDI[BD[i]] = c

plates = [(A[i], BDI[B[i]]) for i in range(N)]
boxes = [(C[i], BDI[D[i]]) for i in range(M)]
plates.sort()
boxes.sort()

i = 0
bit = BIT(c)
for j in range(M):
    while i < N and plates[i][0] <= boxes[j][0]:
        bit.add(plates[i][1], 1)
        i += 1
    if bit.sum(c) == 0:
        continue
    d = bit.floor(boxes[j][1])
    if d > 0:
        bit.add(d, -1)

print('Yes' if i == N and bit.sum(c) == 0 else 'No')
