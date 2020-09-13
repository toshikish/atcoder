N = int(input())

MOD = 1_000_000_007
a, b, c, d = 8, 1, 1, 0
for i in range(N - 1):
    a, b, c, d = 8 * a, a + 9 * b, a + 9 * c, b + c + 10 * d
    a %= MOD
    b %= MOD
    c %= MOD
    d %= MOD
print(d)
