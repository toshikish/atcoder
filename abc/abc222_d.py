from itertools import accumulate

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 998244353

dp = [1 if a[0] <= i <= b[0] else 0 for i in range(3001)]
for i in range(1, N):
    adp = list(accumulate(dp, lambda a, b: (a + b) % MOD))
    ndp = [0] * 3001
    for j in range(a[i], b[i] + 1):
        ndp[j] = adp[j]
    dp = ndp

print(sum(dp) % MOD)
