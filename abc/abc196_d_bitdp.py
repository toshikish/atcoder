from collections import defaultdict

H, W, A, B = map(int, input().split())

dp = defaultdict(int)
dp[(0, A, B)] = 1
for i in range(H):
    for j in range(W):
        ndp = defaultdict(int)
        for key, value in dp.items():
            used, a, b = key
            if used >> j & 1:
                ndp[(used & ~(1 << j), a, b)] += value
            else:
                if b:
                    ndp[(used, a, b - 1)] += value
                if a:
                    if j <= W - 2 and not used & 1 << (j + 1):
                        ndp[(used | 1 << (j + 1), a - 1, b)] += value
                    if i <= H - 2:
                        ndp[(used | 1 << j, a - 1, b)] += value
        dp = ndp

print(dp[(0, 0, 0)])
