S = input()
MOD = 1_000_000_007

W = 'chokudai'
dp = [0] * 9
dp[0] = 1
for i in range(len(S)):
    if S[i] not in W:
        continue
    idx = W.index(S[i])
    dp[idx + 1] += dp[idx]
    dp[idx + 1] %= MOD

print(dp[8])
