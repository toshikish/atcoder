from math import sqrt

N = int(input())


def f(x):
    n = N
    while n % x == 0:
        n //= x
    return n % x == 1


ans = 1
for k in range(2, int(sqrt(N)) + 1):
    res = N % k
    if res == 0:
        k1, k2 = k, N // k
        ans += 1 if f(k1) else 0
        ans += 1 if k1 != k2 and f(k2) else 0
    elif res == 1:
        ans += 1 if k == (N - 1) // k else 2
if N >= 3:
    ans += 1

print(ans)
