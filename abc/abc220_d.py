N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

dp = [0] * 10
dp[A[0]] = 1
for i in range(1, N):
    ndp = [0] * 10
    for j in range(10):
        ndp[(j + A[i]) % 10] += dp[j]
        ndp[(j * A[i]) % 10] += dp[j]
    dp = [ndp[i] % MOD for i in range(10)]

for i in range(10):
    print(dp[i])
