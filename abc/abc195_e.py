N = int(input())
S = input()
X = input()

dp = [[True] * 7 for _ in range(N)]
dp.append([True] + [False] * 6)
for i in range(N - 1, -1, -1):
    Si = int(S[i])
    if X[i] == 'A':
        for j in range(7):
            dp[i][j] = \
                dp[i + 1][(10 * j) % 7] and dp[i + 1][(10 * j + Si) % 7]
    else:
        for j in range(7):
            dp[i][j] = \
                dp[i + 1][(10 * j) % 7] or dp[i + 1][(10 * j + Si) % 7]

print('Takahashi' if dp[0][0] else 'Aoki')
