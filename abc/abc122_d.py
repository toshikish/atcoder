from collections import defaultdict

N = int(input())
MOD = 10 ** 9 + 7

dp = [defaultdict(int) for i in range(N + 1)]
dp[0]['TTT'] = 1
for length in range(N):
    for c1 in 'ACGT':
        for c2 in 'ACGT':
            for c3 in 'ACGT':
                if dp[length][c3 + c2 + c1] == 0:
                    continue
                for c0 in 'ACGT':
                    if c2 + c1 + c0 in ['AGC', 'ACG', 'GAC']:
                        continue
                    if c3 + c1 + c0 == 'AGC':
                        continue
                    if c3 + c2 + c0 == 'AGC':
                        continue
                    dp[length + 1][c2 + c1 + c0] += dp[length][c3 + c2 + c1]

print(sum(dp[N].values()) % MOD)
