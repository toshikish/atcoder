from collections import defaultdict
from math import gcd


def normal(x, y):
    if x == 0:
        return (0, 1)
    elif y == 0:
        return (1, 0)
    g = gcd(x, y)
    x, y = x // g, y // g
    if x < 0:
        x, y = -x, -y
    return (x, y)


def orthogonal(T):
    if T[0] == 0:
        return (1, 0)
    elif T[1] == 0:
        return (0, 1)
    if T[1] > 0:
        return (T[1], -T[0])
    else:
        return (-T[1], T[0])


N = int(input())
C = defaultdict(int)
z = 0
for i in range(N):
    Ai, Bi = map(int, input().split())
    if Ai == Bi == 0:
        z += 1
        continue
    n = normal(Ai, Bi)
    C[n] += 1

MOD = 1000000007
B = [1] * (N + 1)
for i in range(1, N + 1):
    B[i] = B[i - 1] * 2 % MOD

ans = 1
calc = set()
for n, c in C.items():
    if n in calc:
        continue
    a = B[c]
    calc.add(n)
    no = orthogonal(n)
    if no in C:
        co = C[no]
        a += B[co] - 1
        calc.add(no)
    ans *= a
    ans %= MOD
print((ans - 1 + z) % MOD)
