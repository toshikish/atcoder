X, Y = map(int, input().split())
MOD = 10 ** 9 + 7


def pow(a, b, p):
    if b == 0:
        return 1
    if b % 2 == 0:
        d = pow(a, b // 2, p)
        return (d * d) % p
    else:
        return (a * pow(a, b - 1, p)) % p


def fact(a, p):
    f = 1
    for i in range(1, a + 1):
        f *= i
        f %= p
    return f


if (X + Y) % 3 == 0:
    N = (X + Y) // 3
    if X - N >= 0 and Y - N >= 0:
        ans = fact(N, MOD) * pow(fact(X - N, MOD), MOD - 2, MOD) * \
            pow(fact(Y - N, MOD), MOD - 2, MOD)
        ans %= MOD
    else:
        ans = 0
else:
    ans = 0

print(ans)
