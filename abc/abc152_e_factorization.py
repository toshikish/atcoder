from collections import defaultdict

MOD = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))

max_A = max(A)
f = list(range(max_A + 1))
for i in range(2, int(max_A ** 0.5) + 1):
    if f[i] == i:
        f[i::i] = [i] * (max_A // i)


def factors(x):
    factor = defaultdict(int)
    while x != 1:
        factor[f[x]] += 1
        x //= f[x]
    return factor


L_factors = defaultdict(int)
for Ai in A:
    for p, index in factors(Ai).items():
        L_factors[p] = max(L_factors[p], index)
L = 1
for p, index in L_factors.items():
    if index == 0:
        continue
    L *= pow(p, index, MOD)
    L %= MOD

ans = 0
for Ai in A:
    ans += L * pow(Ai, MOD - 2, MOD)
    ans %= MOD
print(ans % MOD)
