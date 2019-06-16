from collections import defaultdict
import functools
import itertools

N = int(input())
P = [tuple(map(int, input().split())) for i in range(N)]

D = defaultdict(list)
for p1, p2 in itertools.combinations(P, 2):
    d = (p1[0] - p2[0], p1[1] - p2[1])
    if d[0] == 0 and d[1] == 0:
        continue
    elif d[0] == 0:
        d = (0, abs(d[1]))
    elif d[0] < 0:
        d = (-d[0], -d[1])
    for S in D[d]:
        if p1 in S:
            S.add(p2)
            break
        elif p2 in S:
            S.add(p1)
            break
    else:
        D[d].append({p1, p2})

ans = 50
for L in D.values():
    ans = min(ans, len(L) + N - functools.reduce(lambda x, S: x + len(S), L, 0))
print(ans if N >= 2 else 1)
