H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MOD = 998244353

dp = [0] * 4
r = x1 == x2
c = y1 == y2
if c and r:
    dp[3] = 1
elif c:
    dp[1] = 1
elif r:
    dp[2] = 1
else:
    dp[0] = 1

for _ in range(K):
    ndp = [0] * 4
    ndp[0] = dp[0] * (H + W - 4) + dp[1] * (W - 1) + dp[2] * (H - 1)
    ndp[1] = dp[0] + dp[1] * (H - 2) + dp[3] * (H - 1)
    ndp[2] = dp[0] + dp[2] * (W - 2) + dp[3] * (W - 1)
    ndp[3] = dp[1] + dp[2]
    dp = [ndpi % MOD for ndpi in ndp]
print(dp[3])
