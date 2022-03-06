N = int(input())
MOD = 998244353

a = b = c = d = e = 1
for i in range(N - 1):
    a, b, c, d, e = a + b, a + b + c, b + c + d, c + d + e, d * 2 + e
    if i % 16 == 0:
        a %= MOD
        b %= MOD
        c %= MOD
        d %= MOD
        e %= MOD

print(((a + b + c + d) * 2 + e) % MOD)
