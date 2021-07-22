from copy import deepcopy

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * 32 for _ in range(4)]
dp[0][0] = 1_000_000_001

for i in range(N):
    dp2 = deepcopy(dp)
    for x in range(5):
        for j in range(3):
            for k in range(32):
                if k & 1 << x:
                    continue
                M = min(dp2[j][k], A[i][x])
                if dp2[j][k | 1 << x] < M:
                    dp2[j][k | 1 << x] = M
    for j in range(3):
        for k in range(32):
            if dp[j + 1][k] < dp2[j][k]:
                dp[j + 1][k] = dp2[j][k]

print(dp[3][31])
