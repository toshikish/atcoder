S = input()

MOD = 10 ** 9 + 7

dp = [0] * 13
dp[0] = 1
for i in range(len(S)):
    new_dp = [0] * 13
    if S[i] == '?':
        for j in range(10):
            for k in range(13):
                new_dp[(k * 10 + j) % 13] += dp[k]
                new_dp[(k * 10 + j) % 13] %= MOD
    else:
        j = int(S[i])
        for k in range(13):
            new_dp[(k * 10 + j) % 13] += dp[k]
            new_dp[(k * 10 + j) % 13] %= MOD
    dp = new_dp[:]
print(dp[5])
