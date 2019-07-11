from collections import defaultdict

N, M = map(int, input().split())
a = defaultdict(lambda: True)
for i in range(M):
    a[int(input())] = False

dp = defaultdict(int)
dp[0] = 1
for i in range(1, N + 1):
    if a[i]:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N] % (10 ** 9 + 7))
