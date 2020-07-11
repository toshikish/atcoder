from collections import defaultdict

N = int(input())
X = input()[::-1]


def popcount(n):
    p = 0
    while n > 0:
        p += n & 1
        n >>= 1
    return p


f = defaultdict(int)
for i in range(1, N + 1):
    f[i] = f[i % popcount(i)] + 1

P = X.count('1')
base = dict()
R = defaultdict(int)
for r in [P - 1, P + 1]:
    if r == 0:
        continue
    base[r] = [1] * N
    for i in range(1, N):
        base[r][i] = base[r][i - 1] * 2 % r
    R[r] = sum(base[r][i] * int(X[i]) for i in range(N)) % r

ans = [0] * N
for i in range(N):
    if X[i] == '1' and P == 1:
        ans[i] = 0
        continue
    if X[i] == '0':
        r = P + 1
        res = R[r] + base[r][i]
    else:
        r = P - 1
        res = R[r] - base[r][i]
    ans[i] = f[res % r] + 1

for i in range(N):
    print(ans[N - i - 1])
