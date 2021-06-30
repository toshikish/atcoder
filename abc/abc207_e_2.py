N = int(input())
A = list(map(int, input().split()))
MOD = 1_000_000_007

dp = [[0] * (i + 1) for i in range(N)]
dp[0][0] = 1
S = 0
for i in range(N - 1):
    S += A[i]
    for j in range(N - 1, 0, -1):
        dp[j][S % (j + 1)] += dp[j - 1][S % j]
        dp[j][S % (j + 1)] %= MOD
S += A[N - 1]
print(sum([dp[i][S % (i + 1)] for i in range(N)]) % MOD)
