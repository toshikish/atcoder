N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7


def pow(x, t):
    if t == 0:
        return 1
    a = pow(x, t >> 1)
    return a * a * (x ** (t & 1)) % MOD


fact = [0] * N
fact[0] = 1
for i in range(1, N):
    fact[i] = fact[i - 1] * i
    fact[i] %= MOD
ifact = [0] * N
ifact[N - 1] = pow(fact[N - 1], MOD - 2)
for i in range(N - 1, 0, -1):
    ifact[i - 1] = ifact[i] * i
    ifact[i - 1] %= MOD


def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * ifact[r] * ifact[n - r] % MOD


A.sort()
ans = 0
for i in range(K, N + 1):
    C = nCr(i - 1, K - 1)
    ans += A[i - 1] * C
    ans -= A[N - i] * C
    ans %= MOD
print(ans)
