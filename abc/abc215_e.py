N = int(input())
S = input()
MOD = 998244353

dp = [[0] * 11 for _ in range(1 << 10)]
dp[0][0] = 1

for i in range(N):
    x = ord(S[i]) - ord('A')
    for bit in range(1 << 10):
        if (bit >> x) & 1 == 0:
            continue
        dp[bit][x + 1] *= 2
        dp[bit][x + 1] %= MOD
    for bit in range(1 << 10):
        if (bit >> x) & 1 == 1:
            continue
        nbit = bit + (1 << x)
        dp[nbit][x + 1] += sum(dp[bit])
        dp[nbit][x + 1] %= MOD

print((sum(dp[i][j] for i in range(1 << 10) for j in range(11)) - 1) % MOD)
