n, a, b = map(int, input().split())
MOD = 1000000007


def two_power(x):
    if x == 0:
        return 1
    half = two_power(x // 2)
    return half * half * (2 ** (x % 2)) % MOD


M = max(a, b)
inv = [0] * (M + 1)
inv[1] = 1
for i in range(2, M + 1):
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD


def nCk(x, y):
    ans = 1
    for i in range(1, y + 1):
        ans *= (x - i + 1) * inv[i]
        ans %= MOD
    return ans


ans = two_power(n) - nCk(n, a) - nCk(n, b) - 1
print(ans % MOD)
