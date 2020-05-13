from itertools import product

N = int(input())
c = input()

ans = N
for LR in product('ABXY', repeat=4):
    LR = ''.join(LR)
    L, R = LR[:2], LR[2:]
    dp = list(range(N + 1))
    for i in range(1, N):
        if c[i - 1:i + 1] == L:
            dp[i + 1] = min(dp[i - 1] + 1, dp[i + 1])
        elif c[i - 1:i + 1] == R:
            dp[i + 1] = min(dp[i - 1] + 1, dp[i + 1])
        else:
            dp[i + 1] = min(dp[i] + 1, dp[i + 1])
    ans = min(ans, dp[N])

print(ans)
