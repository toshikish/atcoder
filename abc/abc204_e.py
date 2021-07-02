from heapq import heappop, heappush
from math import isqrt

N, M = map(int, input().split())
nx = [[] for _ in range(N)]
for _ in range(M):
    Ai, Bi, Ci, Di = map(int, input().split())
    if Ai == Bi:
        continue
    Ai -= 1
    Bi -= 1
    nx[Ai].append((Bi, Ci, Di))
    nx[Bi].append((Ai, Ci, Di))


def f(t, C, D):
    if (t + 1) * (t + 1) >= D:
        td = t
        return t + C + D // (t + 1)
    t1 = isqrt(D) - 1
    t2 = t1 + 1
    return min(t1 + D // (t1 + 1), t2 + D // (t2 + 1)) + C


INF = 1e20
d = [INF] * N
d[0] = 0
used = [False] * N
hq = [(0, 0)]
while hq:
    t, v = heappop(hq)
    if used[v]:
        continue
    used[v] = True
    for nv, C, D in nx[v]:
        if used[nv]:
            continue
        nt = f(t, C, D)
        if nt < d[nv]:
            d[nv] = nt
            heappush(hq, (nt, nv))

print(d[N - 1] if used[N - 1] else -1)
