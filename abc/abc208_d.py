N, M = map(int, input().split())
INF = 1e16
dp = [[INF] * N for _ in range(N)]
for _ in range(M):
    Ai, Bi, Ci = map(int, input().split())
    Ai -= 1
    Bi -= 1
    dp[Ai][Bi] = Ci
for i in range(N):
    dp[i][i] = 0

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    ans += sum([sum([dp[i][j] for j in range(N) if dp[i][j] != INF])
                for i in range(N)])

print(ans)
