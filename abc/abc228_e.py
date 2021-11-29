N, K, M = map(int, input().split())
MOD = 998244353

print(0 if M % MOD == 0 else pow(M, pow(K, N, MOD - 1), MOD))
