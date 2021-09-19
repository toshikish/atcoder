N = int(input())
X, Y = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

INF = N + 1
dp = [[INF] * (Y + 1) for _ in range(X + 1)]
dp[0][0] = 0
for i in range(N):
    Ai, Bi = P[i]
    ndp = [[INF] * (Y + 1) for _ in range(X + 1)]
    for j in range(X + 1):
        for k in range(Y + 1):
            ndp[j][k] = min(ndp[j][k], dp[j][k])
            ndp[min(j + Ai, X)][min(k + Bi, Y)] \
                = min(ndp[min(j + Ai, X)][min(k + Bi, Y)], dp[j][k] + 1)
    dp = ndp

print(-1 if dp[X][Y] == INF else dp[X][Y])
