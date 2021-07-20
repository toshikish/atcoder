H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
INF = 1e14

ans = INF

for _ in range(2):
    dp = [[INF] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            s = A[i][j]
            if i - 1 >= 0:
                s = min(s, dp[i - 1][j] + C)
                ans = min(ans, dp[i - 1][j] + C + A[i][j])
            if j - 1 >= 0:
                s = min(s, dp[i][j - 1] + C)
                ans = min(ans, dp[i][j - 1] + C + A[i][j])
            dp[i][j] = s
    A = A[::-1]

print(ans)
