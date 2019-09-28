from collections import defaultdict

N, M = map(int, input().split())
a = []
c = []
dp = defaultdict(lambda: 1000000000)
for i in range(M):
    ai, bi = map(int, input().split())
    a.append(ai)
    c.append(sum([1 << int(ci) - 1 for ci in input().split()]))

dp[0] = 0
for i in range(M):
    for k, v in list(dp.items()):
        dp[k | c[i]] = min(dp[k | c[i]], dp[k] + a[i])
print(dp[(1 << N) - 1] if (1 << N) - 1 in dp else -1)
