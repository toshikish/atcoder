from collections import Counter
from math import factorial, prod

S, K = input().split()
K = int(K)

C = Counter(S)


def f(k, D):
    if sum(D.values()) == 1:
        for l in D.keys():
            if D[l] == 1:
                return l
    t = 0
    for l in sorted(D.keys()):
        if D[l] == 0:
            del D[l]
            continue
        D[l] -= 1
        p = factorial(sum(D.values())) \
            // prod(factorial(v) for v in D.values())
        if k <= t + p:
            return l + f(k - t, D)
        D[l] += 1
        t += p


print(f(K, C))
