from collections import defaultdict

N = int(input())
m = defaultdict(lambda: 10000000000)
M = defaultdict(lambda: -10000000000)
for _ in range(N):
    Xi, Ci = map(int, input().split())
    m[Ci] = min(Xi, m[Ci])
    M[Ci] = max(Xi, M[Ci])


def f0(s, l, r):
    return abs(r - s) + r - l


def f1(s, l, r):
    return abs(l - s) + r - l


dp = [0, 0]
l = r = 0
for Ci in sorted(m.keys()):
    ndp = [0] * 2
    nl, nr = m[Ci], M[Ci]
    ndp[0] = min(dp[0] + f0(l, nl, nr), dp[1] + f0(r, nl, nr))
    ndp[1] = min(dp[0] + f1(l, nl, nr), dp[1] + f1(r, nl, nr))
    dp = ndp
    l = nl
    r = nr
print(min(dp[0] + abs(l), dp[1] + abs(r)))
