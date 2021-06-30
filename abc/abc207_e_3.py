N = int(input())
A = list(map(int, input().split()))
MOD = 1_000_000_007

dp = [[1] + [0] * i for i in range(N)]
b = [[-1] * (i + 1) for i in range(N)]
b[0][0] = 0
S = 0
for i in range(N):
    S += A[i]
    for j in range(1, N):
        p = b[j][S % (j + 1)]
        # j <= i and p != -1 and j - 1 <= p
        if j <= p + 1:
            dp[i][j] = (dp[p][j] if j <= p else 0) + dp[p][j - 1]
            dp[i][j] %= MOD
        b[j][S % (j + 1)] = i

print(sum(dp[N - 1]) % MOD)
