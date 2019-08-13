from collections import defaultdict

N, A = map(int, input().split())
x = list(map(int, input().split()))

y = []
for xi in x:
    yi = xi - A
    y.append(yi)
X = max(x + [A])
NX = N * X

dp = defaultdict(int)
dp[(0, 0)] = 1
for i in range(N):
    for t in range(-NX, NX + 1):
        dp[(i + 1, t)] = dp[(i, t)] + dp[(i, t - y[i])]
print(dp[(N, 0)] - 1)
