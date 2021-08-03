N, M, K = map(int, input().split())
NG = [[i] for i in range(N)]
for _ in range(M):
    Ui, Vi = map(lambda s: int(s) - 1, input().split())
    NG[Ui].append(Vi)
    NG[Vi].append(Ui)
MOD = 998244353

dp = [0] * N
dp[0] = 1
for _ in range(K):
    S = sum(dp) % MOD
    ndp = [S] * N
    for j in range(N):
        for k in NG[j]:
            ndp[j] -= dp[k]
        ndp[j] %= MOD
    dp = ndp

print(dp[0])
