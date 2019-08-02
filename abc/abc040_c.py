N = int(input())
a = list(map(int, input().split()))

dp = {0: 0, 1: abs(a[1] - a[0])}
for i in range(2, N):
    dp[i] = min(dp[i - 1] + abs(a[i] - a[i - 1]),
                dp[i - 2] + abs(a[i] - a[i - 2]))
print(dp[N - 1])
