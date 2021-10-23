S = list(map(int, list(input())))[::-1]
MOD = 998244353

N = len(S)


def mpow(x):
    if x == 0:
        return 1
    p = mpow(x // 2)
    return (x % 2 + 1) * p * p % MOD


ans = 0
c = 2
for i in range(N):
    ans += S[i] * c
    ans %= MOD
    c = (c * 5 + 1) % MOD
if N == 1:
    ans //= 2
else:
    ans *= mpow(N - 2)
    ans %= MOD
print(ans)
