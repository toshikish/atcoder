from collections import Counter

S = list(input())
MOD = 998244353

N = 5001
fact = [0] * N
fact[0] = 1
for i in range(1, N):
    fact[i] = fact[i - 1] * i
    fact[i] %= MOD
ifact = [0] * N
ifact[N - 1] = pow(fact[N - 1], MOD - 2, MOD)
for i in range(N - 1, 0, -1):
    ifact[i - 1] = ifact[i] * i
    ifact[i - 1] %= MOD


def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * ifact[r] * ifact[n - r] % MOD


C = Counter(S)
N = 0
dp = [1]
for n in C.values():
    ndp = [0] * (N + n + 1)
    for i in range(N + 1):
        for j in range(n + 1):
            ndp[i + j] += dp[i] * nCr(i + j, j)
            ndp[i + j] %= MOD
    dp = ndp
    N += n
print((sum(dp) - 1) % MOD)
