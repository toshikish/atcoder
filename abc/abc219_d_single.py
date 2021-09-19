N = int(input())
X, Y = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

INF = N + 1
dp = [[INF] * (Y + 1) for _ in range(X + 1)]
dp[0][0] = 0
for i in range(N):
    Ai, Bi = P[i]
    for j in range(X, -1, -1):
        for k in range(Y, -1, -1):
            if j == X and k == Y:
                dp[j][k] = min(dp[j][k],
                               min(dp[jj][kk] for jj in range(max(0, j - Ai), X + 1) for kk in range(max(0, k - Bi), Y + 1)) + 1)
                continue
            if j == X:
                if k - Bi < 0:
                    continue
                dp[j][k] = min(dp[j][k],
                               min(dp[jj][k - Bi] for jj in range(max(0, j - Ai), X + 1)) + 1)
                continue
            if k == Y:
                if j - Ai < 0:
                    continue
                dp[j][k] = min(dp[j][k],
                               min(dp[j - Ai][kk] for kk in range(max(0, k - Bi), Y + 1)) + 1)
                continue
            if j - Ai < 0 or k - Bi < 0:
                continue
            dp[j][k] = min(dp[j][k], dp[j - Ai][k - Bi] + 1)

print(-1 if dp[X][Y] == INF else dp[X][Y])
