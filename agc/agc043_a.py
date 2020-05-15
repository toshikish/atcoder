H, W = map(int, input().split())
s = [input() for i in range(H)]

dp = [[0] * W for i in range(H)]

for i in range(H):
    for j in range(W):
        if i == j == 0:
            if s[i][j] == '#':
                dp[i][j] = 1
            continue
        c = []
        if 0 <= i - 1 < H:
            c.append(dp[i - 1][j]
                     + (1 if s[i - 1][j] == '.' and s[i][j] == '#' else 0))
        if 0 <= j - 1 < W:
            c.append(dp[i][j - 1]
                     + (1 if s[i][j - 1] == '.' and s[i][j] == '#' else 0))
        if len(c) > 0:
            dp[i][j] = min(c)

print(dp[H - 1][W - 1])
