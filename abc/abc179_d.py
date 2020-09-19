N, K = map(int, input().split())
S = [tuple(map(int, input().split())) for i in range(K)]
MOD = 998244353

dp = [1]
acc = [0, 1]
for i in range(1, N):
    c = 0
    for lk, rk in S:
        if i - lk < 0:
            continue
        c += acc[i - lk + 1] - acc[max(i - rk, 0)]
    c %= MOD
    dp.append(c)
    acc.append((acc[-1] + dp[-1]) % MOD)
print(dp[N - 1])