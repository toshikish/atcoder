N, M, K, S, T, X = map(int, input().split())
S -= 1
T -= 1
X -= 1
MOD = 998244353
G = [[] for _ in range(N)]
for _ in range(M):
    Ui, Vi = map(lambda s: int(s) - 1, input().split())
    G[Ui].append(Vi)
    G[Vi].append(Ui)

dp = [[0] * N for _ in range(2)]
dp[0][S] = 1
for _ in range(K):
    ndp = [[0] * N for _ in range(2)]
    for v in range(N):
        for nv in G[v]:
            if nv == X:
                ndp[1][nv] += dp[0][v]
                ndp[0][nv] += dp[1][v]
            else:
                ndp[0][nv] += dp[0][v]
                ndp[1][nv] += dp[1][v]
    dp = [[ndp[i][j] % MOD for j in range(N)] for i in range(2)]

print(dp[0][T])
