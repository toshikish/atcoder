from collections import defaultdict

N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
MOD = 998244353

score = [(P[i], Q[i]) for i in range(N)]
score.sort()
dp = [defaultdict(int)]
dp[0][N + 1] = 1
for i in range(N):
    ndp = [defaultdict(int) for _ in range(min(i + 1, K) + 1)]
    for j in range(min(i, K) + 1):
        for k, v in dp[j].items():
            ndp[j][min(k, score[i][1])] += v
            ndp[j][min(k, score[i][1])] %= MOD
            if j + 1 <= K and k > score[i][1]:
                ndp[j + 1][k] += v
                ndp[j + 1][k] %= MOD
    dp = ndp

print(sum(dp[K].values()) % MOD)
