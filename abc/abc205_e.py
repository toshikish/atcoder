N, M, K = map(int, input().split())
MOD = 1_000_000_007


def nCr(x, y):
    if y < 0 or y > x:
        return 0
    n = d = 1
    for i in range(y):
        n = n * (x - i) % MOD
        d = d * (y - i) % MOD
    return n * pow(d, MOD - 2, MOD) % MOD


ans = 0
if N <= M + K:
    ans = nCr(M + N, N) - nCr(M + N, M + K + 1)
    ans %= MOD
print(ans)
