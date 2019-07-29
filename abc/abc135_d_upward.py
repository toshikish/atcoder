S = input()

MOD = 10 ** 9 + 7

dp = [0] * 13
dp[0] = 1
msb = 1
for i in range(len(S) - 1, -1, -1):
    new_dp = [0] * 13
    if S[i] == '?':
        for j in range(10):
            for k in range(13):
                new_dp[(j * msb + k) % 13] += dp[k]
                new_dp[(j * msb + k) % 13] %= MOD
    else:
        j = int(S[i])
        for k in range(13):
            new_dp[(j * msb + k) % 13] += dp[k]
            new_dp[(j * msb + k) % 13] %= MOD
    dp = new_dp[:]
    msb *= 10
    msb %= 13
print(dp[5])
