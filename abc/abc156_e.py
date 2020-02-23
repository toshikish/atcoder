n, k = map(int, input().split())
MOD = 1000000007


def pow(x, t):
    if t == 0:
        return 1
    a = pow(x, t >> 1)
    return a * a * (x ** (t & 1)) % MOD


fact = [0] * (n + 1)
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i
    fact[i] %= MOD
ifact = [0] * (n + 1)
ifact[n] = pow(fact[n], MOD - 2)
for i in range(n, 0, -1):
    ifact[i - 1] = ifact[i] * i
    ifact[i - 1] %= MOD


def nCr(x, y):
    if y < 0 or y > x:
        return 0
    return fact[x] * ifact[y] * ifact[x - y] % MOD


ans = 0
for i in range(min(n - 1, k) + 1):
    ans += nCr(n, i) * nCr(n - 1, i)
    ans %= MOD
print(ans)
