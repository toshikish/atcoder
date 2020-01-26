H, N = map(int, input().split())
M = [tuple(map(int, input().split())) for i in range(N)]

dp = [(j + M[0][0] - 1) // M[0][0] * M[0][1] for j in range(H + 1)]
for i in range(1, N):
    Ai, Bi = M[i]
    ndp = [0] * (H + 1)
    if Ai >= H:
        ndp[0:H + 1] = [min(dp[j], Bi) for j in range(H + 1)]
    else:
        ndp[0:Ai + 1] = [min(dp[j], Bi) for j in range(Ai + 1)]
        for j in range(Ai + 1, H + 1):
            ndp[j] = min(dp[j], ndp[j - Ai] + Bi)
    dp = ndp
print(dp[H])
